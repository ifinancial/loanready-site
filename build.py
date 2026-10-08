#!/usr/bin/env python3
"""Builds the Loan Ready powered by iFinancial static site into ./site"""
import json, os, datetime

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
DOMAIN = "https://loanready.goifinancial.com"   # change if you host elsewhere
PHONE = "772-262-5435"
TEL = "+17722625435"
BOOK = "https://calendar.app.google/Z1xuxt37AZk3eRVm7"
BOOK_A = f'href="{BOOK}" target="_blank" rel="noopener"'
EMAIL = "info@goifinancial.com"
STREET = "751 Northlake Blvd, Suite 2D"
CITY, STATE, ZIP = "North Palm Beach", "FL", "33408"
ADDR_ONE = f"{STREET}, {CITY}, {STATE} {ZIP}"
HOURS = "Mon–Fri 9:00 am – 5:30 pm"
MAPQ = "751+Northlake+Blvd+Suite+2D,+North+Palm+Beach,+FL+33408"
TODAY = datetime.date.today().isoformat()

PAGES = []  # (path, priority)
import hashlib
CSS_V = hashlib.md5(open(os.path.join(ROOT, "assets", "site.css"), "rb").read()).hexdigest()[:8]
LANG = "en"
CURRENT = "/"
# English path -> Spanish path (drives hreflang + the language switch)
ES_MAP = {
    "/": "/es/",
    "/credit-repair/": "/es/reparacion-de-credito/",
    "/express-credit-repair/": "/es/reparacion-express/",
    "/bookkeeping-tax-planning/": "/es/contabilidad-e-impuestos/",
    "/get-out-of-mca/": "/es/salir-de-mca/",
    "/lending-has-changed/": "/es/como-cambiaron-los-prestamos/",
    "/bankable-check/": "/es/soy-bancable/",
    "/free-loan-score/": "/es/evaluacion-gratis/",
    "/get-loan-ready/": "/es/prestamos/",
    "/contact/": "/es/contacto/",
    "/loan-calculator/": "/es/calculadora/",
    "/your-rights/": "/es/sus-derechos/",
    "/thank-you/": "/es/gracias/",
}
EN_MAP = {v: k for k, v in ES_MAP.items()}

# ---------------------------------------------------------------- data
PRODUCTS = [
    {
        "slug": "credit-repair", "name": "Credit Repair Program", "short": "Credit Repair",
        "price": "$250", "per": "/month",
        "note": "Billed after each month's work is done. Cancel anytime.",
        "blurb": "Monthly dispute rounds on all three bureaus, a written plan, and a progress report every cycle.",
        "points": ["Full 3-bureau review in our office", "Disputes on inaccurate, outdated and unverifiable items",
                   "Inquiry and personal-info cleanup", "Utilization and new-credit coaching", "Progress report every round"],
    },
    {
        "slug": "express-credit-repair", "name": "Express Repair", "short": "Express Repair",
        "price": "$1,500", "per": "", "extra": "+ $300 per deleted item",
        "note": "Rounds typically run 15–30 days. Billed after the work is done. The $300 applies only to items actually deleted.",
        "offer": "We fund your deal? Your $1,500 comes back.",
        "blurb": "For owners with a loan on the table. A concentrated round aimed at the items blocking the approval.",
        "points": ["Priority file — worked first", "Targeted at the items a lender flagged",
                   "You pay per deletion, not per letter", "Post-round report on all three bureaus", "Hand-off to iFinancial funding when ready"],
        "feature": True,
    },
    {
        "slug": "bookkeeping-tax-planning", "name": "Bookkeeping & Tax Planning", "short": "Bookkeeping & Tax",
        "price": "$500", "per": "/month",
        "note": "Businesses with $500K–$1M in revenue. $1M–$3M: $1,000/month.",
        "blurb": "Lender-ready books and a tax plan that shows the income you actually earn — the two things underwriters ask for first.",
        "points": ["Monthly bookkeeping and reconciliations", "P&L and balance sheet a bank will accept",
                   "Tax planning through the year, not just in April", "Debt-service coverage tracking", "Document package for your loan file"],
    },
]

LOANS = [
    ("sba-loans", "SBA Loans", "7(a), 504 and SBA Express",
     "SBA loans have the longest terms and some of the lowest rates small businesses can get. They also have the most paperwork, and they're where a lot of owners get turned down.",
     ["Personal credit for every owner with 20% or more of the business", "Two to three years of business and personal tax returns",
      "Cash flow that covers the new payment with room to spare (debt service coverage)", "Year-to-date P&L and balance sheet",
      "Any past government debt, defaults, or open tax liens", "A clear use of funds"],
     ["Tax returns that show too little income because every expense was written off", "Late payments or collections on one owner's personal report",
      "Books that don't match the tax returns", "Missing interim financials"],
     "We clean up the personal credit side, rebuild the books so they tie to your returns, and our in-house CPA and tax team make sure next year's return shows the income a lender needs to see. When the file is ready, iFinancial takes it to SBA lenders who match your profile."),
    ("equipment-financing", "Equipment Financing", "Trucks, machines, medical and restaurant equipment",
     "The equipment itself is the collateral, so approvals can be easier than an unsecured loan. Your rate still depends heavily on your credit and time in business.",
     ["Personal credit score and recent payment history", "Time in business", "Bank statements (often the last 3–6 months)",
      "The equipment quote or invoice", "Down payment ability"],
     ["A recent late payment that drops a score just below a lender's tier", "Too many recent inquiries from shopping around",
      "High card balances pulling the score down"],
     "Equipment rates move in tiers, so a few points can mean a better rate. We focus on the fastest wins first: inquiries, utilization, and inaccurate late payments. Then iFinancial shops the deal with one clean submission instead of ten hard pulls."),
    ("business-line-of-credit", "Business Line of Credit", "Revolving working capital",
     "A line of credit gives you cash to draw on when you need it. Banks treat it as unsecured risk, so they look closely at credit and cash flow.",
     ["Personal and business credit profiles", "Average daily bank balance and deposit consistency",
      "Revenue trend over 6–24 months", "Existing debt and merchant cash advances"],
     ["Stacked merchant cash advances that make the bank statements look stressed", "NSFs and negative-balance days",
      "Thin or no business credit file"],
     "We help you clean up the bank-statement story, separate business and personal spending, build the business credit file, and fix the personal report. That's what moves you from expensive short-term money to a real line."),
    ("term-loans", "Business Term Loans", "Fixed amount, fixed payment",
     "A term loan is a lump sum paid back over a set schedule. It's used for expansion, refinancing expensive debt, or buying inventory.",
     ["Credit score and history of all owners", "Annual revenue and profitability", "Time in business",
      "Existing debt load", "Tax returns and financial statements for larger amounts"],
     ["Profit on paper that doesn't support the payment", "Personal credit dragged down by old collections",
      "No financial statements beyond bank statements"],
     "We build the financials, fix the credit, and show you the debt-service math before a lender sees it. That way you apply for an amount you'll actually get approved for."),
    ("commercial-real-estate", "Commercial Real Estate Loans", "Buy, refinance, or build",
     "Owner-occupied and investment property loans depend on the property and on you. Lenders want strong credit and documented income for every guarantor.",
     ["Guarantor credit and liquidity (cash reserves)", "Property income or business cash flow covering the mortgage",
      "Down payment source", "Tax returns and a personal financial statement", "Experience with similar properties"],
     ["Reserves that aren't documented", "A personal financial statement that doesn't match the credit report",
      "Derogatory items on one guarantor's report"],
     "We get every guarantor's credit report clean, build a personal financial statement that ties out, and organize the documents a commercial underwriter will request. iFinancial then places the deal with bank, SBA 504, DSCR or bridge lenders."),
    ("asset-based-lending", "Asset-Based Lending", "Borrow against receivables, inventory or equipment",
     "Asset-based loans are sized off what your business owns: receivables, inventory, or equipment. Strong assets help, but the reporting has to be clean.",
     ["Accounts receivable aging reports", "Inventory reports and valuation", "Clean, current monthly financials",
      "Customer concentration", "Owner credit as a secondary check"],
     ["AR aging that's out of date or doesn't tie to the books", "Inventory with no tracking", "Monthly closes that run months behind"],
     "This is where bookkeeping matters most. We get your AR aging, inventory and monthly financials current and consistent, so a lender can actually lend against them."),
    ("same-day-funding", "Same-Day & Short-Term Funding", "When you need capital this week",
     "Fast funding exists, and iFinancial can arrange it. It also costs more. We'll help you use it as a bridge, not a habit.",
     ["Recent bank statements", "Consistent monthly deposits", "Existing advances or daily payments", "Time in business"],
     ["Taking a second or third advance to cover the first", "Daily payments squeezing cash flow", "Never building toward bank financing"],
     "If you need money now, iFinancial can fund fast. At the same time, we start the Loan Ready work so your next round of financing is cheaper. The goal is to refinance out of short-term money, not stack more of it."),
    ("home-mortgage", "Home Mortgages", "Buying or refinancing a home",
     "Mortgage pricing is tied to your middle credit score. A small move up can change your rate tier, and that difference adds up over 30 years.",
     ["Middle score of the three bureaus", "Debt-to-income ratio", "Two years of income history (tax returns if self-employed)",
      "Down payment and reserves", "Recent late payments and collections"],
     ["Self-employed income that's too low on paper after write-offs", "One bureau far lower than the other two",
      "Maxed-out cards right before the application"],
     "We work all three bureaus to raise your middle score and coach utilization timing before the lender pulls credit. For business owners, our tax planning makes sure your income actually qualifies. When you're ready, iFinancial connects you with a mortgage lender who fits your situation."),
]

