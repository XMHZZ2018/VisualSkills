# Emailing and Digitally Signing Documents (LibreOffice Writer 7.3.7)

## Emailing Documents

LibreOffice makes it easy to send your current document as an email attachment in several formats. Head to **File > Send > Email Document** (or **File > Send > Email as OpenDocument Text**) and your default email client opens with the file already attached. From there, just fill in the recipient, subject, and message body, then send.

If you'd rather send it in a different format, choose *Email as Microsoft Word* to convert to .docx first, or *Email as PDF* to export a PDF before attaching. With the PDF option, Writer pops open the PDF Options dialog so you can tweak settings before the file is handed off to your mail client.

Need to send to a bunch of people at once? You can use your email program's built-in features, or tap into Writer's mail merge facilities — the Mail Merge Wizard or manual merge without the wizard. Chapter 14 of the Writer Guide covers mail merge in detail.

## Digital Signing of Documents

Digital signatures let you prove a document is authentic and hasn't been tampered with. To sign, you need a personal key (certificate) — a private key you keep secret, paired with a public key that gets embedded in the document. You can obtain a certificate from a certificate authority, whether private or governmental.

When you sign a document, a checksum is computed from the content plus your personal key. Anyone who later opens the file in LibreOffice can verify the checksum against the stored one; if they match, the document is unchanged. LibreOffice can also check the public key against the certificate authority's website, so forgery is caught. A signed document shows an icon in the Status bar — double-click it to view the certificate. You can add multiple signatures, but changing the document after signing invalidates existing signatures.

## Applying a Digital Signature

To sign your document, go to **File > Digital Signatures > Digital Signatures**. If the document has unsaved changes, Writer will prompt you to save first — click **Yes** twice (once to confirm, once to actually save). The Digital Signatures dialog lists any existing signatures; click **Sign Document** to add yours.

See `fig01.png`.

In the Select Certificate dialog that appears, pick your certificate, optionally add a description, and click **Sign**. The certificate shows up in the list with a status icon next to its name. Click **Close** to finish applying the signature.

See `fig02.png`.

## Including a Signature Line

You can also insert a visible signature placeholder into your document via **Insert > Signature Line**. This creates a graphic box where you fill in the suggested signer's name, title, and email. Options like allowing comments and showing the sign date are available. Once placed, the signature line can be signed with an actual digital certificate.

See `fig03.png`.
