"""Generates the HTML pages of deductrail.com. Run from anywhere: python3 src/build.py
Writes index.html, delete-account/index.html, privacy/index.html and 404.html in the repo root.
assets/site.css and the files in assets/ are edited by hand and are not generated.
"""
import os
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE='https://deductrail.com'
def ic(*parts, extra=''):
    inner=''.join(p if p.startswith('<') else f'<path d="{p}"/>' for p in parts)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"{extra}>{inner}</svg>'
I={
 'nav':ic('<polygon points="3 11 22 2 13 21 11 13 3 11"/>'),
 'split':ic('M16 3h5v5','M8 3H3v5','M12 22v-8.3a4 4 0 0 0-1.172-2.872L3 3','m15 9 6-6'),
 'gauge':ic('m12 14 4-4','M3.34 19a10 10 0 1 1 17.32 0'),
 'pen':ic('M12 20h9','M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z'),
 'camera':ic('M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z','<circle cx="12" cy="13" r="3"/>'),
 'file':ic('M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z','M14 2v4a2 2 0 0 0 2 2h4','M16 13H8','M16 17H8','M10 9H8'),
 'download':ic('M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4','m7 10 5 5 5-5','M12 15V3'),
 'brief':ic('<rect x="2" y="7" width="20" height="14" rx="2"/>','M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16'),
 'sync':ic('M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8','M3 3v5h5','M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16','M16 16h5v5'),
 'check':ic('M20 6 9 17l-5-5'),
 'mail':ic('<rect x="2" y="4" width="20" height="16" rx="2"/>','m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7'),
 'phone':ic('<rect x="5" y="2" width="14" height="20" rx="2.5"/>','M11 18h2', extra=' fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"'),
}
def page(path,title,desc,body,canon=None,noindex=False):
    canon=canon if canon is not None else path
    url=SITE+canon
    head=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#2347B8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B0F16" media="(prefers-color-scheme: dark)">
{'<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'}
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/IBMPlexSans_600SemiBold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/IBMPlexSans_400Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Deductrail">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Deductrail app icon and the line: Every business mile, on the record.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/og.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Deductrail home"><img src="/assets/img/icon-rounded.svg" alt="" width="32" height="32">Deductrail</a>
    <nav class="nav" aria-label="Main">
      <a href="/#features">Features</a>
      <a href="/#how">How it works</a>
      <a href="/#privacy">Privacy</a>
      <a href="/#faq">FAQ</a>
      <a class="cta" href="/#contact">Contact</a>
    </nav>
  </div>
</header>
<main id="main">
'''
    foot='''</main>
<footer class="site-footer">
  <div class="wrap">
    <p>© 2026 Wade Works LLC</p>
    <nav aria-label="Footer">
      <a href="/privacy/">Privacy</a>
      <a href="/delete-account/">Delete account</a>
      <a href="mailto:support@deductrail.com">support@deductrail.com</a>
    </nav>
    <p class="fine">Deductrail estimates deductions to help you keep records. It isn’t tax, legal or accounting advice. Deductrail is made by Wade Works LLC in Indiana.</p>
  </div>