AREAS = [
    ("palm-beach-gardens", "Palm Beach Gardens",
     "Palm Beach Gardens is minutes west of our office on Northlake Blvd. A lot of our clients run medical practices, contractors, restaurants and professional-service firms along PGA Blvd and Northlake. Most of them come in after a bank asks for documents they don't have ready.",
     "Head east on Northlake Blvd toward US-1. We're in Suite 2D at 751 Northlake Blvd, North Palm Beach."),
    ("jupiter", "Jupiter",
     "Jupiter owners — marine, construction, hospitality, and home services — often have strong revenue but books and credit that don't show it. We'll meet you in our North Palm Beach office or by video, whichever is easier.",
     "Take US-1 or I-95 south to Northlake Blvd and head east. We're at 751 Northlake Blvd, Suite 2D."),
    ("west-palm-beach", "West Palm Beach",
     "From downtown West Palm to the Northwood and Palm Beach Lakes areas, we help owners and families get ready for SBA, equipment, real estate and mortgage financing. Getting here is an easy drive north.",
     "Take I-95 north to the Northlake Blvd exit and head east, or take US-1 north. We're at 751 Northlake Blvd, Suite 2D."),
    ("riviera-beach-lake-park", "Riviera Beach & Lake Park",
     "Riviera Beach and Lake Park are our closest neighbors. Many clients here are trades, logistics, and marine businesses near the port, plus families getting ready to buy a home. If you're nearby, stop by and we'll go over your report in person.",
     "Head north on US-1 or Congress Ave to Northlake Blvd. We're at 751 Northlake Blvd, Suite 2D, North Palm Beach."),
    ("juno-beach-tequesta", "Juno Beach & Tequesta",
     "Juno Beach and Tequesta are a short drive up the road. We work with a lot of owners here who run restaurants, salons, marine and home-service companies, and with families getting ready to buy or refinance. Many have strong income on paper problems: the business makes money, but the tax returns and credit report don't show it. That's exactly the gap we close.",
     "Take US-1 or I-95 south to Northlake Blvd and follow it to 751 Northlake Blvd, Suite 2D, North Palm Beach."),
    ("stuart", "Stuart & Martin County",
     "Our phone number starts with 772 for a reason: we serve Stuart, Palm City, Jensen Beach and the rest of Martin County. Owners here are often a step away from bank financing, with a solid business held back by a credit report, a stack of advances, or books that are a year behind. Meet us by video, or make the drive south when it's time to sign.",
     "Take I-95 south to the Northlake Blvd exit and follow Northlake to 751 Northlake Blvd, Suite 2D, North Palm Beach. Phone and video appointments are available too."),
    ("port-st-lucie", "Port St. Lucie",
     "Port St. Lucie is one of the fastest-growing cities in Florida, and growth takes capital. We help PSL contractors, trucking and logistics companies, medical practices and new franchise owners get bankable: credit repaired, books current, taxes planned for the loan, and the right lender lined up. Most of our Treasure Coast clients work with us by phone and video.",
     "Take I-95 south to the Northlake Blvd exit and follow Northlake to 751 Northlake Blvd, Suite 2D, North Palm Beach. Most Port St. Lucie clients meet with us by video."),
    ("wellington-royal-palm-beach", "Wellington & Royal Palm Beach",
     "Wellington and Royal Palm Beach owners, from equestrian and agricultural businesses to medical, retail and home services, come to us when a bank asks for documents they don't have ready, or when short-term funding has started to squeeze cash flow. We'll get your file bank-ready and line up the right lender.",
     "Take Southern Blvd or Okeechobee Blvd east to I-95, then north to the Northlake Blvd exit. We're at 751 Northlake Blvd, Suite 2D, North Palm Beach."),
]

RESULTS = [
    ("P.C.", "Jan → Mar 2026", [("Equifax", 718, 820), ("Experian", 704, 805), ("TransUnion", 661, 811)],
     "Inquiries removed and an account updated to positive. All three scores now above 800."),
    ("J.D.", "Jun → Sep 2025", [("Equifax", 673, 765), ("Experian", 630, 719), ("TransUnion", 643, 710)],
     "21 disputed items deleted across bureaus, including inquiries and an account."),
    ("S.M.", "Feb → Aug 2025", [("Equifax", 505, 719), ("Experian", 514, 624), ("TransUnion", 688, 719)],
     "Collection accounts deleted. Card balances are still the next thing to fix."),
    ("C.G.", "May → Jul 2025", [("Experian", 529, 671), ("TransUnion", 515, 664)],
     "Student loan and Sallie Mae items deleted on two bureaus in one round."),
]

FAQS = [
    ("Can you get me out of my merchant cash advances?",
     "Often, yes. It takes a plan, not another advance. We stop the stacking, clean up your bank statements, books and credit, and then move you into a longer-term line, term loan, or SBA loan when your file supports it. How fast depends on your cash flow and how many positions you have open."),
    ("Will applying with a lot of lenders hurt me?",
     "It can. Every hard inquiry shows up, and lenders can see who else you applied with. Business loan inquiries generally don't get the rate-shopping protection mortgages and auto loans get. That's why we submit strategically: the right lender, at the right time, with a complete file."),
    ("Can you guarantee my score will go up or that I'll get approved?",
     "No, and no honest company can. The law lets you dispute information that's inaccurate, outdated or can't be verified. Accurate, timely information can stay on your report. What we can promise is a clear plan, real work every cycle, and an honest read on when you're ready to apply."),
    ("When do I pay?",
     "After the work is done. The monthly program is billed after each month's dispute round is completed. Express Repair is billed after the round, and the $300 per-item fee applies only to items that are actually deleted."),
    ("How long does it take?",
     "Express rounds typically run 15–30 days. The monthly program usually runs several months, depending on how many items are on your reports and how the bureaus respond. We'll give you a realistic timeline after we review your reports."),
    ("Do I have to come into the office?",
     "No, but you're welcome to. We're at 751 Northlake Blvd, Suite 2D in North Palm Beach, open Monday through Friday, 9:00 to 5:30. We can also meet by phone or video."),
    ("What happens when I'm loan ready?",
     "iFinancial takes your file to lenders that match your profile: SBA, banks, equipment lenders, asset-based lenders, real estate lenders and short-term funders. You get one organized submission instead of applying everywhere and piling up inquiries."),
    ("Is this for business owners or individuals?",
     "Both. Most small-business loans depend on the owner's personal credit, so we usually start there. We also help individuals get ready for a mortgage, auto loan or personal financing."),
]

for _f in ('blog_posts_1.py', 'blog_posts_2.py', 'blog_posts_3.py'):
    exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), _f)).read())

# ---------------------------------------------------------------- helpers
def nav():
    return f"""
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span>{STREET}, {CITY} <span class="hide-sm">· {HOURS}</span></span>
  <span><a href="{ES_MAP.get(CURRENT, '/es/')}" hreflang="es" lang="es">Español</a> <span class="sep">·</span> <a {BOOK_A}>Book a call</a> <span class="sep">·</span> <a href="tel:{TEL}">Call {PHONE}</a></span>
</div></div>
<header class="site-head"><div class="wrap">
  <a class="brand" href="/" aria-label="Loan Ready powered by iFinancial — home">
    <img src="/assets/ifinancial-logo.png" alt="iFinancial" width="262" height="160">
    <span class="lock"><span class="lr">LOAN READY</span><span class="pb">powered by iFinancial</span></span>
  </a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">
    <a href="/credit-repair/">Credit Repair</a>
    <a href="/bookkeeping-tax-planning/">Tax &amp; Books</a>
    <a href="/get-out-of-mca/">Get Out of MCAs</a>
    <a href="/get-loan-ready/">Loan Types</a>
    <a href="/loan-calculator/">Calculator</a>
    <a href="/blog/">Guides</a>
    <a href="/results/">Results</a>
    <a href="/contact/">Visit Us</a>
    <a class="btn btn-gold btn-sm" href="/bankable-check/">Am I Bankable?</a>
  </nav>
</div></header>"""

def footer():
    loans = "".join(f'<li><a href="/get-loan-ready/{s}/">{n}</a></li>' for s, n, *_ in LOANS[:6])
    areas = "".join(f'<li><a href="/areas/{s}/">{n}</a></li>' for s, n, *_ in AREAS)
    return f"""
<footer class="site-foot"><div class="wrap">
  <div class="cols">
    <div class="nap">
      <div class="foot-logo"><img src="/assets/ifinancial-logo.png" alt="iFinancial" width="66" height="40"></div>
      <p><b>Loan Ready powered by iFinancial</b><br>{STREET}<br>{CITY}, {STATE} {ZIP}</p>
      <p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{HOURS}</p>
    </div>
    <div><h4>Services</h4><ul>
      <li><a href="/credit-repair/">Credit Repair Program</a></li>
      <li><a href="/express-credit-repair/">Express Repair</a></li>
      <li><a href="/bookkeeping-tax-planning/">Bookkeeping &amp; Tax Planning</a></li>
      <li><a href="/free-loan-score/">Free Loan Score</a></li>
      <li><a href="/bankable-check/">60-Second Bankable Check</a></li>
      <li><a href="/get-out-of-mca/">Get Out of MCAs</a></li>
      <li><a href="/lending-has-changed/">How Lending Has Changed</a></li>
      <li><a href="/loan-calculator/">Loan Calculator</a></li>
      <li><a href="/grow-your-business/">Grow Your Business</a></li>
      <li><a href="/blog/">Guides &amp; Articles</a></li>
      <li><a href="/results/">Client Results</a></li>
    </ul></div>
    <div><h4>Get Ready For</h4><ul>{loans}<li><a href="/get-loan-ready/">All loan types</a></li></ul></div>
    <div><h4>Areas We Serve</h4><ul><li><a href="/">North Palm Beach</a></li>{areas}</ul></div>
  </div>
  <div class="legal">
    <p>Loan Ready is a program of iFinancial (formerly Finance Solutions Group). We do not guarantee any specific credit score increase, deletion, or loan approval. Accurate and timely information cannot be removed from a credit report. You have the right to dispute inaccurate information directly with the credit bureaus at no cost. Funding is subject to lender approval. Individual results vary.</p>
    <p><a href="/your-rights/">Your Rights &amp; Disclosures</a> · <a href="/privacy-policy/">Privacy Policy</a> · <a href="https://goifinancial.com">goifinancial.com</a> · © {datetime.date.today().year} iFinancial</p>
  </div>
</div></footer>
<div class="callbar"><a class="c1" href="tel:{TEL}">Call</a><a class="c3" {BOOK_A}>Book a Call</a><a class="c2" href="/free-loan-score/">Loan Score</a></div>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
if(b){{b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);}});}}}})();
</script>"""

