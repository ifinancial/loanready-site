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
var T=__T__,N=T.n,ans=new Array(N),flags=new Array(N),i=0;
var steps=document.querySelectorAll('.bk-step'),fill=document.getElementById('bk-fill'),cnt=document.getElementById('bk-i'),
back=document.getElementById('bk-back'),side=document.querySelectorAll('.bk-side li'),quiz=document.getElementById('bk-quiz'),res=document.getElementById('bk-result');
function show(k){i=k;steps.forEach(function(s,j){s.hidden=j!==k;});cnt.textContent=k+1;fill.style.width=((k)/N*100)+'%';back.hidden=k===0;
 side.forEach(function(li,j){li.classList.toggle('active',j===k);li.classList.toggle('done',ans[j]!==undefined&&j!==k);});
 var f=steps[k].querySelector('.bk-opt.sel')||steps[k].querySelector('.bk-opt');if(f&&k>0)f.focus({preventScroll:true});}
document.querySelectorAll('.bk-opt').forEach(function(b){b.addEventListener('click',function(){
 var s=+b.dataset.s;ans[s]=+b.dataset.v;flags[s]=b.dataset.flag;
 steps[s].querySelectorAll('.bk-opt').forEach(function(o){o.classList.toggle('sel',o===b);o.setAttribute('aria-pressed',o===b);});
 setTimeout(function(){if(s<N-1)show(s+1);else finish();},260);});});
back.addEventListener('click',function(){if(i>0)show(i-1);});
function finish(){
 var tot=ans.reduce(function(a,b){return a+b;},0),k=tot>=15?'high':(tot>=9?'mid':'low'),t=T.tiers[k];
 quiz.hidden=true;res.hidden=false;res.className='bk-result tier-'+k;
 document.getElementById('r-num').textContent=tot;document.getElementById('r-tier').textContent=t[0];
 document.getElementById('r-head').textContent=t[1];document.getElementById('r-text').textContent=t[2];
 var arc=document.getElementById('g-arc'),L=282.7;arc.style.strokeDasharray='0 '+L;
 setTimeout(function(){arc.style.strokeDasharray=(tot/18*L)+' '+L;},60);
 var ul=document.getElementById('r-flags');ul.innerHTML='';var fl=flags.filter(function(x){return x;});
 fl.forEach(function(x){var li=document.createElement('li');li.textContent=x;ul.appendChild(li);});
 document.getElementById('r-clean').hidden=fl.length>0;ul.hidden=!fl.length;
 document.getElementById('r-form').href=T.form+'?check='+tot+'&tier='+encodeURIComponent(t[0]);
 side.forEach(function(li){li.classList.remove('active');li.classList.add('done');});
 res.scrollIntoView({behavior:'smooth',block:'start'});}
document.getElementById('bk-retake').addEventListener('click',function(){ans=new Array(N);flags=new Array(N);
 document.querySelectorAll('.bk-opt').forEach(function(o){o.classList.remove('sel');});res.hidden=true;quiz.hidden=false;show(0);
 quiz.scrollIntoView({behavior:'smooth',block:'start'});});
show(0);
})();
"""

def bankable_page(T):
    n = len(T["q"])
    steps = ""
    for si, (q, opts) in enumerate(T["q"]):
        o = "".join(
            f'<button type="button" class="bk-opt" aria-pressed="false" data-s="{si}" data-v="{pts}" data-flag="{flag}"><span class="k">{"ABCD"[oi]}</span><span class="t">{txt}</span></button>'
            for oi, (txt, pts, flag) in enumerate(opts))
        steps += f'<div class="bk-step"{" hidden" if si else ""}><div class="bk-cat">{T["cats"][si]}</div><h2>{q}</h2><div class="bk-opts">{o}</div></div>'
    side = "".join(f'<li><span class="dot"></span>{c}</li>' for c in T["cats"])
    chips = "".join(f"<span>{c}</span>" for c in T["chips"])
    nxt = "".join(f"<li><span>{k+1}</span>{x}</li>" for k, x in enumerate(T["next"]))
    js = BK_JS.replace("__T__", json.dumps({"n": n, "tiers": T["tiers"], "form": T["form_path"]}, ensure_ascii=False))
    count = T["count"].replace("{i}", '<b id="bk-i">1</b>').replace("{n}", str(n))
    body = f"""<section class="hero page-hero bk-hero on-dark"><div class="wrap"><div>
<div class="crumbs"><a href="{'/' if LANG == 'en' else '/es/'}">{T['home']}</a> / {T['crumb']}</div><div class="eyebrow">{T['eyebrow']}</div>
<h1>{T['h1']}</h1><p class="lede">{T['lede']}</p><div class="chips">{chips}</div>
</div></div><span class="tri" aria-hidden="true"></span></section>
<section class="bk-section"><div class="wrap bk-grid">
<div class="bk-main">
<div class="bk-card" id="bk-quiz">
<div class="bk-progress"><div class="bk-count">{count}</div><div class="bk-bar"><span id="bk-fill"></span></div></div>
{steps}
<button type="button" class="bk-back" id="bk-back" hidden>{T['back']}</button>
</div>
<div class="bk-card bk-result" id="bk-result" hidden>
<div class="r-head">
<div class="gauge"><svg viewBox="0 0 220 130" aria-hidden="true"><path d="M20 120 A90 90 0 0 1 200 120" class="g-bg"/><path id="g-arc" d="M20 120 A90 90 0 0 1 200 120" class="g-fg"/></svg>
<div class="g-num"><b id="r-num">0</b><span>{T['of']}</span></div></div>
<div><span class="tier-pill" id="r-tier"></span><h2 id="r-head"></h2><p id="r-text"></p></div>
</div>
<div class="r-cols">
<div><h3>{T['flags_title']}</h3><ul id="r-flags" class="flags"></ul><p id="r-clean" class="clean" hidden>{T['clean']}</p></div>
<div><h3>{T['next_title']}</h3><ol class="next">{nxt}</ol></div>
</div>
<div class="btn-row r-cta"><a class="btn btn-gold btn-lg" {BOOK_A}>{T['book']}</a><a class="btn btn-navy" id="r-form" href="{T['form_path']}">{T['form']}</a><a class="btn btn-call dark" href="tel:{TEL}">{T['call'].replace('{phone}', PHONE)}</a></div>
<div class="r-offer"><b>$1,500</b><span>{T['offer']}</span></div>
<p class="fineprint">{T['disclaimer']} <button type="button" class="linkish" id="bk-retake">{T['retake']}</button></p>
</div>
</div>
<aside class="bk-side">
<div class="bk-side-card"><h3>{T['side_title']}</h3><ul>{side}</ul></div>
<div class="bk-side-card trust">{stats_block(T.get('stats'))}
<blockquote>“{T['trust_quote']}”</blockquote><cite>{T['trust_name']}</cite></div>
</aside>
</div></section>
<script>{js}</script>
{band(T['band_h'], T['band_p'])}"""
    page(T["path"], T["title"], T["desc"], body, priority="0.9")
