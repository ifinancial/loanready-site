# Loan calculator + MCA vs bank loan comparison (exec'd inside build.py; shared by EN and ES)

def _pmt(p, apr, n):
    r = apr / 12
    return p / n if r == 0 else p * r / (1 - (1 + r) ** -n)

def _mca_apr(adv, payback, n, per_year=252):
    pmt = payback / n
    lo, hi = 1e-7, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        pv = pmt * (1 - (1 + mid) ** -n) / mid
        if pv > adv: lo = mid
        else: hi = mid
    return mid * per_year * 100

CMP_DEF = {"amt": 100000, "factor": 1.499, "months": 12, "apr": 11}

def cmp_numbers(amt=100000, factor=1.499, months=12, apr=11):
    payback = amt * factor
    days = months * 21
    m_pay = _pmt(amt, apr / 100, months)
    l_total = m_pay * months
    return dict(payback=payback, mca_cost=payback - amt, daily=payback / days,
                eff=_mca_apr(amt, payback, days), monthly=m_pay, loan_total=l_total,
                loan_cost=l_total - amt, diff=payback - l_total)

CALC_EN = {
    "locale": "en-US",
    "cmp": {
        "eyebrow": "The real cost of an MCA",
        "h2": "Same $100,000. One costs <span class='hl'>{diff}</span> more.",
        "lede": "A 1.499 factor rate sounds small. It isn't. Here's a merchant cash advance next to an 11% APR bank loan, same amount, same payoff time. Move the sliders to match your deal.",
        "f_amt": "Amount", "f_factor": "MCA factor rate", "f_months": "Paid back over", "f_apr": "Bank loan APR",
        "mo": "months",
        "mca_t": "Merchant cash advance", "mca_sub": "Factor rate {factor}",
        "loan_t": "Bank loan", "loan_sub": "{apr}% APR",
        "payback": "Total payback", "cost": "Cost of the money", "pay_mca": "Daily payment", "pay_loan": "Monthly payment",
        "eff": "Effective APR (estimate)", "vs": "VS",
        "diff_lead": "The MCA costs you", "diff_tail": "more for the exact same money.",
        "cta_h": "That's money you could keep.", "cta_p": "We move businesses from MCAs into bank and SBA financing.",
        "cta1": "Get Out of MCAs", "cta2": "Book a Call Now",
        "fine": "Illustration only. MCAs are purchases of future receivables, not loans, so they don't carry an APR. The effective APR shown is an estimate assuming fixed payments over about 21 business days a month. Bank loan shown as a fully amortizing monthly loan. Your actual terms will differ.",
    },
    "calc": {
        "path": "/loan-calculator/", "home": "Home", "crumb": "Loan Calculator",
        "title": "Business & Home Loan Calculator: SBA, HELOC, Mortgage, Line of Credit, MCA | Loan Ready",
        "desc": "Free loan calculator for SBA, term loans, lines of credit, HELOCs, mortgages, equipment, commercial real estate and MCAs. Adjust every number. See your payment and true cost.",
        "eyebrow": "Loan calculator",
        "h1": "Run the numbers on any loan.",
        "lede": "SBA, term loans, lines of credit, HELOCs, mortgages, equipment, commercial real estate, and MCAs. Every number is adjustable. See your payment and what the money really costs.",
        "pick": "Choose a loan type",
        "res_cost": "Interest & fees", "res_principal": "Principal",
        "cta_h": "Want a better rate than this?", "cta_p": "Rates and terms depend on how bankable your file is. Let's make yours stronger.",
        "cta1": "Am I Bankable?", "cta2": "Book a Call Now",
        "fine": "Estimates for illustration only. Actual rates, fees and terms depend on the lender and your full financial profile.",
        "types": {
            "sba": ["SBA 7(a)", "Long-term SBA financing for working capital, equipment, expansion or refinancing."],
            "term": ["Term Loan", "A fixed amount paid back on a fixed schedule."],
            "loc": ["Line of Credit", "Draw what you need. Interest-only while you use it, then pay it down."],
            "heloc": ["HELOC", "Borrow against home equity. Interest-only draw period, then repayment."],
            "mortgage": ["Mortgage", "Buy or refinance a home. Includes taxes and insurance."],
            "equipment": ["Equipment", "Finance machines, vehicles or technology."],
            "cre": ["Commercial Real Estate", "Buy or refinance owner-occupied or investment property."],
            "mca": ["MCA", "See what a merchant cash advance really costs."],
        },
        "f": {
            "amount": "Loan amount", "rate": "Interest rate (APR)", "years": "Term", "months": "Term", "fee": "Upfront fees (financed)",
            "balance": "Amount drawn", "payoff": "Pay it off over", "limit": "Amount drawn", "draw": "Draw period", "repay": "Repayment period",
            "price": "Purchase price", "down": "Down payment", "tax": "Property tax (per year)", "ins": "Insurance (per year)",
            "amort": "Amortization", "advance": "Advance amount", "factor": "Factor rate",
        },
        "u": {"yrs": "yrs", "mo": "mo"},
        "r": {
            "monthly": "Monthly payment", "total_interest": "Total interest", "total_paid": "Total paid", "loan_amt": "Loan amount",
            "fees": "Fees", "pi": "Principal & interest", "taxins": "Taxes & insurance", "io": "Interest-only payment",
            "payoff_pmt": "Payment to pay it off", "draw_pmt": "Draw-period payment (interest-only)", "repay_pmt": "Repayment-period payment",
            "daily": "Daily payment", "payback": "Total payback", "cost": "Cost of the advance", "eff": "Effective APR (estimate)",
            "weekly": "Weekly payment",
        },
    },
}