def local_business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "FinancialService",
        "@id": DOMAIN + "/#business",
        "name": "Loan Ready powered by iFinancial",
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/assets/ifinancial-logo.png",
        "image": DOMAIN + "/assets/ifinancial-logo.png",
        "telephone": "+1-" + PHONE,
        "email": EMAIL,
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
                    "addressRegion": STATE, "postalCode": ZIP, "addressCountry": "US"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00", "closes": "17:30"}],
        "areaServed": ["North Palm Beach", "Palm Beach Gardens", "Jupiter", "West Palm Beach", "Riviera Beach",
                       "Lake Park", "Juno Beach", "Tequesta", "Palm Beach County"],
        "parentOrganization": {"@type": "Organization", "name": "iFinancial", "alternateName": "Finance Solutions Group", "url": "https://goifinancial.com"},
        "alternateName": ["Loan Ready", "Loan Ready by iFinancial"],
        "knowsAbout": ["Credit repair", "Business loans", "SBA loans", "Merchant cash advance refinancing", "Small business bookkeeping", "Tax planning", "Business credit"],
        "hasMap": "https://www.google.com/maps/search/?api=1&query=751+Northlake+Blvd+Suite+2D+North+Palm+Beach+FL+33408",
        "sameAs": ["https://goifinancial.com"],
    }

def page(path, title, desc, body, schema=None, priority="0.7", noindex=False):
    global CURRENT
    CURRENT = path
    url = DOMAIN + path
    en_p = path if LANG == "en" else EN_MAP.get(path)
    es_p = ES_MAP.get(path) if LANG == "en" else path
    alts = ""
    if en_p and es_p and not noindex:
        alts = (f'<link rel="alternate" hreflang="en" href="{DOMAIN}{en_p}">\n'
                f'<link rel="alternate" hreflang="es" href="{DOMAIN}{es_p}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{en_p}">')
    schemas = [local_business_schema()] + (schema or [])
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    html = f"""<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{alts}
{robots}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/og-loan-ready.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Loan Ready by iFinancial">
<meta property="og:locale" content="{'es_US' if LANG == 'es' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="North Palm Beach">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">
{ld}
</head>
<body>
{nav()}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    if path.endswith(".html"):
        out = os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)
    if not noindex:
        PAGES.append((path, priority))

def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + p}
                                for i, (n, p) in enumerate(items)]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def page_hero(crumbs, h1, lede, eyebrow=None, book_first=False):
    c = " / ".join([f'<a href="{p}">{n}</a>' for n, p in crumbs[:-1]] + [crumbs[-1][0]])
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    if book_first:
        btns = f'<div class="btn-row"><a class="btn btn-gold" {BOOK_A}>Book My Call Now</a><a class="btn btn-line" href="tel:{TEL}">Call {PHONE}</a></div>'
    else:
        btns = f'<div class="btn-row"><a class="btn btn-gold" href="/free-loan-score/">Get My Free Loan Score</a><a class="btn btn-line" {BOOK_A}>Book a Call Now</a><a class="btn btn-call" href="tel:{TEL}">or call {PHONE}</a></div>'
    return f"""<section class="hero page-hero on-dark"><div class="wrap"><div>
<div class="crumbs">{c}</div>{eb}
<h1>{h1}</h1><p class="lede">{lede}</p>
{btns}
</div></div><span class="tri" aria-hidden="true"></span></section>"""

def product_cards():
    out = []
    for p in PRODUCTS:
        feat = " feature" if p.get("feature") else ""
        tag = '<span class="tag">Loan on the table</span>' if p.get("feature") else ""
        pts = "".join(f"<li>{x}</li>" for x in p["points"])
        out.append(f"""<div class="product{feat}">{tag}
<h3>{p['name']}</h3><p>{p['blurb']}</p>
<div class="price">{p['price']}<small>{p['per']}</small></div>{'<div class="price-extra">'+p['extra']+'</div>' if p.get('extra') else ''}
<div class="price-note">{p['note']}</div>{'<div class="offer-pill">'+p['offer']+'</div>' if p.get('offer') else ''}
<ul class="checks">{pts}</ul>
<a class="btn btn-navy" href="/{p['slug']}/">See how it works</a></div>""")
    return '<div class="grid-3">' + "".join(out) + "</div>"

def loan_tiles(limit=None):
    items = LOANS if not limit else LOANS[:limit]
    return '<div class="grid-4">' + "".join(
        f'<a class="loan-tile" href="/get-loan-ready/{s}/"><h3>{n}</h3><p>{sub}</p><span class="go">What lenders check →</span></a>'
        for s, n, sub, *_ in items) + "</div>"

def result_cards(n=None):
    out = []
    for who, when, rows, note in (RESULTS if not n else RESULTS[:n]):
        r = "".join(f'<div class="bureau"><span class="b">{b}</span><span class="s"><span>{a} →</span> {z}</span><span class="d">+{z-a}</span></div>' for b, a, z in rows)
        out.append(f'<div class="result"><div class="who">Client {who}<small>{when}</small></div>{r}<p class="note">{note}</p></div>')
    cls = "grid-2 results-2" if not n or n >= 4 else "grid-3"
    return f'<div class="{cls}">' + "".join(out) + "</div>"

def payment(p, rate, n):
    r = rate / 12
    return p * r / (1 - (1 + r) ** -n)

def cost_block():
    P, N = 50000, 60
    lo, hi = 0.09, 0.19
    pg, pb = payment(P, lo, N), payment(P, hi, N)
    ig, ib = pg * N - P, pb * N - P
    return f"""<div class="cost">
<div class="cost-box bad"><div class="eyebrow">Credit &amp; books not ready</div><div class="big">${pb:,.0f}/mo</div>
<dl><dt>Loan</dt><dd>$50,000 · 5 yrs</dd><dt>Example rate</dt><dd>19%</dd><dt>Total interest</dt><dd>${ib:,.0f}</dd></dl></div>
<div class="cost-box good"><div class="eyebrow">Loan ready</div><div class="big">${pg:,.0f}/mo</div>
<dl><dt>Loan</dt><dd>$50,000 · 5 yrs</dd><dt>Example rate</dt><dd>9%</dd><dt>Total interest</dt><dd>${ig:,.0f}</dd></dl></div>
<div class="cost-diff"><span>Same loan, same business. The difference is the file you walk in with.</span><b>${ib-ig:,.0f} saved</b></div>
</div><p class="fineprint" style="margin-top:12px">Illustrative example only. Actual rates depend on the lender, loan type, and your full financial profile.</p>"""

def faq_block(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs) + "</div>"

def visit_block():
    return f"""<section class="alt"><div class="wrap grid-2">
<div><div class="eyebrow">Visit the office</div><h2>Sit down with us on Northlake Blvd.</h2>
<p>Bring your questions, or just bring your phone. We'll pull your reports together and walk through every item with you. Prefer not to drive? We do phone and video appointments too.</p>
<div class="visit-card"><dl>
<dt>Address</dt><dd>{STREET}<br>{CITY}, {STATE} {ZIP}</dd>
<dt>Hours</dt><dd>{HOURS}</dd>
<dt>Phone</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd>
<dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
</dl><div class="btn-row" style="margin-top:20px"><a class="btn btn-navy" href="https://www.google.com/maps/dir/?api=1&destination={MAPQ}" target="_blank" rel="noopener">Get Directions</a><a class="btn btn-gold" {BOOK_A}>Book a Call or Visit</a></div></div></div>
<iframe class="map" title="Map to Loan Ready, {ADDR_ONE}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={MAPQ}&output=embed"></iframe>
</div></section>"""

def band(h, p):
    return f"""<section class="band on-dark"><div class="wrap"><div><h2>{h}</h2><p>{p}</p></div>
<div class="btn-row"><a class="btn btn-gold" href="/bankable-check/">Am I Bankable?</a><a class="btn btn-line" {BOOK_A}>Book a Call Now</a><a class="btn btn-call" href="tel:{TEL}">or call {PHONE}</a></div></div></section>"""

def sidebar(current=None):
    others = "".join(f'<li><a href="/get-loan-ready/{s}/">{n}</a></li>' for s, n, *_ in LOANS if s != current)
    return f"""<aside class="sidebar">