</footer>
</body>
</html>
'''
    fp=os.path.join(OUT,path.strip('/'),'index.html') if path.endswith('/') else os.path.join(OUT,path.strip('/'))
    os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'w').write(head+body+foot)

def card(icon,title,text,tone='',tag=''):
    t=f'<span class="tag">{tag}</span>' if tag else ''
    return f'''      <article class="card"><div class="icon {tone}">{I[icon]}</div><h3>{title}{t}</h3><p>{text}</p></article>\n'''

def check(b,s): return f'        <li>{I["check"]}<div><b>{b}</b><span>{s}</span></div></li>\n'
def faq(q,a): return f'      <details><summary>{q}</summary><p>{a}</p></details>\n'

features=''.join([
 card('nav','Records the trips you start','Tap Start trip and Deductrail measures the miles with GPS. It keeps recording when you lock your phone or switch apps, until you hold to stop.','teal'),
 card('split','Business, personal or commute','Mark each trip and add its business purpose. Trips missing a purpose get their own filter, and personal and commute miles stay out of your deduction.'),
 card('gauge','IRS standard mileage rate','Each trip uses the IRS business rate in effect on the day you drove, including mid-year changes, so you see an estimated deduction as you go.'),
 card('pen','Manual and odometer trips','Forgot to start a trip? Add it by hand with miles, or from odometer readings, and mark round trips in one tap.'),
 card('camera','Expenses with receipt photos','Snap or pick a receipt photo, then set the vendor, amount, category and business-use share. Meals are counted at 50%. You can link an expense to a trip.'),
 card('file','Totals by Schedule C line','Reports add up car and truck expenses, supplies, meals and more by Schedule C line, for each business and year.'),
 card('download','CSV export on any plan','Export your mileage log and expenses as CSV whenever you like, for your own records or your tax preparer.'),
 card('brief','A business for each side hustle','Each business keeps its own trips, expenses and totals. The free plan includes one business, and Pro adds more.',tag='Pro'),
 card('sync','Backup and sync','Sign in with a one-time code sent to your email, with no password, to back up your records and sync them across your devices.',tag='Pro'),
])

home=f'''<section class="hero" aria-labelledby="hero-title">
  <div class="wrap">
    <div>
      <img class="app-icon" src="/assets/img/icon-rounded.svg" alt="Deductrail app icon" width="76" height="76">
      <h1 id="hero-title">Every business mile,<br><span class="accent">on the record.</span></h1>
      <p class="lede">Deductrail tracks mileage and expenses for business deductions. Start a trip and it records the miles, even with your phone locked. Add receipts, and see your totals by Schedule C line.</p>
      <div class="chips" role="list" aria-label="Availability">
        <span class="soon" role="listitem">{I["phone"]}<span><small>Coming soon</small>iPhone</span></span>
        <span class="soon" role="listitem">{I["phone"]}<span><small>Coming soon</small>Android</span></span>
      </div>
      <p class="hero-note">Coming soon to iPhone and Android. Not in the app stores yet.<br>Screens shown are from the current Deductrail build, with sample data.</p>
    </div>
    <figure class="phones" style="margin:0">
      <div class="phone back"><img src="/assets/img/screen-trips.webp" width="640" height="1385" alt="Deductrail Trips screen for October 2026 showing 80.6 business miles, a $61.26 estimated deduction and four trips grouped by day." fetchpriority="low"></div>
      <div class="phone front"><img src="/assets/img/screen-home.webp" width="640" height="1385" alt="Deductrail Home screen showing 80.6 business miles this month, a $61.26 estimated deduction at 76 cents a mile, a Start trip button and recent trips."></div>
    </figure>
  </div>
</section>

<section id="features" aria-labelledby="features-title">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Features</p>
      <h2 id="features-title">A mileage log and expense book in your pocket</h2>
      <p>Made for people with one or more side hustles who want clean records at tax time.</p>
    </div>
    <div class="grid">
{features}    </div>
  </div>
</section>

<section class="alt" id="how" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How it works</p>
      <h2 id="how-title">Three steps from driving to deductions</h2>
    </div>
    <ol class="steps">
      <li><h3>Add your business</h3><p>Name your side hustle. Trips and expenses belong to a business, because each one files its own Schedule C.</p></li>
      <li><h3>Drive and save receipts</h3><p>Tap Start trip before you drive and hold to stop when you arrive. Mark the trip business, personal or commute, and add receipts as you spend.</p></li>
      <li><h3>Review and export</h3><p>Check your miles, estimated deduction and expenses by month or year, then export a CSV when you need it.</p></li>
    </ol>
  </div>
</section>

