# Blog engine + Grow Your Business page (exec'd at the end of build.py, English only)
import re as _re

def _strip(html):
    return _re.sub(r"<[^>]+>", " ", html)

def word_count(html):
    return len(_strip(html).split())

def _slug(t):
    t = _re.sub(r"<[^>]+>", "", t).lower()
    return _re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]

def _toc(body):
    items = []
    def sub(m):
        txt = m.group(1)
        i = _slug(txt)
        items.append((i, _re.sub(r"<[^>]+>", "", txt)))
        return f'<h2 id="{i}">{txt}</h2>'
    body = _re.sub(r"<h2>(.*?)</h2>", sub, body)
    return body, items

def _mid_cta(body, post):
    svc_path, svc_name = post["service"]
    cta = f"""<div class="aside-cta mid"><h3>Want to know where you stand?</h3>
<p style="margin:0 0 14px">Take the free 60-second Bankable Check, or book a call with our team in North Palm Beach.</p>
<div class="btn-row"><a class="btn btn-gold" href="/bankable-check/">Am I Bankable?</a><a class="btn btn-navy" {BOOK_A}>Book a Call Now</a></div></div>"""
    parts = body.split("<h2", 3)
    if len(parts) == 4:
        return parts[0] + "<h2" + parts[1] + "<h2" + parts[2] + cta + "<h2" + parts[3]
    return body + cta

def _post_page(p):
    path = f"/blog/{p['slug']}/"
    wc = word_count(p["body"])
    assert wc >= 1000, (p["slug"], wc)
    mins = max(4, round(wc / 230))
    body, toc = _toc(p["body"])
    body = _mid_cta(body, p)
    toc_html = '<nav class="toc" aria-label="In this guide"><b>In this guide</b><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc) + "</ol></nav>"
    svc_path, svc_name = p["service"]
    others = [q for q in BLOG if q["slug"] != p["slug"]]
    # related: same service first, then next in list
    idx = BLOG.index(p)
    related = (others[idx:] + others[:idx])[:3]
    date_h = datetime.date.fromisoformat(p.get("date", TODAY)).strftime("%B %-d, %Y")
    html = page_hero([("Home", "/"), ("Guides", "/blog/"), (p["tag"], path)], p["h1"][0].upper() + p["h1"][1:], p["lede"], eyebrow=p["tag"]) + f"""
<section><div class="wrap layout"><article class="content post">
<div class="post-meta">By the Loan Ready team at iFinancial · {date_h} · {mins} min read</div>
{toc_html}
{body}
<h2 id="faq">Frequently asked questions</h2>{faq_block(p['faqs'])}
<div class="aside-cta"><h3>{svc_name}</h3><p style="margin:0 0 14px">See how this works with our team, in our North Palm Beach office or by video.</p>
<div class="btn-row"><a class="btn btn-gold" href="{svc_path}">Learn about {svc_name}</a><a class="btn btn-navy" {BOOK_A}>Book a Call Now</a></div></div>
<p class="fineprint">General education only, not legal, tax or financial advice. Loan Ready does not guarantee credit score changes, deletions or loan approval. Funding is subject to lender approval.</p>
</article>{sidebar()}</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><div class="eyebrow">Keep reading</div><h2>More guides from our team.</h2></div>{guide_cards(related)}</div></section>
{band("Don't get stuck in this economy. Be ready for tomorrow.", "Find out in 60 seconds how a bank would read your file.")}"""
    article = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["h1"][0].upper() + p["h1"][1:], "description": p["desc"],
        "datePublished": p.get("date", TODAY), "dateModified": TODAY,
        "author": {"@type": "Organization", "name": "Loan Ready by iFinancial", "url": DOMAIN + "/"},
        "publisher": {"@type": "Organization", "name": "iFinancial", "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/ifinancial-logo.png"}},
        "mainEntityOfPage": DOMAIN + path, "image": DOMAIN + "/assets/og-loan-ready.png",
        "wordCount": wc, "inLanguage": "en-US", "articleSection": p["tag"],
        "about": [{"@type": "Thing", "name": p["tag"]}],
        "spatialCoverage": {"@type": "Place", "name": "Palm Beach County, Florida"},
    }
    page(path, p["title"], p["desc"], html,
         [article, faq_schema(p["faqs"]), breadcrumb_schema([("Home", "/"), ("Guides", "/blog/"), (p["tag"], path)])], priority="0.8")
    return wc

counts = {p["slug"]: _post_page(p) for p in BLOG}