CALC_JS = r"""
(function(){
var L=__L__,fmt=new Intl.NumberFormat(L.locale,{style:'currency',currency:'USD',maximumFractionDigits:0});
function $(id){return document.getElementById(id);}
function pmt(p,apr,n){var r=apr/12;return r===0?p/n:p*r/(1-Math.pow(1+r,-n));}
function mcaApr(adv,payback,n){var p=payback/n,lo=1e-7,hi=1,m;for(var k=0;k<200;k++){m=(lo+hi)/2;var pv=p*(1-Math.pow(1+m,-n))/m;if(pv>adv)lo=m;else hi=m;}return m*252*100;}
function pct(v){return v.toLocaleString(L.locale,{maximumFractionDigits:0})+'%';}
// ---------- comparison
var C=document.getElementById('cmp');
if(C){
 var ins=C.querySelectorAll('[data-c]');
 function cmp(){
  var v={};ins.forEach(function(i){if(i.type==='range'||!v[i.dataset.c])v[i.dataset.c]=+i.value;});
  var a=v.amt,f=v.factor,m=v.months,apr=v.apr,days=m*21,pb=a*f,mp=pmt(a,apr/100,m),lt=mp*m;
  $('c-pb').textContent=fmt.format(pb);$('c-mc').textContent=fmt.format(pb-a);$('c-dp').textContent=fmt.format(pb/days);
  $('c-eff').textContent=pct(mcaApr(a,pb,days));$('c-lt').textContent=fmt.format(lt);$('c-lc').textContent=fmt.format(lt-a);
  $('c-mp').textContent=fmt.format(mp);var d=fmt.format(pb-lt);$('c-diff').textContent=d;C.querySelectorAll('.c-diff2').forEach(function(e){e.textContent=d;});
  $('c-fv').textContent=f.toFixed(3);$('c-av').textContent=apr;$('c-apr').textContent=apr+'%';
  var mx=Math.max(pb-a,1);$('c-bar-m').style.width='100%';$('c-bar-l').style.width=Math.max(2,(lt-a)/mx*100)+'%';
  C.querySelectorAll('[data-out]').forEach(function(o){var i=C.querySelector('[data-c="'+o.dataset.out+'"]');o.textContent=o.dataset.fmt==='$'?fmt.format(+i.value):(o.dataset.fmt==='x'?(+i.value).toFixed(3):i.value);});
 }
 ins.forEach(function(i){i.addEventListener('input',cmp);});cmp();
}
// ---------- calculator
var K=document.getElementById('calc');
if(!K)return;
var T=L.types,cur=Object.keys(T)[0];
function field(k,f){
 var u=f.u==='$'?'$':'',suf=f.u==='%'?'%':(f.u==='x'?'×':(f.u&&f.u!=='$'?' '+f.u:''));
 return '<div class="cf"><div class="cf-top"><label for="i-'+k+'">'+f.l+'</label><div class="cf-num">'+(u?'<span>$</span>':'')+
 '<input id="i-'+k+'" type="number" inputmode="decimal" min="'+f.min+'" max="'+f.max+'" step="'+f.step+'" value="'+f.v+'" data-k="'+k+'">'+(suf?'<span>'+suf+'</span>':'')+
 '</div></div><input type="range" min="'+f.min+'" max="'+f.max+'" step="'+f.step+'" value="'+f.v+'" data-r="'+k+'" aria-label="'+f.l+'"></div>';
}
function render(){
 var t=T[cur];$('k-desc').textContent=t.d;
 $('k-fields').innerHTML=Object.keys(t.f).map(function(k){return field(k,t.f[k]);}).join('');
 $('k-fields').querySelectorAll('input').forEach(function(i){i.addEventListener('input',function(){
  var k=i.dataset.k||i.dataset.r,o=$('k-fields').querySelector(i.dataset.k?'[data-r="'+k+'"]':'[data-k="'+k+'"]');o.value=i.value;t.f[k].v=+i.value;calc();});});
 K.querySelectorAll('.ktab').forEach(function(b){b.classList.toggle('on',b.dataset.t===cur);b.setAttribute('aria-selected',b.dataset.t===cur);});
 calc();
}
function g(k){return +T[cur].f[k].v;}
function out(big,bigLabel,rows,principal,cost){
 $('k-big').textContent=fmt.format(big);$('k-big-l').textContent=bigLabel;
 $('k-rows').innerHTML=rows.map(function(r){return '<div class="kr"><span>'+r[0]+'</span><b>'+r[1]+'</b></div>';}).join('');
 var tot=Math.max(principal+cost,1);$('k-p').style.width=(principal/tot*100)+'%';$('k-c').style.width=(cost/tot*100)+'%';
 $('k-pv').textContent=fmt.format(principal);$('k-cv').textContent=fmt.format(cost);
}
function calc(){
 var R=L.r,m,n,p,tot;
 switch(cur){
 case 'sba': p=g('amount')*(1+g('fee')/100);n=g('years')*12;m=pmt(p,g('rate')/100,n);tot=m*n;
  out(m,R.monthly,[[R.loan_amt,fmt.format(g('amount'))],[R.fees,fmt.format(p-g('amount'))],[R.total_interest,fmt.format(tot-p)],[R.total_paid,fmt.format(tot)]],g('amount'),tot-g('amount'));break;
 case 'term': p=g('amount');n=g('months');m=pmt(p,g('rate')/100,n);tot=m*n;
  out(m,R.monthly,[[R.weekly,fmt.format(m*12/52)],[R.total_interest,fmt.format(tot-p)],[R.total_paid,fmt.format(tot)]],p,tot-p);break;
 case 'loc': p=g('balance');var io=p*g('rate')/100/12;n=g('payoff');m=pmt(p,g('rate')/100,n);tot=m*n;
  out(m,R.payoff_pmt,[[R.io,fmt.format(io)],[R.total_interest,fmt.format(tot-p)],[R.total_paid,fmt.format(tot)]],p,tot-p);break;
 case 'heloc': p=g('limit');var r=g('rate')/100,dm=g('draw')*12,rm=g('repay')*12,iop=p*r/12,rp=pmt(p,r,rm);tot=iop*dm+rp*rm;
  out(iop,R.draw_pmt,[[R.repay_pmt,fmt.format(rp)],[R.total_interest,fmt.format(tot-p)],[R.total_paid,fmt.format(tot)]],p,tot-p);break;
 case 'mortgage': p=g('price')*(1-g('down')/100);n=g('years')*12;var pi=pmt(p,g('rate')/100,n),ti=(g('tax')+g('ins'))/12;tot=pi*n;
  out(pi+ti,R.monthly,[[R.pi,fmt.format(pi)],[R.taxins,fmt.format(ti)],[R.loan_amt,fmt.format(p)],[R.total_interest,fmt.format(tot-p)]],p,tot-p);break;
 case 'equipment': p=g('price')*(1-g('down')/100);n=g('months');m=pmt(p,g('rate')/100,n);tot=m*n;
  out(m,R.monthly,[[R.loan_amt,fmt.format(p)],[R.total_interest,fmt.format(tot-p)],[R.total_paid,fmt.format(tot)]],p,tot-p);break;
 case 'cre': p=g('price')*(1-g('down')/100);n=g('amort')*12;m=pmt(p,g('rate')/100,n);tot=m*n;
  out(m,R.monthly,[[R.loan_amt,fmt.format(p)],[R.total_interest,fmt.format(tot-p)],[R.total_paid,fmt.format(tot)]],p,tot-p);break;
 case 'mca': p=g('advance');var pb=p*g('factor'),days=g('months')*21;
  out(pb/days,R.daily,[[R.weekly,fmt.format(pb/days*5)],[R.payback,fmt.format(pb)],[R.cost,fmt.format(pb-p)],[R.eff,pct(mcaApr(p,pb,days))]],p,pb-p);break;
 }
}
K.querySelectorAll('.ktab').forEach(function(b){b.addEventListener('click',function(){cur=b.dataset.t;render();});});
render();
})();
"""

