# Chapter 3: Signing a PDF on Your Computer

You have a PDF that needs your signature. Here are the tall-free trees to shake:
Windows, Mac, and Linux, using only built-in or genuinely free tools.

## The universal no-account method (any computer)

Open the PDF in your browser (Chrome, Edge, Firefox, Safari — click the file, or
drag it into a browser window). Modern browsers can add text boxes and draw a
signature directly on the PDF, then let you print or save the completed file.

- **Edge (Windows):** open the PDF → toolbar **Draw** and **Add text** → save
  with **Save as**.
- **Chrome:** open the PDF → use the **annotate** tools (text/draw) → save via
  print → "Save as PDF."
- **Firefox:** open → use the built-in text highlighting and drawing tools →
  download the edited copy.

Best for: form fills and quick draws when you do not want to install anything at
all. Limitation: no saved signature image and no tamper-evidence certificate.

## The best free method: signing tools on each platform

### Windows: Adobe Acrobat Reader (free)

Adobe's free Reader is safe when downloaded from Adobe's own site
(`adobe.com/acrobat/pdf-reader`). Steps:

1. Open your PDF in Acrobat Reader.
2. Click **Fill & Sign** in the right-hand toolbar (or Tools → Fill & Sign).
3. Click **Sign yourself** → **Add signature**.
4. Choose: **Type** (pick a handwriting-ish font), **Draw** (mouse or trackpad's stiff
   finger mode), or **Image** (upload your signature photo from Chapter 2).
5. Click once on the PDF where you want it; drag to size; it now behaves like
   form content.
6. To fill text fields, click **Fill & Sign → Add text**, then click fields and type.
7. **File → Save** (yes, keep the same format; no "export" step needed).

Optional upgrade — **a certificate-based signature** (tamper-evident, free, two
minutes):

1. Tools → **Use a certificate** → **Digitally sign**.
2. When asked for a Digital ID, choose "Configure a new Digital ID," then select
   "Create a new Digital ID." As the destination, pick "Save to File" (the simple
   option, not the more exotic ones).
3. Fill in just a name and email (use your real name and your normal email). Set a
   password you will remember.
4. Now "Digitally sign" draws a box on the PDF; when you save, the file locks:
   Acrobat shows a green check and the text "document has not been modified
   since it was signed," which is exactly the sentence you want a landlord or
   a court to see.

Get the *sibling PDF Everyday Handbook* if you need heavy editing beyond signing.

### Mac: Preview (already installed, best in class)

1. Open the PDF in **Preview** (double-click, or right-click → Open With → Preview).
2. Click the **Markup** pencil icon; if the toolbar lacks the signature button,
   View → Customize Toolbar → drag **Sign** onto it.
3. Click **Sign** → **Create Signature** (first time only). Choose:
   - **Trackpad**: sign with your finger on the trackpad.
   - **Camera**: hold your paper-signed name up to the webcam on the guide line —
     Preview grabs it, straightens, and makes the background transparent. This one
     is magic and takes 20 seconds.
4. Once created, click Sign → your signature → click on the page to place it.
5. Use **text boxes** (Markup "T") for typed fields.
6. **File → Save** or Export.

Preview saves your signatures for reuse across all documents on that Mac — no
account, no cloud, stays on your Mac.

### Linux

- **Okular** (KDE): open → Tools → Annotations → freehand/text signatures.
- **Xournal++**: excellent for hand-drawn placement; export final PDF.
- **Adobe Acrobat Reader** also exists as a snap/flatpak on many distros and
  supports the digital-certificate flow described above.

## Which method, one-line answers

| You need... | Easiest free answer |
|---|---|
| Type my name on one form | Your browser's Add Text; or Acrobat Reader Fill & Sign |
| Draw with finger/mouse | Mac Preview trackpad; Acrobat Reader Draw; Xournal++ |
| My real paper signature on the file | Camera capture in Preview, or signature image (Chapter 2) |
| Tamper-proof signature box | Acrobat Reader certificate (2 minutes, free) |
| No account, no uploads of any kind | Built-in tools: Preview, Edge, Okular, or browser annotate |

## When the PDF has real form fields vs when it doesn't

Some PDFs have actual fillable form fields (gray boxes, tab-jump fields). Great
tools for those: **Acrobat Reader** is reliable at detecting and filling them;
browsers usually handle them too.

Some PDFs are just "a printed page turned into a PDF" — no real fields. Then you
overlay: add text boxes and signature marks wherever the underline demands it.
Every tool above does this. Type, click, place, save. Do not stress about pixel
perfection; readability is the bar.

## The post-sign checklist (this becomes Chapter 6's first habit)

1. **Open the saved copy and look at it.** Every signature present? Every field
   filled? Name spelled right? Date right?
2. **Save it where you will look later** — naming and filing come in Chapter 6.
3. **If you used the tool request flow** (someone sent the request via DocuSign
   or similar), download the **completed PDF with the audit certificate** they
   offer. Do it while you are in the flow; it is the receipt for the whole event.
4. **Email it to yourself** as the low-tech second copy, especially on a shared
   or borrowed computer.
