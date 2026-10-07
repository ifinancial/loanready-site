# Bankable Check page — shared by English and Spanish builds (exec'd inside build.py)

BK_EN = {
    "path": "/bankable-check/",
    "title": "Am I Bankable? Free 60-Second Business Loan Readiness Check | Loan Ready",
    "desc": "Answer 8 questions and see how a bank would read your file: credit, inquiries, MCAs, books, taxes and bank statements. Free, no credit pull. Loan Ready by iFinancial.",
    "home": "Home", "crumb": "Bankable Check",
    "eyebrow": "Free bankability check",
    "h1": "Are you <em>bankable</em> right now?",
    "lede": "Banks check everything now. Answer 8 quick questions the way an underwriter reads your file. You'll see your score, your red flags, and what to fix first.",
    "chips": ["8 questions", "60 seconds", "No credit pull"],
    "count": "Question {i} of {n}",
    "back": "← Back",
    "side_title": "What a bank looks at",
    "cats": ["Credit score", "Recent inquiries", "MCAs & daily payments", "Time in business", "Books vs. tax returns", "Profit on your return", "Late payments", "Bank statements"],
    "trust_quote": "He guided me through the SBA process to secure crucial funding for my business when no one else could.",
    "trust_name": "Peter C., CFO",
    "tiers": {
        "high": ["Bankable", "You may be ready for bank or SBA money.", "Don't waste it. One wrong application can cost you the approval. Let us match you to the right lender and submit at the right time."],
        "mid": ["Close: fixable", "A few things stand between you and a bank yes.", "This is exactly what we fix. Most files like yours need a focused plan of a few months, not years."],
        "low": ["Not yet: let's build the path", "Right now, a bank would likely say no.", "That's not the end. It's the starting point. We fix your financial footprint and step you from expensive money into bank and SBA financing."],
    },
    "flags_title": "What a lender would flag",
    "clean": "No major red flags in your answers. Now the strategy matters: where you apply, when, and in what order.",
    "next_title": "What happens next",
    "next": ["Book a 15-minute call. Bring your questions.", "We pull your full picture: credit, statements, books and taxes.", "You get a plan, and we submit to the right lender when you're ready."],
    "book": "Book My Call Now", "form": "Get My Full Loan Score", "form_path": "/free-loan-score/",
    "call": "or call {phone}",
    "offer": "Start with Express Repair and we'll refund your $1,500 when iFinancial funds your deal.",
    "disclaimer": "Educational self-check only. Not a credit decision or a guarantee of approval. Every lender has its own guidelines.",
    "retake": "Retake the check",
    "of": "of 18",
    "band_h": "Don't get stuck in this economy. Be ready for tomorrow.",
    "band_p": "Talk to us before you talk to a bank.",
    "q": [
        ("What's your credit score, roughly?", [("720 or higher", 3, ""), ("680–719", 2, ""), ("620–679", 1, "Your score is in a range where many banks decline or price you high."), ("Under 620 / not sure", 0, "Your score is below what most banks, and now many MCA funders, accept.")]),
        ("Hard inquiries in the last 12 months?", [("0–3", 2, ""), ("4–8", 1, "Lenders can see you've been shopping around."), ("9 or more", 0, "A long trail of applications tells lenders others have said no.")]),
        ("Open MCAs or daily/weekly payments to funders?", [("None", 3, ""), ("One", 1, "An open advance shows on your statements and often as a UCC filing."), ("Two or more", 0, "Stacked advances are one of the biggest red flags for banks.")]),
        ("How long have you been in business?", [("2+ years", 2, ""), ("1–2 years", 1, "Many bank and SBA lenders prefer 2+ years of history."), ("Under 1 year", 0, "Under a year limits you to a narrow set of lenders.")]),
        ("Are your books current, and do they match your tax returns?", [("Yes", 2, ""), ("Behind or not sure", 1, "Books that don't tie to your returns stall underwriting."), ("No bookkeeping", 0, "Without financial statements, bank and SBA loans are off the table.")]),
        ("What did your last business tax return show?", [("A healthy profit", 2, ""), ("A small profit", 1, "Thin profit on paper limits how much a bank will lend."), ("A loss", 0, "A loss on your return usually means a decline, even with strong revenue.")]),
        ("Late payments or collections in the last 2 years?", [("None", 2, ""), ("1–2", 1, "Recent late payments or collections drag your profile down."), ("3 or more", 0, "Multiple recent derogatory items will stop most bank approvals.")]),
        ("NSFs or negative-balance days in the last 3 months?", [("None", 2, ""), ("A few", 1, "Underwriters count NSFs and negative days on your statements."), ("Frequent", 0, "Frequent NSFs tell a lender cash flow can't support a payment.")]),
    ],
}