<div class="side-box side-dark"><h3>Not sure where you stand?</h3><p>Get a free Loan Score. We'll review your credit, books and tax situation against what lenders require.</p>
<a class="btn btn-gold" style="width:100%" href="/free-loan-score/">Start My Loan Score</a>
<a class="btn btn-line" style="width:100%;margin-top:10px" {BOOK_A}>Book a Call Now</a>
<p style="margin:14px 0 0;font-size:.92rem">Or call <a style="color:#fff" href="tel:{TEL}">{PHONE}</a></p></div>
<div class="side-box"><h3>Guides</h3><ul>{"".join(f'<li><a href="/blog/{p["slug"]}/">{p["tag"]}: {p["h1"][0].upper() + p["h1"][1:]}</a></li>' for p in BLOG[:6])}</ul></div>
<div class="side-box"><h3>Get ready for</h3><ul>{others}</ul></div>
</aside>"""



STATS = [("$50M+", "funded for our clients"), ("200+", "clients served"), ("5 yrs", "getting owners funded"),
         ("In-house", "accountants, CPA & bookkeepers")]

def stats_block(stats=None, dark=False):
    st = stats or STATS
    cls = "stats dark" if dark else "stats"
    return f'<div class="{cls}">' + "".join(f'<div class="stat"><b>{n}</b><span>{l}</span></div>' for n, l in st) + "</div>"

CASES = [
    ("Ragtop", "6 loans in 6 months",
     "Buried in MCAs and high-interest debt, with daily payments eating cash flow.",
     ["6 loans over 6 months", "Every MCA paid off", "Opened a new division now doing $2M+ a year"]),
    ("DMLPA", "From MCAs to 3 credit lines",
     "High-interest credit cards, MCA debt and other business debt holding the credit profile down.",
     ["Credit profile repaired", "High-interest cards and MCA debt paid off", "3 business lines of credit open", "Working on a 10-year SBA loan"]),
    ("Burning Hearts Tattoo", "2 MCAs paid off early",
     "Two merchant cash advances and a credit profile that kept them out of bank money.",
     ["Credit repair completed", "Both MCAs paid off early", "Saved on the interest payback"]),
]

def cases_block(cases=None, labels=("Before", "After")):
    out = []
    for name, head, before, after in (cases or CASES):
        a = "".join(f"<li>{x}</li>" for x in after)
        out.append(f"""<article class="case"><div class="case-top"><span class="case-name">{name}</span><h3>{head}</h3></div>
<div class="case-before"><span class="lbl">{labels[0]}</span><p>{before}</p></div>
<div class="case-after"><span class="lbl">{labels[1]}</span><ul>{a}</ul></div></article>""")
    return '<div class="grid-3 cases">' + "".join(out) + "</div>"

def offer_strip(h="Get funded, get your $1,500 back.",
                p="Start with Express Repair. If iFinancial funds your deal, we refund your $1,500 Express program fee. Terms are spelled out in your agreement.",
                cta="Book a Call Now"):
    return f"""<div class="offer"><div class="offer-badge">$1,500<small>back</small></div><div><h3>{h}</h3><p>{p}</p></div>
<a class="btn btn-gold" {BOOK_A}>{cta}</a></div>"""

LANDSCAPE = [
    ("Lenders see who else you applied with.",
     "Every hard inquiry shows on your personal and business credit. Cash advances leave UCC filings. Your bank statements show every payment to another lender. In the short-term world, funders share data with each other. Spray applications around and the next lender sees all of it."),
    ("Where and when you submit matters.",
     "Apply the week after a bad deposit month, before your taxes are filed, or with five lenders at once, and you can get declined by people who would have said yes a month later. Business loan inquiries generally don't get the rate-shopping protection that mortgages and auto loans do."),
    ("MCAs are getting stricter.",
     "What we're seeing: many advance funders now look for credit in the 620s and up, more documents, and tighter rules on stacking. That's how banks used to underwrite. If MCA money is getting harder to get, bank money is out of reach without a plan."),
    ("Taxes and borrowing power pull against each other.",
     "Write off everything and you save on taxes, but your return shows a business that can't afford a loan. Proper tax planning finds the balance. You keep more from Uncle Sam and still show the income a lender needs to see."),
]

def landscape_cards():
    return '<div class="grid-2 land">' + "".join(
        f'<div class="land-card"><span class="land-n">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>'
        for i, (h, p) in enumerate(LANDSCAPE)) + "</div>"

def ladder_block():
    rungs = [
        ("Today", "Bridge or restructure", "A bridge loan, or restructuring your current debt without a default, if you need relief now."),
        ("Months 1–3", "Fix the footprint", "Credit profile, books, bank statements, and tax plan. No more stacking."),
        ("Months 3–6", "Lines & term loans", "Lower-cost lines of credit and term loans that pay off the expensive money."),
        ("Months 6–12", "Bank & SBA", "Long-term bank and SBA financing. Then the next round, and the one after that."),
    ]
    return '<div class="ladder">' + "".join(
        f'<div class="rung"><span class="when">{w}</span><h3>{h}</h3><p>{p}</p></div>' for w, h, p in rungs) + "</div>"

REVIEWS = [
    ("He guided me through the SBA process to secure crucial funding for my business when no one else could.", "Peter C.", "CFO"),
    ("They fixed my credit, got me funding, and made me feel like I made friends.", "Alex A.", "Finance executive"),
    ("They were able to get my credit from a 600 to over 700 and was able to secure me financing at low rates for my business.", "Coco R.", "Business owner"),
]

def reviews_block():
    return '<div class="grid-3">' + "".join(
        f'<figure class="review"><div class="stars" aria-label="5 stars">★★★★★</div><blockquote>“{q}”</blockquote><figcaption><b>{n}</b> · {r}</figcaption></figure>'
        for q, n, r in REVIEWS) + "</div>"

def check_teaser(dark=False):
    return f"""<div class="teaser"><div><div class="eyebrow">Free · 60 seconds</div><h3>Are you bankable right now?</h3>
<p>Answer 8 quick questions. You'll see how a bank would read your file, and exactly what's holding you back.</p></div>
<a class="btn btn-gold" href="/bankable-check/">Take the Bankable Check</a></div>"""

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'calc.py')).read())

# ---------------------------------------------------------------- HOME
home = f"""
<section class="hero on-dark"><div class="wrap">
<div>
<div class="eyebrow">North Palm Beach · Palm Beach County</div>
<h1>Turned down for a loan? <em>Let's get you loan ready.</em></h1>
<p class="lede"><b style="color:#fff">We fix your financial footprint and credit profile so it's bankable.</b> Credit repair, bookkeeping and tax planning under one roof. Then iFinancial funds you, again and again, as your business grows.</p>
<ul class="hero-points"><li>Out of MCAs</li><li>Into bank &amp; SBA</li><li>Lines of credit</li><li>Equipment</li><li>Real estate</li></ul>
<div class="btn-row"><a class="btn btn-gold" href="/bankable-check/">Am I Bankable? (60 sec)</a><a class="btn btn-line" {BOOK_A}>Book a Call Now</a><a class="btn btn-call" href="tel:{TEL}">or call {PHONE}</a></div>
</div>
<div class="score-card" aria-label="Example Loan Score">
<div class="sc-head"><b>Loan Score</b><small>Sample file</small></div>
<div class="sc-row"><span>Personal credit (3 bureaus)</span><span class="pill fix">2 collections</span></div>
<div class="sc-row"><span>Hard inquiries</span><span class="pill wip">11 in 12 mo</span></div>
<div class="sc-row"><span>Books tie to tax returns</span><span class="pill fix">No</span></div>
<div class="sc-row"><span>Debt service coverage</span><span class="pill wip">1.05x</span></div>
<div class="sc-row"><span>Time in business</span><span class="pill ok">4 yrs</span></div>
<div class="sc-foot"><b>Plan:</b> Express Repair round + bookkeeping catch-up. Target: SBA 7(a) in about 6 months.</div>
</div>
</div><span class="tri" aria-hidden="true"></span></section>
<div class="wrap stats-wrap">{stats_block()}</div>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">Lending has changed</div>
<h2>Banks see everything now. Your file has to be ready before you apply.</h2>
<p>Getting a bank loan is harder than it's been in years. Lenders check with each other. Short-term funders are tightening up. One wrong application can follow you for months. Here's what changed.</p></div>
{landscape_cards()}
<div class="btn-row" style="margin-top:28px"><a class="btn btn-navy" href="/lending-has-changed/">How to apply strategically →</a><a class="btn btn-gold" href="/bankable-check/">Am I bankable right now?</a></div>
</div></section>

{mca_compare(CALC_EN)}

<section><div class="wrap">
<div class="section-head"><div class="eyebrow">Not one loan. A lending relationship.</div>
<h2>We take you from MCAs to bank and SBA money, and stay with you.</h2>
<p>Most funders give you money once and disappear. We structure every round for the loan you need today <i>and</i> the one you'll need next year. Each step lowers your cost of capital.</p></div>
{ladder_block()}
<div class="btn-row" style="margin-top:28px"><a class="btn btn-gold" href="/get-out-of-mca/">Get out of MCAs</a><a class="btn btn-line dark-line" {BOOK_A}>Book a Call Now</a></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">Three ways we get you ready</div>
<h2>Fix the file. Then get funded.</h2>
<p>Banks rarely say no because of one thing. It's usually the credit report, the books, and the tax returns not telling the same story. Our accountants, CPA, bookkeepers and credit specialists are all on staff, working in tandem to fix all three and get you funded.</p></div>
{product_cards()}
<div style="margin-top:28px">{offer_strip()}</div>
</div></section>

<section><div class="wrap">
<div class="section-head"><div class="eyebrow">Every type of loan</div>
<h2>What are you trying to get approved for?</h2>
<p>Each lender looks at something different. Pick your loan and see what they check, where people get stuck, and how we fix it.</p></div>
{loan_tiles()}
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">How it works</div><h2>From "denied" to "approved" in four steps.</h2></div>
<div class="steps">
<div class="step"><h3>Free Loan Score</h3><p>We review your credit, financials and tax returns against real lender guidelines. You see exactly what's in the way.</p></div>
<div class="step"><h3>Fix what's blocking you</h3><p>Disputes on inaccurate items, bookkeeping catch-up, and tax planning. Done by our in-house team.</p></div>
<div class="step"><h3>Build the loan file</h3><p>Statements, returns, and a credit report a lender can say yes to, organized into one package.</p></div>
<div class="step"><h3>Get funded through iFinancial</h3><p>We submit strategically, to the right lender at the right time. Then we keep building toward the next, cheaper round.</p></div>
</div>
<div style="margin-top:36px">{check_teaser()}</div>
</div></section>