def _calc_types(T):
    t, f, u = T["types"], T["f"], T["u"]
    def F(key, lab, v, mn, mx, st, unit):
        return key, {"l": lab, "v": v, "min": mn, "max": mx, "step": st, "u": unit}
    cfg = {
        "sba": [F("amount", f["amount"], 500000, 25000, 5000000, 5000, "$"), F("rate", f["rate"], 10.5, 3, 18, 0.125, "%"), F("years", f["years"], 10, 1, 25, 1, u["yrs"]), F("fee", f["fee"], 3, 0, 5, 0.25, "%")],
        "term": [F("amount", f["amount"], 150000, 10000, 2000000, 5000, "$"), F("rate", f["rate"], 11, 4, 40, 0.25, "%"), F("months", f["months"], 60, 6, 120, 6, u["mo"])],
        "loc": [F("balance", f["balance"], 50000, 5000, 1000000, 5000, "$"), F("rate", f["rate"], 12, 4, 40, 0.25, "%"), F("payoff", f["payoff"], 18, 3, 60, 1, u["mo"])],
        "heloc": [F("limit", f["limit"], 100000, 10000, 1000000, 5000, "$"), F("rate", f["rate"], 8.5, 3, 18, 0.125, "%"), F("draw", f["draw"], 10, 1, 15, 1, u["yrs"]), F("repay", f["repay"], 20, 5, 30, 1, u["yrs"])],
        "mortgage": [F("price", f["price"], 450000, 50000, 3000000, 5000, "$"), F("down", f["down"], 20, 0, 60, 1, "%"), F("rate", f["rate"], 6.75, 2, 12, 0.125, "%"), F("years", f["years"], 30, 10, 30, 5, u["yrs"]), F("tax", f["tax"], 6000, 0, 50000, 250, "$"), F("ins", f["ins"], 3600, 0, 30000, 100, "$")],
        "equipment": [F("price", f["price"], 120000, 5000, 2000000, 5000, "$"), F("down", f["down"], 10, 0, 50, 1, "%"), F("rate", f["rate"], 9, 3, 30, 0.25, "%"), F("months", f["months"], 60, 12, 120, 6, u["mo"])],
        "cre": [F("price", f["price"], 1500000, 100000, 20000000, 50000, "$"), F("down", f["down"], 25, 0, 50, 1, "%"), F("rate", f["rate"], 7.5, 3, 15, 0.125, "%"), F("amort", f["amort"], 25, 5, 30, 1, u["yrs"])],
        "mca": [F("advance", f["advance"], 100000, 5000, 2000000, 5000, "$"), F("factor", f["factor"], 1.499, 1.05, 1.6, 0.001, "x"), F("months", f["months"], 12, 3, 24, 1, u["mo"])],
    }
    return {k: {"n": t[k][0], "d": t[k][1], "f": dict(v)} for k, v in cfg.items()}

