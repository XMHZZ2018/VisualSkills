"""Small PIL-based image helper invoked by the Phase-2 assembler via Bash.

Subcommands
-----------
crop       Tight crop to bbox.   --bbox L,T,R,B  (pixels in 1920x1080 space)
annotate   Draw a red rectangle on a full-size shot to highlight a region.
compose    Stack two images side-by-side (horizontal) or top-bottom (vertical).

All coordinates are in the NATIVE docker screenshot resolution (1920x1080),
which is what the bridge saves to `screenshots/step_NNN.png`.

Exit code 0 on success, non-zero on error.  Prints the output path on success.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.stderr.write(
        "img_tool.py needs Pillow: pip install Pillow\n"
    )
    raise


def _parse_bbox(s: str) -> tuple[int, int, int, int]:
    parts = [int(p.strip()) for p in s.split(",")]
    if len(parts) != 4:
        raise ValueError(f"bbox must be L,T,R,B (4 ints), got {s!r}")
    l, t, r, b = parts
    if r <= l or b <= t:
        raise ValueError(f"bbox must have R>L and B>T, got L={l} T={t} R={r} B={b}")
    return l, t, r, b


def _clamp_bbox(img: Image.Image, bbox: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    l, t, r, b = bbox
    w, h = img.size
    return max(0, l), max(0, t), min(w, r), min(h, b)


def cmd_crop(args: argparse.Namespace) -> int:
    img = Image.open(args.input)
    bbox = _clamp_bbox(img, _parse_bbox(args.bbox))
    cropped = img.crop(bbox)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(out_path, format="PNG", optimize=True)
    print(out_path)
    return 0


def cmd_annotate(args: argparse.Namespace) -> int:
    img = Image.open(args.input).convert("RGB")
    bbox = _clamp_bbox(img, _parse_bbox(args.bbox))
    draw = ImageDraw.Draw(img)
    draw.rectangle(bbox, outline=args.color, width=args.width)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, format="PNG", optimize=True)
    print(out_path)
    return 0


def cmd_compose(args: argparse.Namespace) -> int:
    inputs = [Image.open(p).convert("RGB") for p in args.inputs.split(",")]
    if not inputs:
        raise ValueError("no inputs")
    pad = args.pad
    bg = (255, 255, 255)

    if args.direction == "horizontal":
        h = max(im.height for im in inputs)
        w = sum(im.width for im in inputs) + pad * (len(inputs) - 1)
        canvas = Image.new("RGB", (w, h), bg)
        x = 0
        for im in inputs:
            canvas.paste(im, (x, (h - im.height) // 2))
            x += im.width + pad
    else:  # vertical
        w = max(im.width for im in inputs)
        h = sum(im.height for im in inputs) + pad * (len(inputs) - 1)
        canvas = Image.new("RGB", (w, h), bg)
        y = 0
        for im in inputs:
            canvas.paste(im, ((w - im.width) // 2, y))
            y += im.height + pad

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, format="PNG", optimize=True)
    print(out_path)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_crop = sub.add_parser("crop", help="Tight crop to bbox")
    p_crop.add_argument("--input", required=True)
    p_crop.add_argument("--output", required=True)
    p_crop.add_argument("--bbox", required=True, help="L,T,R,B in 1920x1080 pixels")
    p_crop.set_defaults(func=cmd_crop)

    p_ann = sub.add_parser("annotate", help="Draw a red rectangle on a full shot")
    p_ann.add_argument("--input", required=True)
    p_ann.add_argument("--output", required=True)
    p_ann.add_argument("--bbox", required=True, help="L,T,R,B in 1920x1080 pixels")
    p_ann.add_argument("--color", default="red")
    p_ann.add_argument("--width", type=int, default=6)
    p_ann.set_defaults(func=cmd_annotate)

    p_comp = sub.add_parser("compose", help="Side-by-side or top-bottom")
    p_comp.add_argument("--inputs", required=True, help="comma-separated PNG paths")
    p_comp.add_argument("--output", required=True)
    p_comp.add_argument("--direction", choices=("horizontal", "vertical"),
                        default="horizontal")
    p_comp.add_argument("--pad", type=int, default=12)
    p_comp.set_defaults(func=cmd_compose)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