<section><div class="wrap">
<div class="section-head"><div class="eyebrow">Real businesses, real turnarounds</div><h2>From MCAs to bank money.</h2>
<p>Shared with our clients' permission.</p></div>
{cases_block()}
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">Real clients, real reports</div><h2>Recent results.</h2>
<p>Scores taken from client progress reports, shared with permission. Initials only.</p></div>
{result_cards()}
<p class="fineprint" style="margin-top:16px">Individual results. Scores vary by bureau and scoring model. These are not typical or guaranteed outcomes. <a href="/results/">See all results →</a></p>
</div></section>

<section><div class="wrap">
<div class="section-head"><div class="eyebrow">What clients say</div><h2>Funded, and still working with us.</h2></div>
{reviews_block()}
<p class="fineprint" style="margin-top:14px">From client reviews of iFinancial.</p>
</div></section>

<section><div class="wrap grid-2">
<div><div class="eyebrow">Why it matters</div><h2>A weak file costs you thousands, even when you get approved.</h2>
<p>Lenders price risk. A lower score, messy books, or tax returns that show too little income push you into a higher rate tier. The work you do before you apply often pays for itself on the first loan.</p>
<a class="btn btn-gold" href="/bankable-check/">See where I stand</a></div>
<div>{cost_block()}</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">Guides</div><h2>Know before you apply.</h2><p>Straight talk on credit, business loans, SBA, MCAs and growth, from the team that's funded $50M+ for local owners.</p></div>
{guide_cards(n=6)}
<div class="btn-row" style="margin-top:24px"><a class="btn btn-navy" href="/blog/">All guides →</a></div>
</div></section>

<section><div class="wrap grid-2">
<div><div class="eyebrow">Questions</div><h2>Straight answers.</h2><p>Ask us anything else at <a href="tel:{TEL}">{PHONE}</a>.</p></div>
{faq_block(FAQS)}
</div></section>

{visit_block()}
{band("Don't get stuck in this economy. Be ready for tomorrow.", "Find out in 60 seconds how a bank would read your file. Then let's fix what's in the way.")}
"""
page("/", "Credit Repair & Loan Readiness in North Palm Beach, FL | Loan Ready by iFinancial",
     "Credit repair, bookkeeping and tax planning in North Palm Beach that gets you ready for SBA, bank, equipment, real estate and mortgage loans. Free Loan Score. Call 772-262-5435.",
     home, [faq_schema(FAQS)], priority="1.0")

# ---------------------------------------------------------------- PRODUCT PAGES
PRODUCT_DETAIL = {
"credit-repair": {
 "title": "Credit Repair in North Palm Beach, FL — $250/Month | Loan Ready",
 "desc": "Monthly credit repair on all three bureaus from our North Palm Beach office. $250/month, billed after the work is done. Built to get you loan ready.",
 "h1": "Credit repair that's aimed at an approval.",
 "lede": "$250 a month. Billed after each month's work is done. Every round is aimed at the items a lender will actually care about.",
 "body": """
<h2>What you get every month</h2>
<ul>
<li><b>A full review of all three reports.</b> We go line by line through Equifax, Experian and TransUnion. We look for accounts reported wrong, balances that don't match, duplicate collections, outdated items, and personal information that shouldn't be there.</li>
<li><b>Dispute rounds.</b> We challenge items that are inaccurate, outdated, or can't be verified. Each round is tracked so you know what was sent, to whom, and what came back.</li>
<li><b>Inquiry cleanup.</b> We dispute inquiries you didn't authorize.</li>
<li><b>Coaching on what moves scores.</b> Card balances, timing before you apply, and when not to open new accounts. This is often worth as much as the disputes.</li>
<li><b>A progress report each round.</b> You'll see before and after scores and every item's status on all three bureaus.</li>
</ul>
<h2>What credit repair can and can't do</h2>
<p>The Fair Credit Reporting Act gives you the right to dispute information that's inaccurate, incomplete, or can't be verified. The bureaus have to investigate. Items that can't be verified have to be corrected or removed.</p>
<p>Accurate, timely information can stay on your report. Anyone who promises to remove accurate negative items, or guarantees a specific score, is not being straight with you. We'll tell you up front which items are worth challenging and which ones we'll work around instead.</p>
<h2>Why ours is different: we finish at the lender</h2>
<p>Most credit repair companies stop when the score goes up. We're part of iFinancial, so the goal is the loan. While your credit is being worked, we can also get your books and tax planning in shape. When the whole file is ready, iFinancial places it with a lender that fits.</p>
<h2>How billing works</h2>
<p>You're billed $250 after each month's round is completed, never before. You can cancel at any time. Your agreement will spell out your rights under federal and Florida law, including your right to cancel.</p>
""",
 "faqs": [("How many months will I need?", "It depends on how many items you have and how the bureaus respond. Many files need several rounds. We'll give you an honest estimate after reviewing your reports."),
          ("Will disputing hurt my credit?", "No. Disputing information on your report doesn't lower your score."),
          ("Can I do this myself?", "Yes, and you can dispute directly with the bureaus for free. Clients come to us for the time, the experience, and the path to funding at the end.")]},
"express-credit-repair": {
 "title": "Express Credit Repair — 15–30 Day Rounds | North Palm Beach | Loan Ready",
 "desc": "Express credit repair for owners with a loan on the table. $1,500 + $300 per deleted item, billed after the work is done. North Palm Beach, FL.",
 "h1": "Express Repair for when a loan is waiting.",
 "lede": "$1,500 plus $300 per deleted item. Rounds typically run 15–30 days. You're billed after the work is done, and the per-item fee applies only to items that are actually deleted.",
 "body": """
<h2>Who Express is for</h2>
<p>You have a deal in front of you: a building, a piece of equipment, an SBA loan, or a home. The lender came back with a short list of items to clean up. Express is a concentrated round focused on exactly those items. Your file goes to the front of the line.</p>
<h2>How it works</h2>
<ul>
<li><b>Day 1: Review in the office or by video.</b> We pull your three reports and go over the lender's conditions with you. Then we agree on which items to target.</li>
<li><b>Days 2–30: Priority round.</b> Our team prepares and sends disputes on the targeted items and tracks every response.</li>
<li><b>End of round: Report and billing.</b> You get an updated three-bureau report. The $1,500 program fee is billed after the round. The $300 per-item fee applies only to items that were deleted.</li>
<li><b>Next: Back to the lender.</b> If you're ready, iFinancial takes the updated file to the lender, or to a better one.</li>
</ul>
[[OFFER]]
<h2>An honest note on timing</h2>
<p>Bureaus generally have 30 days to investigate a dispute. Many respond sooner, but some take the full window. We can't control their timeline or guarantee any specific deletion. We can make sure your round is prepared well and goes out fast.</p>
<h2>Express or monthly?</h2>
<p>If you have a closing date or a lender waiting, choose Express. If you're six months or more from applying, the $250/month program is usually the better value. You can start with Express and move to monthly afterward.</p>
""",
 "faqs": [("Do I really get the $1,500 back?", "Yes. If iFinancial funds your deal, we refund your $1,500 Express program fee. The exact terms, including the timeframe, are in your agreement."),
          ("What counts as a deleted item?", "An item that is removed from one of your credit reports as a result of our dispute, confirmed on your updated report. If an item is deleted from all three bureaus, we'll explain upfront how that is counted in your agreement."),
          ("What if nothing is deleted?", "Then no per-item fees apply. We'll review the results with you and lay out the next step honestly."),
          ("Can Express help with a mortgage?", "Yes. Mortgage lenders use your middle score, so moving one bureau can matter. We'll target the bureau that will move the middle score.")]},
"bookkeeping-tax-planning": {
 "title": "Bookkeeping & Tax Planning for Small Business | North Palm Beach | Loan Ready",
 "desc": "Lender-ready bookkeeping and year-round tax planning for Palm Beach County businesses. $500/month ($500K–$1M revenue), $1,000/month ($1M–$3M).",
 "h1": "Books a bank will accept. Taxes that show what you earn.",
 "lede": "$500/month for businesses with $500K–$1M in revenue. $1,000/month for $1M–$3M. Monthly bookkeeping and year-round tax planning, built for your next loan.",
 "body": """