def calc_js(T):
    L = {"locale": T["locale"], "r": T["calc"]["r"], "types": _calc_types(T["calc"])}
    return CALC_JS.replace("__L__", json.dumps(L, ensure_ascii=False))

def money(x):
    return f"${x:,.0f}"

def mca_compare(T, standalone=True):
    c = T["cmp"]
    d = cmp_numbers(**CMP_DEF)
    h2 = c["h2"].replace("{diff}", f'<span class="c-diff2">{money(d["diff"])}</span>')
    def sl(key, lab, v, mn, mx, st, fmtk, shown):
        return f'<label class="cs"><span class="cs-l">{lab}</span><b data-out="{key}" data-fmt="{fmtk}">{shown}</b><input type="range" data-c="{key}" min="{mn}" max="{mx}" step="{st}" value="{v}"></label>'
    sliders = (sl("amt", c["f_amt"], 100000, 10000, 1000000, 5000, "$", money(100000)) +
               sl("factor", c["f_factor"], 1.499, 1.1, 1.6, 0.001, "x", "1.499") +
               sl("months", c["f_months"] + f' ({c["mo"]})', 12, 3, 24, 1, "", "12") +
               sl("apr", c["f_apr"] + " (%)", 11, 4, 30, 0.25, "", "11"))
    mca_sub = c["mca_sub"].replace("{factor}", '<span id="c-fv">1.499</span>')
    loan_sub = c["loan_sub"].replace("{apr}", '<span id="c-av">11</span>')
    script = f"<script>{calc_js(T)}</script>" if standalone else ""
    return f"""<section class="cmp on-dark" id="cmp"><div class="wrap">
<div class="cmp-head"><div class="eyebrow">{c['eyebrow']}</div><h2>{h2}</h2><p>{c['lede']}</p></div>
<div class="cmp-sliders">{sliders}</div>
<div class="cmp-grid">
<div class="cmp-col bad"><div class="cmp-t">{c['mca_t']}</div><div class="cmp-s">{mca_sub}</div>
<div class="cmp-big" id="c-pb">{money(d['payback'])}</div><div class="cmp-bl">{c['payback']}</div>
<dl><dt>{c['cost']}</dt><dd id="c-mc">{money(d['mca_cost'])}</dd><dt>{c['pay_mca']}</dt><dd id="c-dp">{money(d['daily'])}</dd><dt>{c['eff']}</dt><dd class="eff" id="c-eff">{d['eff']:.0f}%</dd></dl>
<div class="cmp-bar"><span class="m" id="c-bar-m"></span></div></div>
<div class="cmp-vs">{c['vs']}</div>
<div class="cmp-col good"><div class="cmp-t">{c['loan_t']}</div><div class="cmp-s">{loan_sub}</div>
<div class="cmp-big" id="c-lt">{money(d['loan_total'])}</div><div class="cmp-bl">{c['payback']}</div>
<dl><dt>{c['cost']}</dt><dd id="c-lc">{money(d['loan_cost'])}</dd><dt>{c['pay_loan']}</dt><dd id="c-mp">{money(d['monthly'])}</dd><dt>APR</dt><dd id="c-apr">{CMP_DEF['apr']}%</dd></dl>
<div class="cmp-bar"><span class="l" id="c-bar-l" style="width:{max(2, d['loan_cost']/d['mca_cost']*100):.0f}%"></span></div></div>
</div>
<div class="cmp-diff"><span>{c['diff_lead']}</span><b id="c-diff">{money(d['diff'])}</b><span>{c['diff_tail']}</span></div>
<div class="cmp-cta"><div><h3>{c['cta_h']}</h3><p>{c['cta_p']}</p></div><div class="btn-row"><a class="btn btn-gold btn-lg" href="{'/get-out-of-mca/' if LANG == 'en' else '/es/salir-de-mca/'}">{c['cta1']}</a><a class="btn btn-line" {BOOK_A}>{c['cta2']}</a></div></div>
<p class="cmp-fine">{c['fine']}</p>
</div></section>{script}"""

