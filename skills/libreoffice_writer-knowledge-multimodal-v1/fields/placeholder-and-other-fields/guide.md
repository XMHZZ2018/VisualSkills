# Placeholder and Other Fields (LibreOffice Writer 7.3.7)

A placeholder field is basically a "fill in later" marker — it prompts you (or someone else) to insert text, a table, a frame, an image, or an object when the field is clicked in the document. They're great for templates where you want to leave clear spots for content.

To create one, open the Fields dialog via **Insert > Fields > More Fields**, then head to the **Functions** tab. Pick **Placeholder** in the *Type* column, then choose what kind of placeholder you need (Text, Table, Frame, Image, or Object) from the *Format* column. Type a label in the **Placeholder** box — this is the hint text that appears in the document — and optionally add a tooltip in the **Reference** box that shows when someone hovers over it.

See `fig01.png`.

What happens when you click a placeholder depends on its type. An Image placeholder opens the Insert Image dialog so you can browse for a file; selecting one and clicking **Open** drops it right in. A Table placeholder opens the Insert Table dialog, a Frame placeholder opens the Frame dialog, and an Object placeholder opens Insert OLE Object. The Text placeholder is the simplest — just click it and start typing in the **Placeholder** box to replace it inline.

## Other fields

LibreOffice Writer has a bunch of additional field types beyond what's covered here — things like database fields, conditional text, and more. Most of these are tucked away in the same **Insert > Fields > More Fields** dialog across its various tabs. The built-in Help system is the best place to dig into them when you need something specific.

## Classifying document contents

If you work somewhere that cares about document security classifications, Writer supports the TSCP (Transglobal Secure Collaboration Participation) open standard. It uses three BAF (Business Authentication Framework) categories — Intellectual Property, National Security, and Export Control — each with four BAILS levels: Non-Business, General Business, Confidential, and Internal Only.

To turn it on, enable the TSCP toolbar via **View > Toolbars > TSCP Classification**. This gives you dropdown list boxes for picking a security level. Writer stores the classification as custom fields in your document properties (**File > Properties, Custom Properties** tab), treating it as proper metadata.

One handy safeguard: content from a document with a higher classification level can't be pasted into a document with a lower one, helping prevent accidental leaks.