<h2>Why underwriters care about your books</h2>
<p>The fastest way to get turned down is a P&amp;L that doesn't match your tax return, or a tax return that shows almost no profit. Lenders size your loan off documented income. If the books are behind or every possible expense is written off, the bank sees a business that can't afford the payment.</p>
<h2>Save on taxes without killing your borrowing power</h2>
<p>Most owners are told to write off everything. That saves money in April, and then the bank sees a business that barely breaks even. Our in-house accountants and CPA plan your taxes with your next loan in mind. You legally keep more from Uncle Sam, and your returns still show the income an underwriter needs.</p>
<p>The timing matters too. We plan when to file, when to take distributions, and when to apply, so the documents a lender pulls tell the strongest true story about your business.</p>
<h2>What's included</h2>
<ul>
<li><b>Monthly bookkeeping.</b> Categorized transactions, bank and credit card reconciliations, and a monthly close.</li>
<li><b>Lender-ready statements.</b> A P&amp;L and balance sheet every month, in the format underwriters expect.</li>
<li><b>Year-round tax planning.</b> Our CPA and accountants work with you during the year, not just at filing time. Together you balance lower taxes against showing the income your next loan needs.</li>
<li><b>Debt service tracking.</b> We track how much new debt your cash flow can support. You'll know what you can borrow before you apply.</li>
<li><b>Loan file package.</b> Statements, returns, aging reports, and a personal financial statement, organized for the lender.</li>
</ul>
<h2>Pricing</h2>
<p><b>$500–$1M in annual revenue:</b> $500/month.<br><b>$1M–$3M in annual revenue:</b> $1,000/month.<br>Under $500K or over $3M? <a href="/contact/">Call us</a> and we'll quote your situation.</p>
<h2>Behind on your books?</h2>
<p>Most new clients are. We'll start with a catch-up project to bring your books current, then move to the monthly plan. We'll quote the catch-up after we see where things stand.</p>
""",
 "faqs": [("Do you file my tax return?", "Tax planning is included. Ask us about return preparation for your business and personal returns when we meet, and we'll confirm what's covered for your situation."),
          ("What software do you use?", "We work in QuickBooks Online and can usually work with what you already have."),
          ("Do I need this if I just want credit repair?", "Not always. If you're a business owner seeking a business loan, though, the books are usually the bigger problem than the credit score.")]},
}

for p in PRODUCTS:
    d = PRODUCT_DETAIL[p["slug"]]
    path = f"/{p['slug']}/"
    body = page_hero([("Home", "/"), (p["name"], path)], d["h1"], d["lede"], eyebrow=p["name"]) + f"""
<section><div class="wrap layout">
<article class="content">{d['body'].replace('[[OFFER]]', offer_strip())}
<div class="aside-cta"><h3>{p['price']}<span style="font-weight:600;color:var(--muted);font-size:.9rem">{p['per'] or ' ' + p.get('extra','')}</span></h3><p style="margin:0 0 14px">{p['note']}</p>
<a class="btn btn-gold" href="/free-loan-score/">Start with a Free Loan Score</a></div>
<h2>Common questions</h2>{faq_block(d['faqs'])}
</article>
{sidebar()}
</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><div class="eyebrow">Results</div><h2>Recent client reports.</h2></div>{result_cards(3)}
<p class="fineprint" style="margin-top:14px">Shared with permission. Individual results vary and are not guaranteed.</p></div></section>
{band("Ready to see what's in your way?", "Free Loan Score. In our North Palm Beach office or by video.")}"""
    service = {"@context": "https://schema.org", "@type": "Service", "name": p["name"], "provider": {"@id": DOMAIN + "/#business"},
               "areaServed": "Palm Beach County, FL", "description": d["desc"],
               "offers": {"@type": "Offer", "priceCurrency": "USD", "price": p["price"].replace("$", "").replace(",", ""), "description": (p["per"] or p.get("extra","")).strip()}}
    page(path, d["title"], d["desc"], body, [service, faq_schema(d["faqs"]), breadcrumb_schema([("Home", "/"), (p["name"], path)])], priority="0.9")

# ---------------------------------------------------------------- LOAN HUB + PAGES
hub = page_hero([("Home", "/"), ("Business Loans", "/get-loan-ready/")], "Business loans in Palm Beach County, done the right way.",
                "SBA, lines of credit, term loans, equipment, commercial real estate, asset-based and same-day funding. Every lender checks something different. See what they look at, where owners get stuck, and how we get you approved.",
                eyebrow="Business loans · Loan readiness") + f"""
<section><div class="wrap">{loan_tiles()}</div></section>
<section class="alt"><div class="wrap grid-2">
<div><div class="eyebrow">One file, every lender</div><h2>Apply once, the right way.</h2>
<p>Applying with five lenders means five hard inquiries and five chances to get a no. We build one organized file, match it to lenders that fit, and submit it through iFinancial. Fewer inquiries, better odds.</p></div>
<div><h3>Every Loan Ready file includes</h3><ul class="checks"><li>Three-bureau credit review and repair plan</li><li>Current P&amp;L and balance sheet</li><li>Tax returns that tie to the books</li><li>Debt service coverage calculation</li><li>Bank statement review</li><li>Personal financial statement</li></ul></div>
</div></section>
{band("Not sure which loan fits?", "Tell us what you need the money for. We'll tell you which loan fits and what it will take to qualify.")}"""
page("/get-loan-ready/", "Business Loans in Palm Beach County: SBA, Lines of Credit, Equipment | Loan Ready",
     "Business loans for Palm Beach County and Treasure Coast owners: SBA, lines of credit, term loans, equipment, commercial real estate. We get your file bankable, then iFinancial gets you funded.",
     hub, [breadcrumb_schema([("Home", "/"), ("Get Loan Ready", "/get-loan-ready/")])], priority="0.9")

for slug, name, sub, intro, checks, stuck, fix in LOANS:
    path = f"/get-loan-ready/{slug}/"
    ck = "".join(f"<li>{c}</li>" for c in checks)
    st = "".join(f"<li>{c}</li>" for c in stuck)
    body = page_hero([("Home", "/"), ("Get Loan Ready", "/get-loan-ready/"), (name, path)],
                     f"Get ready for {name.lower() if not name.startswith('SBA') else name}.", intro, eyebrow=sub) + f"""
<section><div class="wrap layout"><article class="content">
<h2>What lenders look at</h2><ul class="checks">{ck}</ul>
<h2>Where applicants get stuck</h2><ul>{st}</ul>
<h2>How Loan Ready fixes it</h2><p>{fix}</p>
<div class="aside-cta"><h3>Find out if you're ready for {name.lower() if not name.startswith('SBA') else name}</h3><p style="margin:0 0 14px">Your free Loan Score compares your file to what these lenders require.</p>
<a class="btn btn-gold" href="/free-loan-score/">Get My Free Loan Score</a></div>
<h2>Services that help</h2>
<p><a href="/credit-repair/">Credit Repair Program</a> · <a href="/express-credit-repair/">Express Repair</a> · <a href="/bookkeeping-tax-planning/">Bookkeeping &amp; Tax Planning</a></p>
<p class="fineprint">Loan Ready prepares you to apply. Approval, rates and terms are set by the lender. Funding is arranged through iFinancial and is subject to lender approval.</p>
</article>{sidebar(slug)}</div></section>
{band(f"Want {name.lower() if not name.startswith('SBA') else name} at a better rate?", "Start with the free Loan Score. In person in North Palm Beach, or by video.")}"""
    page(path, f"Get Ready for {name} | North Palm Beach, FL | Loan Ready by iFinancial",
         f"{name}: what lenders check, why applicants get turned down, and how Loan Ready by iFinancial gets your credit, books and taxes ready. North Palm Beach, FL.",
         body, [breadcrumb_schema([("Home", "/"), ("Get Loan Ready", "/get-loan-ready/"), (name, path)])], priority="0.8")

# ---------------------------------------------------------------- AREA PAGES
for slug, name, intro, directions in AREAS:
    path = f"/areas/{slug}/"
    body = page_hero([("Home", "/"), (name, path)], f"Credit repair &amp; loan readiness for {name}.",
                     intro, eyebrow=f"Serving {name}") + f"""
<section><div class="wrap">
<div class="section-head"><div class="eyebrow">What we do for {name}</div><h2>Three services, one goal: the approval.</h2></div>
{product_cards()}
</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><div class="eyebrow">Loans we prepare {name} clients for</div><h2>Pick your loan.</h2></div>{loan_tiles()}</div></section>
<section><div class="wrap grid-2">
<div><div class="eyebrow">Getting here from {name}</div><h2>Our office is close by.</h2><p>{directions}</p>
<p>Open {HOURS}. Phone and video appointments are available if you'd rather not make the drive.</p>
<div class="btn-row"><a class="btn btn-navy" href="https://www.google.com/maps/dir/?api=1&destination={MAPQ}" target="_blank" rel="noopener">Directions</a><a class="btn btn-gold" {BOOK_A}>Book a Call</a></div></div>
<iframe class="map" title="Map to our office" loading="lazy" src="https://www.google.com/maps?q={MAPQ}&output=embed"></iframe>
</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><div class="eyebrow">Guides for {name} owners</div><h2>Know before you apply.</h2></div>{guide_cards(n=3)}</div></section>
{band(f"{name} owners: find out what's blocking your approval.", "Free Loan Score. No obligation.")}"""
    page(path, f"Credit Repair & Business Loan Readiness in {name}, FL | Loan Ready",
         f"Credit repair, bookkeeping and tax planning for {name} business owners and families. Get ready for SBA, equipment, real estate and mortgage loans. Office on Northlake Blvd.",
         body, [breadcrumb_schema([("Home", "/"), (name, path)])], priority="0.7")

# ---------------------------------------------------------------- RESULTS
body = page_hero([("Home", "/"), ("Results", "/results/")], "Client results, straight from the reports.",
                 "These numbers come from our clients' credit progress reports. They're shared with permission, using initials only.", eyebrow="Results") + f"""