def calc_page(T):
    k = T["calc"]
    types = _calc_types(k)
    tabs = "".join(f'<button type="button" class="ktab" role="tab" data-t="{key}">{v["n"]}</button>' for key, v in types.items())
    home = "/" if LANG == "en" else "/es/"
    body = f"""<section class="hero page-hero on-dark"><div class="wrap"><div>
<div class="crumbs"><a href="{home}">{k['home']}</a> / {k['crumb']}</div><div class="eyebrow">{k['eyebrow']}</div>
<h1>{k['h1']}</h1><p class="lede">{k['lede']}</p></div></div><span class="tri" aria-hidden="true"></span></section>
<section class="calc-section"><div class="wrap">
<div class="calc" id="calc">
<div class="ktabs" role="tablist" aria-label="{k['pick']}">{tabs}</div>
<div class="kgrid">
<div class="kin"><p class="kdesc" id="k-desc"></p><div id="k-fields"></div></div>
<div class="kout"><div class="kbig"><span id="k-big-l"></span><b id="k-big">$0</b></div>
<div id="k-rows"></div>
<div class="ksplit"><div class="ksbar"><span class="p" id="k-p"></span><span class="c" id="k-c"></span></div>
<div class="kslab"><span><i class="p"></i>{k['res_principal']} <b id="k-pv"></b></span><span><i class="c"></i>{k['res_cost']} <b id="k-cv"></b></span></div></div>
<div class="kcta"><h3>{k['cta_h']}</h3><p>{k['cta_p']}</p><div class="btn-row"><a class="btn btn-gold" href="{'/bankable-check/' if LANG == 'en' else '/es/soy-bancable/'}">{k['cta1']}</a><a class="btn btn-line" {BOOK_A}>{k['cta2']}</a></div></div>
</div></div>
<p class="fineprint" style="margin-top:16px">{k['fine']}</p>
</div></div></section>
{mca_compare(T, standalone=False)}
<script>{calc_js(T)}</script>"""
    page(k["path"], k["title"], k["desc"], body, priority="0.9")