<section aria-labelledby="report-title">
  <div class="wrap split">
    <div class="phone-col"><div class="phone"><img src="/assets/img/screen-reports.webp" width="640" height="1385" loading="lazy" alt="Deductrail Reports screen for 2026 listing Schedule C Part II lines: line 9 car and truck expenses $61.26, line 22 supplies $64.18 and line 24b meals $19.20."></div></div>
    <div>
      <p class="eyebrow">Reports</p>
      <h2 id="report-title">See where your deduction comes from</h2>
      <p class="muted" style="margin-top:14px;font-size:19px">Reports group your year by Schedule C line, and show the miles and rate behind the car and truck total.</p>
      <ul>
        <li>{I["check"]}<span><b>Mileage at the IRS rate.</b> Each trip uses the rate in effect on its date, rounded to the cent.</span></li>
        <li>{I["check"]}<span><b>Expenses by category.</b> Supplies, meals at 50% and other categories land on their Schedule C lines.</span></li>
        <li>{I["check"]}<span><b>Yours to export.</b> CSV of your mileage log and expenses, any time.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="alt" id="privacy" aria-labelledby="privacy-title">
  <div class="wrap privacy">
    <div class="section-head" style="margin-bottom:0">
      <p class="eyebrow">Privacy</p>
      <h2 id="privacy-title">Your records stay yours</h2>
      <p>Deductrail records your location only during trips you start, keeps your route on your phone, and lets you delete everything at any time.</p>
      <p style="margin-top:18px;font-size:16px"><a href="/privacy/">Privacy policy</a> · <a href="/delete-account/">Delete your account</a></p>
    </div>
    <ul class="checks">
{check("Location only during a trip you start","Deductrail never starts a trip on its own and doesn’t ask for “Always” location access. The GPS points of your route stay on your phone. Only the trip summary syncs when you sign in.")}{check("Never sold","Your data isn’t sold and isn’t shared with advertisers or insurers.")}{check("No ads, analytics or trackers","The app has no advertising, analytics or tracking SDKs. This website has none either.")}{check("No account needed on your phone","Use Deductrail on your phone without signing in, and your records stay on the device.")}{check("Delete any time","Delete your account and data in the app, under Settings. It takes effect right away.")}    </ul>
  </div>
</section>

<section id="faq" aria-labelledby="faq-title">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">FAQ</p>
      <h2 id="faq-title">Questions</h2>
    </div>
    <div class="faq">
{faq("When can I get Deductrail?","Deductrail is coming soon to iPhone and Android. It isn’t in the App Store or Google Play yet. We’ll post the links here when it is.")}{faq("Does it detect drives automatically?","No. Deductrail records only the trips you start, so nothing is recorded by surprise. Once a trip is running, it keeps recording when you lock your phone or switch apps. On iPhone the blue location indicator stays on, and on Android a notification stays up, until you end the trip. You can also add trips by hand or from odometer readings.")}{faq("Will it drain my battery?","GPS runs only while a trip you started is recording. When no trip is running, Deductrail doesn’t use your location.")}{faq("Do I need an account?","Not on your phone. Your records stay on the device. If you want backup and sync across devices, sign in with a one-time code sent to your email. There’s no password to remember.")}{faq("Is it free?","There’s a free plan with unlimited expenses, one business and CSV export. Free reports and exports include your first 30 trips each month, and every trip is still saved. Deductrail Pro adds unlimited trips, more businesses, and backup and sync. The app shows the price before you buy.")}{faq("What mileage rate does Deductrail use?","The IRS standard mileage rate for business, based on the date of each trip. For 2026 that’s 72.5¢ a mile from January 1 to June 30 and 76¢ a mile from July 1 to December 31.")}{faq("Is Deductrail tax advice?","No. Deductrail helps you keep mileage and expense records and estimates your deduction. Check with a tax professional about your situation.")}{faq("How do I delete my account?","In the app, go to Settings, then Delete account and data. You can also email privacy@deductrail.com. See <a href=\"/delete-account/\">Delete your account</a> for details.")}    </div>
  </div>
</section>

<section id="contact" aria-labelledby="contact-title" style="padding-top:24px">
  <div class="wrap">
    <div class="contact">
      <div>
        <h2 id="contact-title">Questions or feedback?</h2>
        <p>Email us any time. We’d love to hear from you.</p>
      </div>
      <a class="btn light" href="mailto:support@deductrail.com">{I["mail"]}support@deductrail.com</a>
    </div>
  </div>