<section><div class="wrap">
<div class="section-head"><div class="eyebrow">Business turnarounds</div><h2>From MCAs to bank money.</h2></div>
{cases_block()}
<div class="section-head" style="margin-top:56px"><div class="eyebrow">Credit results</div><h2>Before and after, from the reports.</h2></div>
{result_cards()}
<div class="aside-cta" style="max-width:820px"><h3>Read these honestly</h3>
<p style="margin:0">Every file is different. These are individual results, not typical or guaranteed outcomes. Scores vary by bureau, scoring model and timing. Some items get deleted, and some are verified and stay. Some scores move fast and some take months. We'll tell you what's realistic for your file after we review it.</p></div>
</div></section>
<section class="alt"><div class="wrap grid-2">
<div><div class="eyebrow">What clients say</div><h2>"He under-promised and over-delivered."</h2><p>That's from a client review of our team, and it's how we try to work: honest expectations, then real work.</p></div>
<div><p>Read more reviews on our <a href="https://goifinancial.com">iFinancial site</a> and on Google. Worked with us? We'd appreciate a review.</p>
<a class="btn btn-gold" href="/free-loan-score/">Start My Free Loan Score</a></div>
</div></section>
{band("Your file could be next.", "Free Loan Score in North Palm Beach or by video.")}"""
page("/results/", "Credit Repair Results | Loan Ready by iFinancial | North Palm Beach, FL",
     "Before-and-after credit scores from Loan Ready clients, taken from their progress reports and shared with permission.", body,
     [breadcrumb_schema([("Home", "/"), ("Results", "/results/")])], priority="0.7")

# ---------------------------------------------------------------- FREE LOAN SCORE (Netlify form)
form = f"""
<form class="form" name="loan-score" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="company_website">
<input type="hidden" name="form-name" value="loan-score">
<p class="hidden"><label>Leave this empty <input name="company_website"></label></p>
<input type="hidden" name="bankable_check" id="f-check" value="">
<div class="row">
<div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
</div>
<div class="row">
<div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="f-biz">Business name (if any)</label><input id="f-biz" name="business" autocomplete="organization"></div>
</div>
<div class="row">
<div class="field"><label for="f-loan">What are you trying to get?</label><select id="f-loan" name="loan_type" required>
<option value="">Choose one</option>{''.join(f'<option>{n}</option>' for _, n, *_ in LOANS)}<option>Not sure yet</option></select></div>
<div class="field"><label for="f-amt">How much?</label><select id="f-amt" name="amount"><option>Under $50K</option><option>$50K–$150K</option><option>$150K–$500K</option><option>$500K–$1M</option><option>Over $1M</option><option>Not sure</option></select></div>
</div>
<div class="row">
<div class="field"><label for="f-score">Your credit score, roughly</label><select id="f-score" name="score_range"><option>Under 580</option><option>580–639</option><option>640–679</option><option>680–719</option><option>720+</option><option>Don't know</option></select></div>
<div class="field"><label for="f-rev">Annual business revenue</label><select id="f-rev" name="revenue"><option>No business / personal loan</option><option>Under $500K</option><option>$500K–$1M</option><option>$1M–$3M</option><option>Over $3M</option></select></div>
</div>
<div class="row">
<div class="field"><label for="f-denied">Turned down recently?</label><select id="f-denied" name="recently_denied"><option>No</option><option>Yes, in the last 90 days</option><option>Yes, earlier this year</option></select></div>
<div class="field"><label for="f-meet">How should we meet?</label><select id="f-meet" name="meeting"><option>In the North Palm Beach office</option><option>Video call</option><option>Phone call</option></select></div>
</div>
<div class="field"><label for="f-notes">Anything else we should know?</label><textarea id="f-notes" name="notes" rows="3"></textarea></div>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> I agree that iFinancial may contact me by phone, text or email about my request. Consent isn't a condition of purchase. Message and data rates may apply. Reply STOP to opt out.</label>
<button class="btn btn-gold" type="submit">Get My Free Loan Score</button>
</form>
<script>(function(){{var q=new URLSearchParams(location.search);var c=q.get('check');if(c){{var f=document.getElementById('f-check');if(f)f.value=c+' / 18 ('+(q.get('tier')||'')+')';}}}})();</script>"""
body = f"""<section class="hero page-hero on-dark"><div class="wrap grid-2" style="grid-template-columns:1fr 1fr;align-items:start">
<div><div class="crumbs"><a href="/">Home</a> / Free Loan Score</div><div class="eyebrow">Free · No obligation</div>
<h1>Get your free Loan Score.</h1>
<p class="lede">Tell us what you're trying to get. We'll review your credit, books and tax picture against what lenders actually require, then show you exactly what to fix.</p>
<ul class="hero-points" style="flex-direction:column"><li>Takes about 2 minutes</li><li>We'll call within one business day</li><li>Meet in North Palm Beach, by video, or by phone</li><li>Requesting your Loan Score doesn't affect your credit</li></ul>
<div class="book-box"><b>Rather pick a time right now?</b><span>Choose a slot on our calendar and skip the wait.</span><a class="btn btn-gold" {BOOK_A}>Book a Call Now</a></div>
<p>Prefer to talk now? <a style="color:#fff;font-weight:700" href="tel:{TEL}">Call {PHONE}</a></p></div>
<div>{form}</div>
</div></section>"""
page("/free-loan-score/", "Free Loan Score — See What's Blocking Your Approval | Loan Ready by iFinancial",
     "Free Loan Score from Loan Ready by iFinancial in North Palm Beach. We review your credit, books and taxes against real lender requirements.", body, priority="0.9")

page("/thank-you/", "Thank You | Loan Ready by iFinancial", "We received your request.",
     page_hero([("Home", "/"), ("Thank you", "/thank-you/")], "Got it. We'll be in touch within one business day.",
               f"Don't want to wait for our call? Pick a time on our calendar right now and it's locked in. Or call {PHONE} ({HOURS}).", book_first=True), noindex=True)


# ---------------------------------------------------------------- LENDING HAS CHANGED
body = page_hero([("Home", "/"), ("Lending Has Changed", "/lending-has-changed/")],
                 "Bank lending has changed. Here's how to get approved anyway.",
                 "Banks check with other lenders. Short-term funders are tightening. Where, when and how you apply now decides whether you get a yes.",
                 eyebrow="The 2026 lending landscape") + f"""
<section><div class="wrap layout"><article class="content">
<h2>Lenders can see more than you think</h2>
<p>When you apply for business financing, the lender doesn't just look at your score. They see:</p>
<ul>
<li><b>Every recent hard inquiry</b> on your personal credit, and often your business credit too. They know who else you've applied with and how recently.</li>
<li><b>UCC filings.</b> Most merchant cash advances file a UCC lien. It's public, and lenders check it.</li>
<li><b>Your bank statements.</b> Daily and weekly debits to other funders, NSFs, negative-balance days, and deposit swings are all right there.</li>
<li><b>Shared industry data.</b> In the short-term funding world, funders share information about who has funded whom and how those deals performed.</li>
</ul>
<p>So "apply everywhere and see who says yes" is now the fastest way to get told no.</p>

<h2>Strategic submission: where, when, and how</h2>
<p><b>Where.</b> Every lender has its own box: credit tiers, industries, time in business, revenue, and how much existing debt they'll tolerate. We match your file to lenders whose guidelines you already meet. One well-matched submission beats ten random ones.</p>
<p><b>When.</b> Timing changes the picture. That means after a strong deposit month, after your tax return is filed and shows the right income, after disputed items have cleared, and before new inquiries pile up. A few weeks can turn a decline into an approval.</p>
<p><b>How.</b> A complete, consistent file: credit report, bank statements, tax returns and financial statements that all tell the same story. Underwriters decline files with holes because holes look like risk.</p>

<div class="aside-cta"><h3>Find out if you're ready before a lender does.</h3><p style="margin:0 0 14px">Our 60-second Bankable Check shows you how a bank would read your file.</p>
<div class="btn-row"><a class="btn btn-gold" href="/bankable-check/">Take the Bankable Check</a><a class="btn btn-navy" {BOOK_A}>Book a Call Now</a></div></div>

<h2>MCAs are underwriting like banks used to</h2>
<p>Merchant cash advances used to be the easy yes. That's changing. In our experience, many funders now want credit in the 620s and up, more documentation, cleaner bank statements, and stricter limits on stacking. If short-term money is getting harder to get, waiting until you're desperate is the most expensive plan there is.</p>

<h2>SBA money can't pay off an MCA anymore</h2>
<p>Under SBA rules in effect since 2025, SBA loan proceeds can't be used to refinance merchant cash advances. The SBA also raised the minimum small-business credit score for its streamlined 7(a) small loans (now capped at $350,000), restored its upfront guaranty fees, and requires businesses to be 100% owned by U.S. citizens, nationals or lawful permanent residents. Owners who planned to "just get an SBA loan" to clear their advances need a different first step: conventional financing first, SBA after.</p>
<h2>Taxes vs. borrowing power</h2>
<p>Lenders size your loan off documented income. Writing off everything saves on taxes, but it can make your business look like it can't afford a payment. Proper tax planning balances both. You keep more from Uncle Sam and still qualify for the money you need. <a href="/bookkeeping-tax-planning/">See how our tax planning works →</a></p>

<h2>What "bankable" actually means</h2>
<ul class="checks">
<li>A clean, strong credit profile, with inaccurate items disputed and utilization under control</li>
<li>Few recent inquiries and no unexplained new debt</li>
<li>Bank statements without NSFs, negative days or stacked daily payments</li>
<li>Current books that tie to your tax returns</li>
<li>Tax returns that show enough income to cover the new payment</li>
<li>A plan for which lender comes first, and which comes next</li>
</ul>
<p>That's what we build. <b>We fix your financial footprint and credit profile so it's bankable.</b> Then iFinancial submits it, strategically.</p>
<p class="fineprint">Lending criteria vary by lender and change over time. Descriptions here reflect general industry practice and our own experience, not any specific lender's guidelines.</p>
</article>{sidebar()}</div></section>
{band("Don't get stuck in this economy. Be ready for tomorrow.", "Know where you stand before you apply anywhere.")}"""
page("/lending-has-changed/", "Why Bank Loans Are Harder to Get in 2026, and How to Get Approved | Loan Ready",
     "Banks check with other lenders and see who you applied with. MCAs are tightening. How to submit strategically, and how Loan Ready by iFinancial makes your file bankable.",
     body, [breadcrumb_schema([("Home", "/"), ("Lending Has Changed", "/lending-has-changed/")])], priority="0.9")

# ---------------------------------------------------------------- GET OUT OF MCA
mca_faqs = [
    ("Can an SBA or bank loan pay off my MCA?", "Not with SBA money right now. Under SBA rules in effect since 2025, SBA loan proceeds can't be used to pay off merchant cash advances. Conventional bank loans, lines of credit and term loans can, when the numbers and the file support it. That's why our path pays off MCAs first with lower-cost conventional financing, then moves you into SBA for growth. Lenders look closely at why the advances were taken and whether your cash flow covers the new payment. We get the file to that point."),
    ("What if I have three or four positions open?", "It's common, and it's fixable, but not overnight. Step one is to stop adding positions. Then we work out the order to retire them and what the bank needs to see from your statements before we submit."),
    ("Do I have to stop using MCAs completely?", "Not on day one. If you need capital now, iFinancial can help structure it so it doesn't trap you. The goal is that every round costs less than the last, until you're in bank and SBA money."),
]
body = page_hero([("Home", "/"), ("Get Out of MCAs", "/get-out-of-mca/")],
                 "Stuck in MCAs? Let's get you into bank and SBA money.",
                 "Daily payments eating your cash flow? We'll stop the stacking, rebuild your file, and move you to long-term financing. Then we keep funding you as you grow.",
                 eyebrow="MCA to bank & SBA") + f"""
