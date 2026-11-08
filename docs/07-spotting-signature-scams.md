# Chapter 7: Spotting Signature Scams

E-signature fraud is popular with scammers for a simple reason: the real thing is
so routine that nobody questions a "please sign this" email. This chapter shows you
the tells, the traps, and the recoveries. Ten minutes of reading here beats any
single tool purchase.

## The three big scam families

### Family 1: Fake signature requests (phishing)

**The play:** an email or text that looks like a DocuSign/Dropbox Sign/Adobe
request. It says "Document ready for signature — Review Document." The button
leads not to the real service, but to a credential-harvesting clone ("log in to
view the document"), a malware download disguised as a PDF, or a billing trap.

**The tells:**

- **The sender address has a real service name but a fake domain.** Real DocuSign
  requests come from `@docusign.net` (yes, the request system uses `.net`; the
  company's main site is `.com`). Lookalikes use `docusign-alerts.com`-style
  domains, oddly spelled brand mash-ups, or a personal Gmail pretending to be HR.
- **No context.** You have no pending signature with "the accounting department,"
  no pending lease, no deal. Real requests have context.
- **Urgency:** "expires in 24 hours," "final notice," "resignature required today."
  Real services do warn about expiring envelopes, but combined with a fake domain
  urgency is a scam tell, not a service feature.
- **Hover the button.** On a computer, hover (don't click) and read the URL in the
  corner. It should be the real service domain. On a phone, long-press the link to
  preview the URL. If the pre-click link shows a different site than the visible
  text, done — close it.
- **Attachment called something like `doc_8823.pdf.zip` or an HTML file** that
  opens a "log in to view" page. No legitimate service sends you a zip of a
  signature. No service asks you to "log in" from an HTML attachment.

**Safe pattern to build:** if an email says "sign here," but you expected it, go
to that service yourself — open a new browser tab, type the service's real address
or use the app on your phone, and log in there to see the pending request. Never
follow the emailed link on first contact. If the request is real, it will be
sitting in your real account's dashboard.

### Family 2: You are the one being scammed into signing

**The play:** a signing request whose *content* is the trap. Common ones:

- **Free-trial burial:** "sign to download your report" — the doc includes terms
  enrolling you in a subscription. Scheduled recurring charges follow.
- **Fake job / fake landlord:** they need "your signature" but really they need
  your SSN, ID photos, bank details. Persona theft dressed as paperwork.
- **Wrapped agreements:** page 14 of 16 says "by signing you agree to arbitration
  with [company] in [faraway state]" — not a scam per se, but a trap worth
  noticing before you sign.
- **Refund/tech-support scam finisher:** a scammer on the phone tells you "I need
  you to sign this remote-access approval" — signing gives them control of your
  device or account.

**The counter-measure is Chapter 1's one-minute pre-sign check, plus two more:**

- **Never sign under time pressure across an unsolicited channel.** Scammers
  manufacture urgency; legitimate paperwork rarely does.
- **Search the company name + "scam" or "reviews"** before anything that asks for
  ID, bank details, or a recurring-payment consent. Two minutes, every time.

### Family 3: Real signatures, fake documents

**The plays:**

- **The stacked PDF:** you sign page 1 of what looks like a single agreement; your
  signature image gets pasted onto an entirely different contract.
- **Scope creep:** the terms change after your mark is on it.
- **Signature reuse:** a signature image you emailed once for a friendly form
  resurfaces on a document you never saw.

**Who is exposed:** anyone who emails signature images around, posts them to
forms, or lets a stranger "handle the paperwork."

**Your defense:**

1. **Sign inside files, visibly.** When you sign a PDF Chapter 3–4 style, your mark
   sits inside the pages with your name's date next to fields — not as a lone
   floating image shared separately.
2. **Prefer certificate-signed output (free, Chapter 3)** for anything with real
   stakes: an Adobe certificate signature locks the entire file, making
   page-swaps detectable by anyone who opens the result.
3. **Neveremail a blank signature image to an unknown party.** If a form truly
   needs just a signature image and you do not know the company, send the signed
   PDF page instead — the mark appears only in context.
4. **Read around your signature.** Glance at what is above and below the signature
   line on the actual page — a healthy habit that catches both scope creep and
   page-stacking.

## E-signature fraud that targets the *sender* side

If you run a small business or asking others to sign (invoices, agreements):

- **Redirect scams:** someone emails pretending to be an employee/vendor with a
  "new bank details authorization to sign" — classic wire fraud. Verify bank-info
  changes by phone, on a number known independently, always.
- **Imposter envelopes:** a fraudster sends someone a DocuSign request pretending
  to be you. If a signer contacts you saying "I got a request I don't recognize,"
  treat it as an incident: log into your real account, check envelopes, change
  passwords.
- **Templates poisoned by lookalike services:** if others sign "your" doc via a
  tiny unknown service, the audit trail is that service's say-so. For anything
  consequential, use a major, established service (Chapter 2) so the audit story
  is strong.

## Red-flag checklist (print this / screenshot it)

□ Sender email domain matches the real service (or is a person you know)
□ The request makes sense — you expected it, context is known
□ URL where the button leads (hover/long-press) is the real service domain
□ No payment or card entry needed to *view* a document
□ No "log in" page inside a downloaded file
□ Content on the signing page matches what was described
□ I read the pages around the signature
□ Nothing on this page signs me up for recurring charges
□ I'll get a completed copy (or I have screenshots of everything)
□ Nobody asked me to sign while on an unexpected phone call "to fix" something

Five or more unchecked = stop and verify by an independent route (call the
organization on a number you looked up yourself).

## If you already clicked or signed something sketchy

Sorted by escalating badness:

1. **Clicked the link only:** nothing done yet; don't log in. Just run the device's
  normal security scan if any; move on. (Clicking alone rarely does harm unless
  you then entered credentials or downloaded a file.)
2. **Entered your password on a fake page:** change that password immediately
   (from a trusted device), then any other site where you reused it. Turn on
   two-factor authentication where the service offers it.
3. **Downloaded and opened a file:** disconnect from the internet, run a real
   antivirus scan (Windows Defender is built-in and fine), and if strange behavior
   follows, get a techie friend or a repair shop to look — recovery from
   "unknown download" is a real-world solvable problem.
4. **Signed a document under false pretenses:** save every message and the signed
   copy (Chapter 6's naming), then contact the real company/bank with the evidence
   bundle; report to **reportfraud.ftc.gov** (US) and your state attorney general's
   consumer page. If money moved through a bank, call the bank's fraud line first,
   quickly — banks have reversal processes that work best same-day.
5. **Gave SSN/ID photos:** report at **identitytheft.gov** (creates your recovery
   plan), file credit freezes with the three bureaus (Equifax, Experian,
   TransUnion — free, takes minutes online each), and watch your mail for new
   account statements you did not open.

## The calm reframe

Scammers succeed when they rush you and when you contact them through their own
channel. Almost every protective habit in this chapter is a sentence long: go to
the service directly, hover first, read around your name, never sign under phone
pressure. That is the whole game.