hub = page_hero([("Home", "/"), ("Guides", "/blog/")], "Guides for owners who want to get funded.",
                "Plain-English guides on credit repair, business loans, SBA, getting out of MCAs, tax planning and growing your business, written for Palm Beach County and Treasure Coast owners.",
                eyebrow="Loan Ready guides") + f"""
<section><div class="wrap">{guide_cards()}</div></section>
{band("Rather talk it through?", "Book a call with our team. Bring your questions.")}"""
page("/blog/", "Credit Repair & Business Loan Guides | Loan Ready by iFinancial, North Palm Beach",
     "Guides on credit repair, business loans, SBA requirements, MCA debt, tax planning, business credit and growth for Palm Beach County owners.",
     hub, [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Loan Ready guides", "url": DOMAIN + "/blog/",
            "hasPart": [{"@type": "BlogPosting", "headline": p["h1"], "url": f"{DOMAIN}/blog/{p['slug']}/"} for p in BLOG]},
           breadcrumb_schema([("Home", "/"), ("Guides", "/blog/")])], priority="0.8")

# ---------------------------------------------------------------- GROW YOUR BUSINESS (service page)
grow_faqs = [
    ("Is this business consulting?", "Yes, focused on one outcome: making your business bankable and funding its growth at the lowest sensible cost. We combine advisory work with hands-on credit, bookkeeping, tax planning and funding through iFinancial."),
    ("What does it cost?", "It depends on what your business needs. Many clients start with our bookkeeping and tax planning plan ($500 or $1,000 a month based on revenue) plus credit work if needed. We'll recommend a plan after a free review."),
    ("Do you only work with businesses that need a loan right now?", "No. Some of our best results come from owners who start planning 6 to 12 months before they need capital."),
]
body = page_hero([("Home", "/"), ("Grow Your Business", "/grow-your-business/")],
                 "Grow your business with a funding plan, not a funding scramble.",
                 "Business growth consulting for Palm Beach County and Treasure Coast owners. We prepare your business for banking: where to bank, how to build long-term lender relationships, and which financing fits each stage. Then we handle it for you.",
                 eyebrow="Business growth & funding strategy") + f"""
<div class="wrap stats-wrap">{stats_block()}</div>
<section><div class="wrap layout"><article class="content">
<h2>We're not a loan company. We're your path to the bank.</h2>
<p>Most owners meet lenders one transaction at a time, usually when they're already under pressure. That's how businesses end up with expensive money and no relationship. We do it the other way around. We get your business ready for banking first, then help you build relationships with the right lenders so every round of funding costs less than the last.</p>
<h2>What we do for growing businesses</h2>
<ul>
<li><b>Funding roadmap.</b> A 12–24 month plan: what capital you'll need, when, for what, and which lender fits each step.</li>
<li><b>Banking strategy.</b> Where to bank, how to structure your accounts, and how to build a relationship with a banker before you need them.</li>
<li><b>Bankable financials.</b> Our in-house accountants, CPA and bookkeepers keep monthly books current and plan taxes with your next loan in mind. <a href="/bookkeeping-tax-planning/">Learn more</a>.</li>
<li><b>Credit profile.</b> Personal <a href="/credit-repair/">credit repair</a> for owners and a business credit profile that stands on its own. <a href="/blog/how-to-build-business-credit/">How business credit works</a>.</li>
<li><b>KPIs that matter.</b> Gross margin, debt service coverage, collections and cash runway, reviewed with you so growth doesn't outrun cash.</li>
<li><b>Funding through iFinancial.</b> Lines of credit, term loans, equipment, real estate and SBA, submitted strategically. With the right credit profile and financial footprint, that can include 0% introductory-rate options.</li>
</ul>
{offer_strip()}
<h2>Built for the long run</h2>
<p>We don't fund you once and disappear. Ragtop went from stacked MCAs to six loans in six months, paid off every advance, and opened a new division now doing more than $2 million a year. DMLPA went from high-interest cards and MCA debt to three lines of credit and is working on a 10-year SBA loan. That's what start-to-funded looks like.</p>
{cases_block()}
<h2>Read before you grow</h2>
<p><a href="/blog/grow-your-business-without-choking-cash-flow/">How to grow your business without choking your cash flow</a> · <a href="/blog/business-loans-palm-beach-county/">How to get a business loan in Palm Beach County</a> · <a href="/blog/sba-loan-requirements/">SBA loan requirements in 2026</a></p>
<h2>Common questions</h2>{faq_block(grow_faqs)}
</article>{sidebar()}</div></section>
{band("Don't get stuck in this economy. Be ready for tomorrow.", "Book a call and let's map your next 12 months of growth.")}"""
page("/grow-your-business/", "Grow Your Business: Growth Consulting & Funding Strategy | North Palm Beach | Loan Ready",
     "Business growth consulting in North Palm Beach: funding roadmaps, banking strategy, bookkeeping, tax planning, credit and funding through iFinancial. $50M+ funded for 200+ clients.",
     body, [faq_schema(grow_faqs), breadcrumb_schema([("Home", "/"), ("Grow Your Business", "/grow-your-business/")]),
            {"@context": "https://schema.org", "@type": "Service", "name": "Business growth consulting and funding strategy",
             "serviceType": "Business consulting", "provider": {"@id": DOMAIN + "/#business"}, "areaServed": ["Palm Beach County, FL", "Martin County, FL", "St. Lucie County, FL"]}],
     priority="0.9")
print("guide word counts:", counts)