<section><div class="wrap layout"><article class="content">
<h2>The MCA trap</h2>
<p>It starts with one advance to cover a slow month. Then the daily payments squeeze cash flow, so you take a second. Then a third. Each one makes your bank statements look worse, and banks look at those statements. Soon the only people who will fund you are the people keeping you stuck.</p>

<h2>How we get you out</h2>
<ol>
<li><b>Stop the bleeding.</b> No new positions. We review every advance, its payment and its balance, and map the order to retire them.</li>
<li><b>Fix the footprint.</b> Credit profile repair, bookkeeping caught up, and bank statements cleaned up over the months a bank will review.</li>
<li><b>Tax plan for the loan.</b> Your next return needs to show the income that supports a bank payment. Our in-house CPA plans for that, without overpaying Uncle Sam.</li>
<li><b>Step down your cost of capital.</b> Move from advances to a line of credit or term loan, then to bank and SBA financing. Every round should cost less than the last.</li>
<li><b>Stay funded.</b> We don't fund you once and disappear. We're with you for the next round, and the one after that.</li>
</ol>
{ladder_block()}

<div class="aside-cta"><h3>How deep are you in?</h3><p style="margin:0 0 14px">Take the 60-second Bankable Check, or book a call and bring your MCA statements. We'll map your way out.</p>
<div class="btn-row"><a class="btn btn-gold" {BOOK_A}>Book a Call Now</a><a class="btn btn-navy" href="/bankable-check/">Take the Bankable Check</a></div></div>

<h2>Businesses we've moved out of MCAs</h2>
{cases_block()}
<h2>Common questions</h2>{faq_block(mca_faqs)}
<p class="fineprint">Refinancing depends on lender approval, your cash flow and your full financial profile. Under current SBA rules, SBA loan proceeds can't be used to refinance merchant cash advances. Not every advance can be refinanced with conventional bank debt either.</p>
</article>{sidebar()}</div></section>
{mca_compare(CALC_EN)}
{band("Every month in an MCA costs you. Let's plan your way out.", "Book a call today. Bring your statements, and leave with a plan.")}"""
page("/get-out-of-mca/", "Get Out of Merchant Cash Advances, Into Bank & SBA Loans | Loan Ready by iFinancial",
     "Stuck in stacked MCAs? Loan Ready by iFinancial fixes your credit profile, books, bank statements and tax plan so you can move to bank and SBA financing. North Palm Beach, FL.",
     body, [faq_schema(mca_faqs), breadcrumb_schema([("Home", "/"), ("Get Out of MCAs", "/get-out-of-mca/")])], priority="0.9")

# ---------------------------------------------------------------- BANKABLE CHECK (interactive)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bankable.py')).read())
bankable_page(BK_EN)
calc_page(CALC_EN)

# ---------------------------------------------------------------- CONTACT / ABOUT
body = page_hero([("Home", "/"), ("Visit Us", "/contact/")], "Visit Loan Ready in North Palm Beach.",
                 f"{ADDR_ONE}. Open {HOURS}.", eyebrow="Contact") + visit_block() + f"""
<section><div class="wrap grid-2">
<div><div class="eyebrow">Who we are</div><h2>Part of iFinancial. Built to close the gap.</h2>
<p><b>iFinancial, formerly Finance Solutions Group.</b> Same team, same office, new name.</p>
{stats_block()}
<p>iFinancial bridges the gap between small business owners and the bankers who lend to them. We arrange everything from same-day funding to SBA, asset-based and long-term loans.</p>
<p>Loan Ready is the other half of that work. It's for the owners and families who aren't approvable yet. Our in-house credit team, bookkeeping and tax planning get the file ready, and then iFinancial gets it funded.</p></div>
<div><h3>Our team</h3><ul class="checks"><li>Credit repair specialists for monthly and Express files</li><li>Accountants, a CPA and bookkeepers on staff, working in tandem with the credit team</li><li>Funding advisors at iFinancial for placement</li></ul>
<a class="btn btn-gold" href="/free-loan-score/">Book a Free Loan Score</a></div>
</div></section>"""
page("/contact/", "Contact & Directions — 751 Northlake Blvd, North Palm Beach | Loan Ready",
     f"Visit Loan Ready by iFinancial at {ADDR_ONE}. {HOURS}. Call {PHONE}.", body,
     [breadcrumb_schema([("Home", "/"), ("Visit Us", "/contact/")])], priority="0.8")

# ---------------------------------------------------------------- LEGAL
rights = page_hero([("Home", "/"), ("Your Rights", "/your-rights/")], "Your rights and our disclosures.",
                   "Plain-language summary. Your written agreement contains the complete disclosures required by law.") + """
<section><div class="wrap"><article class="content">
<h2>You can do this yourself</h2>
<p>You have the right to dispute inaccurate information in your credit report by contacting the credit bureau directly, at no cost. Neither you nor any credit repair company has the right to have accurate, current and verifiable information removed from your credit report.</p>
<h2>What we do and don't promise</h2>
<ul><li>We do not guarantee any specific score increase, deletion, or result.</li>
<li>We do not guarantee loan approval. Lenders make all credit decisions.</li>
<li>We never advise you to create a new credit identity or give false information to anyone.</li></ul>
<h2>When you pay</h2>
<p>We do not charge for credit repair services before they are performed. Monthly program fees are billed after each month's services are completed. Express Repair fees are billed after the round is completed, and per-item fees apply only to items deleted.</p>
<h2>Your right to cancel</h2>
<p>You can cancel your contract without penalty within the time period stated in your agreement, as required by the federal Credit Repair Organizations Act and Florida law. Your agreement explains exactly how to cancel.</p>
<h2>Free credit reports</h2>
<p>You can get free credit reports from all three bureaus at AnnualCreditReport.com.</p>
<h2>Questions or complaints</h2>
<p>Contact us at <a href="mailto:info@goifinancial.com">info@goifinancial.com</a> or 772-262-5435. You can also contact the Consumer Financial Protection Bureau, the Federal Trade Commission, or the Florida Attorney General.</p>
</article></div></section>"""
page("/your-rights/", "Your Rights & Disclosures | Loan Ready by iFinancial",
     "Consumer rights and disclosures for Loan Ready by iFinancial credit repair services.", rights, priority="0.3")

privacy = page_hero([("Home", "/"), ("Privacy Policy", "/privacy-policy/")], "Privacy Policy", f"Last updated {TODAY}.") + f"""
<section><div class="wrap"><article class="content">
<h2>What we collect</h2><p>Information you give us through our forms, by phone, or in person: name, contact details, business information, and details about your credit and financing goals. With your written authorization, we also handle your credit reports and financial documents.</p>
<h2>How we use it</h2><p>To respond to your request, provide the services you sign up for, prepare your loan file, and connect you with lenders through iFinancial when you ask us to. We do not sell your personal information.</p>
<h2>Sharing</h2><p>We share information only with service providers who help us operate, with credit bureaus and creditors as part of disputes you authorize, with lenders you choose to apply with, and when required by law.</p>
<h2>Calls and texts</h2><p>If you give consent, we may contact you by phone, text or email. Reply STOP to any text to opt out.</p>
<h2>Security</h2><p>We use reasonable safeguards to protect your information. No method of transmission or storage is 100% secure.</p>
<h2>Contact</h2><p>{ADDR_ONE} · {PHONE} · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article></div></section>"""
page("/privacy-policy/", "Privacy Policy | Loan Ready by iFinancial", "Privacy policy for Loan Ready by iFinancial.", privacy, priority="0.2")

page("/404.html", "Page Not Found | Loan Ready", "Page not found.",
     page_hero([("Home", "/"), ("Not found", "/404.html")], "That page isn't here.", "Try the menu above, or start with a free Loan Score."), noindex=True)

# ---------------------------------------------------------------- BLOG + GROW
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog.py')).read())

# ---------------------------------------------------------------- SPANISH
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content_es.py')).read())

# ---------------------------------------------------------------- sitemap, robots, netlify
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p, pr in PAGES:
        f.write(f"  <url><loc>{DOMAIN}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
with open(os.path.join(ROOT, "_headers"), "w") as f:
    f.write("/assets/*.png\n  Cache-Control: public, max-age=31536000\n/assets/*.css\n  Cache-Control: public, max-age=300\n/*\n  X-Frame-Options: SAMEORIGIN\n  Referrer-Policy: strict-origin-when-cross-origin\n")
print(f"Built {len(PAGES)} indexable pages")
