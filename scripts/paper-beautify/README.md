# Paper Beautify

Format a LaTeX paper by learning from published papers in the same venue.

## Commands

```
./run.sh <paper.zip>          # Extract zip to workspace/
/setup-paper-refs              # Search & download reference paper images
/format-paper                  # Analyze references, apply formatting, compile PDF
```

## Example

```
./run.sh ~/Downloads/my_paper_COLM2026.zip
/setup-paper-refs
/format-paper
```

## Workspace

Extracted paper files live in `workspace/`. Output PDF and `CHANGES.md` are saved there too.