BK_JS = r"""
(function(){
var T=__T__,f=document.getElementById('quiz'),box=document.getElementById('result'),err=document.getElementById('quiz-err');
f.addEventListener('submit',function(e){
 e.preventDefault();var total=0,flags=[],ok=true;
 for(var i=0;i<T.n;i++){var c=f.querySelector('input[name=q'+i+']:checked');if(!c){ok=false;break;}total+=+c.value;if(c.dataset.flag)flags.push(c.dataset.flag);}
 if(!ok){err.hidden=false;return;} err.hidden=true;
 var k=total>=15?'high':(total>=9?'mid':'low'),t=T.tiers[k];
 box.className='result-box tier-'+k;
 document.getElementById('r-num').textContent=total;document.getElementById('r-tier').textContent=t[0];
 document.getElementById('r-head').textContent=t[1];document.getElementById('r-text').textContent=t[2];
 var ul=document.getElementById('r-flags');ul.innerHTML='';flags.forEach(function(x){var li=document.createElement('li');li.textContent=x;ul.appendChild(li);});
 ul.hidden=!flags.length;document.getElementById('r-clean').hidden=!!flags.length;
 document.getElementById('r-form').href=T.form+'?check='+total+'&tier='+encodeURIComponent(t[0]);
 box.hidden=false;box.scrollIntoView({behavior:'smooth',block:'start'});
});
f.querySelectorAll('input[type=radio]').forEach(function(r){r.addEventListener('change',function(){r.closest('.q').classList.add('answered');});});
})();
"""

def bankable_page(T):
    n = len(T["q"])
    qhtml = ""
    for i, (q, opts) in enumerate(T["q"]):
        o = "".join(f'<label class="opt"><input type="radio" name="q{i}" value="{pts}" data-flag="{flag}"><span>{t}</span></label>' for t, pts, flag in opts)
        qhtml += f'<fieldset class="q"><legend><span class="qn">{i+1}</span><span class="qt"><small>{T["cats"][i]}</small>{q}</span></legend><div class="opts">{o}</div></fieldset>'
    chips = "".join(f"<span>{c}</span>" for c in T["chips"])
    js = BK_JS.replace("__T__", json.dumps({"n": n, "tiers": T["tiers"], "form": T["form_path"]}, ensure_ascii=False))
    home = "/" if LANG == "en" else "/es/"
    body = f"""<section class="hero page-hero bk-hero on-dark"><div class="wrap"><div>
<div class="crumbs"><a href="{home}">{T['home']}</a> / {T['crumb']}</div><div class="eyebrow">{T['eyebrow']}</div>
<h1>{T['h1']}</h1><p class="lede">{T['lede']}</p><div class="chips">{chips}</div>
</div></div><span class="tri" aria-hidden="true"></span></section>
<section class="quiz-section"><div class="wrap quiz-wrap">
<form id="quiz" class="quiz" novalidate>{qhtml}
<p class="quiz-err" id="quiz-err" hidden>{T.get('err', 'Answer all 8 questions to see your result.')}</p>
<button type="submit" class="btn btn-gold btn-lg">{T.get('submit', 'See My Result')}</button></form>
<div id="result" class="result-box" hidden>
<div class="r-top"><div class="r-score"><b id="r-num">0</b><span>/ 18</span></div><div><div class="eyebrow" id="r-tier"></div><h2 id="r-head"></h2><p id="r-text"></p></div></div>
<h3 class="r-sub">{T['flags_title']}</h3><ul id="r-flags" class="flags"></ul><p id="r-clean" class="clean" hidden>{T['clean']}</p>
<div class="btn-row r-cta"><a class="btn btn-gold btn-lg" {BOOK_A}>{T['book']}</a><a class="btn btn-navy" id="r-form" href="{T['form_path']}">{T['form']}</a><a class="btn btn-call dark" href="tel:{TEL}">{T['call'].replace('{phone}', PHONE)}</a></div>
<div class="r-offer"><b>$1,500</b><span>{T['offer']}</span></div>
<p class="fineprint">{T['disclaimer']}</p>
</div>
</div></section>
<script>{js}</script>
{band(T['band_h'], T['band_p'])}"""
    page(T["path"], T["title"], T["desc"], body, priority="0.9")