</section>
'''
page('/','Deductrail: mileage and expense tracking for business deductions','Deductrail tracks your business mileage and expenses, with receipt photos, IRS standard rates and Schedule C totals. Coming soon to iPhone and Android.',home)

delete=f'''<article class="doc">
  <div class="wrap">
    <p class="eyebrow">Account</p>
    <h1>Delete your Deductrail account</h1>
    <p class="lede">This page explains how to delete your account and data in <strong>Deductrail</strong>, the mileage and expense tracking app from <strong>Wade Works LLC</strong>.</p>

    <h2>Option 1: Delete in the app</h2>
    <div class="panel">
      <ol>
        <li>Open Deductrail and sign in to the account you want to delete.</li>
        <li>Tap the <strong>Settings</strong> tab.</li>
        <li>Under <strong>Your data</strong>, tap <strong>Delete account and data</strong>.</li>
        <li>Type <kbd>DELETE</kbd> to confirm.</li>
        <li>Tap <strong>Delete account and data</strong>.</li>
      </ol>
      <p class="path" aria-label="Path: Settings, Your data, Delete account and data"><b>Settings</b><i>›</i><b>Your data</b><i>›</i><b>Delete account and data</b></p>
    </div>
    <p style="margin-top:16px">If you want a copy of your data, export it first: Settings › Your data › <strong>Export all data (CSV)</strong>.</p>
    <p>If you use Deductrail without signing in, your data is stored only on your device, and the same steps erase it from that device.</p>

    <h2>Option 2: Ask us by email</h2>
    <p>Email <a href="mailto:privacy@deductrail.com?subject=Delete%20my%20account">privacy@deductrail.com</a> from the email address on your Deductrail account, with the subject <strong>Delete my account</strong>. We use that address to find your account.</p>

    <h2>What is deleted, and when</h2>
    <p>Deleting your account removes, immediately and permanently:</p>
    <ul>
      <li>your account</li>
      <li>your trips</li>
      <li>your expenses</li>
      <li>your businesses</li>
      <li>your receipts, including receipt photos</li>
    </ul>
    <p>This removes the data from our servers and from the device you delete from. It can’t be undone.</p>
    <p>If you delete an individual trip, expense, or business without deleting your account, it is kept on our servers for 30 days so your other devices can sync the change, and then it is permanently purged. A receipt photo is removed as soon as its expense is deleted.</p>

    <h2>What is kept</h2>
    <p>After your account is deleted, we keep none of your account data, except as our <a href="/privacy/">privacy policy</a> states.</p>

    <h2>Subscriptions</h2>
    <p>Deleting your account doesn’t cancel a Deductrail Pro subscription. Cancel it in your App Store or Google Play subscriptions.</p>

    <h2>Questions</h2>
    <p>Email <a href="mailto:privacy@deductrail.com">privacy@deductrail.com</a>.</p>
  </div>
</article>
'''
page('/delete-account/','Delete your Deductrail account','How to delete your Deductrail account and data, what is deleted, and when.',delete)

priv='''<article class="doc">
  <div class="wrap">
    <p class="eyebrow">Legal</p>
    <h1>Privacy policy</h1>
    <div class="panel">
      <p>Our privacy policy will be posted here before launch.</p>
      <p>Questions in the meantime: <a href="mailto:privacy@deductrail.com">privacy@deductrail.com</a></p>
    </div>
  </div>
</article>
'''
page('/privacy/','Deductrail privacy policy','Deductrail privacy policy.',priv)

nf='''<section class="notfound" aria-labelledby="nf-title">
  <div class="wrap">
    <p class="code">404</p>
    <h1 id="nf-title">This page took a wrong turn</h1>
    <p>We couldn’t find that page.</p>
    <a class="btn primary" href="/">Back to Deductrail</a>
  </div>
</section>
'''
page('404.html','Page not found · Deductrail','That page could not be found.',nf,canon='/',noindex=True)
print('built')
