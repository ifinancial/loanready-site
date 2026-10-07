# Spanish version of the site (exec'd inside build.py after the English pages)
LANG = "es"
HOURS_ES = "Lun–Vie 9:00 am – 5:30 pm"

# ---------------------------------------------------------------- Calculator ES
CALC_ES = {
    "locale": "es-US",
    "cmp": {
        "eyebrow": "El costo real de un MCA",
        "h2": "Los mismos $100,000. Uno cuesta <span class='hl'>{diff}</span> más.",
        "lede": "Un factor de 1.499 suena poco. No lo es. Aquí tiene un adelanto de efectivo al lado de un préstamo bancario al 11% APR, mismo monto y mismo plazo. Mueva los controles para ver su caso.",
        "f_amt": "Monto", "f_factor": "Factor del MCA", "f_months": "Se paga en", "f_apr": "APR del préstamo", "mo": "meses",
        "mca_t": "Adelanto de efectivo (MCA)", "mca_sub": "Factor {factor}", "loan_t": "Préstamo bancario", "loan_sub": "{apr}% APR",
        "payback": "Total a devolver", "cost": "Costo del dinero", "pay_mca": "Pago diario", "pay_loan": "Pago mensual",
        "eff": "APR efectivo (estimado)", "vs": "VS",
        "diff_lead": "El MCA le cuesta", "diff_tail": "más por exactamente el mismo dinero.",
        "cta_h": "Ese dinero se lo podría quedar usted.", "cta_p": "Pasamos negocios de los MCA a financiamiento de banco y SBA.",
        "cta1": "Salir de los MCA", "cta2": "Agendar una llamada",
        "fine": "Solo ilustrativo. Los MCA son compras de ventas futuras, no préstamos, y no tienen APR. El APR efectivo es un estimado con pagos fijos en unos 21 días hábiles al mes. El préstamo se muestra con pagos mensuales que lo amortizan por completo. Sus términos reales serán diferentes.",
    },
    "calc": {
        "path": "/es/calculadora/", "home": "Inicio", "crumb": "Calculadora",
        "title": "Calculadora de Préstamos: SBA, HELOC, Hipoteca, Línea de Crédito, MCA | Loan Ready",
        "desc": "Calculadora gratis para préstamos SBA, a plazo, líneas de crédito, HELOC, hipotecas, equipo, bienes raíces comerciales y MCA. Ajuste cada número y vea su pago y costo real.",
        "eyebrow": "Calculadora de préstamos", "h1": "Haga los números de cualquier préstamo.",
        "lede": "SBA, préstamos a plazo, líneas de crédito, HELOC, hipotecas, equipo, bienes raíces comerciales y MCA. Todo es ajustable. Vea su pago y lo que de verdad cuesta el dinero.",
        "pick": "Elija un tipo de préstamo", "res_cost": "Intereses y cargos", "res_principal": "Capital",
        "cta_h": "¿Quiere una tasa mejor?", "cta_p": "Las tasas dependen de qué tan bancable es su archivo. Hagámoslo más fuerte.",
        "cta1": "¿Soy bancable?", "cta2": "Agendar una llamada",
        "fine": "Estimados solo ilustrativos. Las tasas, cargos y términos reales dependen del prestamista y de su perfil financiero completo.",
        "types": {
            "sba": ["SBA 7(a)", "Financiamiento SBA a largo plazo para capital de trabajo, equipo, expansión o refinanciamiento."],
            "term": ["Préstamo a plazo", "Una suma fija que se paga en un calendario fijo."],
            "loc": ["Línea de crédito", "Use lo que necesite. Solo intereses mientras la usa, y luego la paga."],
            "heloc": ["HELOC", "Préstamo sobre el valor de su casa. Periodo de solo intereses y luego de pago."],
            "mortgage": ["Hipoteca", "Comprar o refinanciar una casa. Incluye impuestos y seguro."],
            "equipment": ["Equipo", "Financie maquinaria, vehículos o tecnología."],
            "cre": ["Bienes raíces comerciales", "Comprar o refinanciar una propiedad comercial o de inversión."],
            "mca": ["MCA", "Vea lo que realmente cuesta un adelanto de efectivo."],
        },
        "f": {"amount": "Monto del préstamo", "rate": "Tasa de interés (APR)", "years": "Plazo", "months": "Plazo", "fee": "Cargos iniciales (financiados)",
              "balance": "Monto utilizado", "payoff": "Pagarlo en", "limit": "Monto utilizado", "draw": "Periodo de uso", "repay": "Periodo de pago",
              "price": "Precio de compra", "down": "Pago inicial", "tax": "Impuesto a la propiedad (al año)", "ins": "Seguro (al año)",
              "amort": "Amortización", "advance": "Monto del adelanto", "factor": "Factor"},
        "u": {"yrs": "años", "mo": "meses"},
        "r": {"monthly": "Pago mensual", "total_interest": "Intereses totales", "total_paid": "Total pagado", "loan_amt": "Monto del préstamo",
              "fees": "Cargos", "pi": "Capital e intereses", "taxins": "Impuestos y seguro", "io": "Pago de solo intereses",
              "payoff_pmt": "Pago para liquidarla", "draw_pmt": "Pago en periodo de uso (solo intereses)", "repay_pmt": "Pago en periodo de pago",
              "daily": "Pago diario", "payback": "Total a devolver", "cost": "Costo del adelanto", "eff": "APR efectivo (estimado)", "weekly": "Pago semanal"},
    },
}

def nav():
    en = EN_MAP.get(CURRENT, "/")
    return f"""
<a class="skip" href="#main">Ir al contenido</a>
<div class="topbar"><div class="wrap">
  <span>{STREET}, {CITY} <span class="hide-sm">· {HOURS_ES}</span></span>
  <span><a href="{en}" hreflang="en" lang="en">English</a> <span class="sep">·</span> <a {BOOK_A}>Agendar llamada</a> <span class="sep">·</span> <a href="tel:{TEL}">Llame al {PHONE}</a></span>
</div></div>
<header class="site-head"><div class="wrap">
  <a class="brand" href="/es/" aria-label="Loan Ready powered by iFinancial — inicio">
    <img src="/assets/ifinancial-logo.png" alt="iFinancial" width="262" height="160">
    <span class="lock"><span class="lr">LOAN READY</span><span class="pb">powered by iFinancial</span></span>
  </a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menú</button>
  <nav class="nav" id="nav" aria-label="Principal">
    <a href="/es/reparacion-de-credito/">Crédito</a>
    <a href="/es/contabilidad-e-impuestos/">Impuestos y Contabilidad</a>
    <a href="/es/salir-de-mca/">Salir de los MCA</a>
    <a href="/es/prestamos/">Préstamos</a>
    <a href="/es/calculadora/">Calculadora</a>
    <a href="/es/contacto/">Visítenos</a>
    <a class="btn btn-gold btn-sm" href="/es/soy-bancable/">¿Soy bancable?</a>
  </nav>
</div></header>"""

def footer():
    return f"""
<footer class="site-foot"><div class="wrap">
  <div class="cols">
    <div class="nap">
      <div class="foot-logo"><img src="/assets/ifinancial-logo.png" alt="iFinancial" width="66" height="40"></div>
      <p><b>Loan Ready powered by iFinancial</b><br>{STREET}<br>{CITY}, {STATE} {ZIP}</p>
      <p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{HOURS_ES}</p>
    </div>
    <div><h4>Servicios</h4><ul>
      <li><a href="/es/reparacion-de-credito/">Programa de Reparación de Crédito</a></li>
      <li><a href="/es/reparacion-express/">Reparación Express</a></li>
      <li><a href="/es/contabilidad-e-impuestos/">Contabilidad y Planificación de Impuestos</a></li>
      <li><a href="/es/salir-de-mca/">Salir de los MCA</a></li>
    </ul></div>
    <div><h4>Herramientas gratis</h4><ul>
      <li><a href="/es/soy-bancable/">¿Soy bancable? (60 segundos)</a></li>
      <li><a href="/es/evaluacion-gratis/">Evaluación gratis (Loan Score)</a></li>
      <li><a href="/es/calculadora/">Calculadora de préstamos</a></li>
      <li><a href="/es/como-cambiaron-los-prestamos/">Cómo cambiaron los préstamos</a></li>
    </ul></div>
    <div><h4>Zonas que servimos</h4><ul><li>North Palm Beach</li><li>Palm Beach Gardens</li><li>Jupiter</li><li>West Palm Beach</li><li>Riviera Beach y Lake Park</li></ul></div>
  </div>
  <div class="legal">
    <p>Loan Ready es un programa de iFinancial. No garantizamos ningún aumento específico de puntaje, eliminación de cuentas ni aprobación de préstamos. La información correcta y vigente no se puede eliminar de un reporte de crédito. Usted tiene derecho a disputar información incorrecta directamente con los burós de crédito sin costo. El financiamiento está sujeto a la aprobación del prestamista. Los resultados individuales varían.</p>
    <p><a href="/es/sus-derechos/">Sus derechos y divulgaciones</a> · <a href="/">English</a> · <a href="https://goifinancial.com">goifinancial.com</a> · © {datetime.date.today().year} iFinancial</p>
  </div>
</div></footer>
<div class="callbar"><a class="c1" href="tel:{TEL}">Llamar</a><a class="c3" {BOOK_A}>Agendar</a><a class="c2" href="/es/soy-bancable/">¿Bancable?</a></div>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
if(b){{b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);}});}}}})();
</script>"""

def page_hero(crumbs, h1, lede, eyebrow=None, book_first=False):
    c = " / ".join([f'<a href="{p}">{n}</a>' for n, p in crumbs[:-1]] + [crumbs[-1][0]])
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    if book_first:
        btns = f'<div class="btn-row"><a class="btn btn-gold" {BOOK_A}>Agendar mi llamada ahora</a><a class="btn btn-line" href="tel:{TEL}">Llame al {PHONE}</a></div>'
    else:
        btns = f'<div class="btn-row"><a class="btn btn-gold" href="/es/soy-bancable/">¿Soy bancable?</a><a class="btn btn-line" {BOOK_A}>Agendar una llamada</a><a class="btn btn-call" href="tel:{TEL}">o llame al {PHONE}</a></div>'
    return f"""<section class="hero page-hero on-dark"><div class="wrap"><div>
<div class="crumbs">{c}</div>{eb}
<h1>{h1}</h1><p class="lede">{lede}</p>
{btns}
</div></div><span class="tri" aria-hidden="true"></span></section>"""

def band(h, p):
    return f"""<section class="band on-dark"><div class="wrap"><div><h2>{h}</h2><p>{p}</p></div>
<div class="btn-row"><a class="btn btn-gold" href="/es/soy-bancable/">¿Soy bancable?</a><a class="btn btn-line" {BOOK_A}>Agendar una llamada</a><a class="btn btn-call" href="tel:{TEL}">o llame al {PHONE}</a></div></div></section>"""

def sidebar(current=None):
    return f"""<aside class="sidebar">
<div class="side-box side-dark"><h3>¿No sabe dónde está parado?</h3><p>Haga la prueba de 60 segundos y vea su archivo como lo ve un banco.</p>
<a class="btn btn-gold" style="width:100%" href="/es/soy-bancable/">¿Soy bancable?</a>
<a class="btn btn-line" style="width:100%;margin-top:10px" {BOOK_A}>Agendar una llamada</a>
<p style="margin:14px 0 0;font-size:.92rem">O llame al <a style="color:#fff" href="tel:{TEL}">{PHONE}</a></p></div>
<div class="side-box"><h3>Le preparamos para</h3><ul>{''.join(f'<li><a href="/es/prestamos/#{s}">{n}</a></li>' for s, n, *_ in LOANS_ES)}</ul></div>
</aside>"""

def visit_block():
    return f"""<section><div class="wrap grid-2">
<div><div class="eyebrow">Visite la oficina</div><h2>Siéntese con nosotros en Northlake Blvd.</h2>
<p>Traiga sus preguntas. Revisamos sus reportes y cada partida con usted. ¿Prefiere no manejar? También atendemos por teléfono y videollamada.</p>
<div class="visit-card"><dl>
<dt>Dirección</dt><dd>{STREET}<br>{CITY}, {STATE} {ZIP}</dd>
<dt>Horario</dt><dd>{HOURS_ES}</dd>
<dt>Teléfono</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd>
<dt>Correo</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
</dl><div class="btn-row" style="margin-top:20px"><a class="btn btn-navy" href="https://www.google.com/maps/dir/?api=1&destination={MAPQ}" target="_blank" rel="noopener">Cómo llegar</a><a class="btn btn-gold" {BOOK_A}>Agendar llamada o visita</a></div></div></div>
<iframe class="map" title="Mapa a Loan Ready, {ADDR_ONE}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={MAPQ}&output=embed&hl=es"></iframe>
</div></section>"""

STATS_ES = [("$50M+", "financiados para nuestros clientes"), ("200+", "clientes atendidos"), ("5 años", "consiguiendo financiamiento"),
            ("En casa", "contadores, CPA y tenedores de libros")]

PRODUCTS_ES = [
    {"slug": "/es/reparacion-de-credito/", "name": "Programa de Reparación de Crédito", "price": "$250", "per": "/mes",
     "note": "Se cobra después de terminar el trabajo de cada mes. Cancele cuando quiera.",
     "blurb": "Rondas mensuales de disputas en los tres burós, un plan por escrito y un reporte de progreso en cada ciclo.",
     "points": ["Revisión completa de los 3 burós", "Disputas de partidas incorrectas, obsoletas o no verificables", "Limpieza de consultas e información personal", "Asesoría de utilización y crédito nuevo", "Reporte de progreso en cada ronda"]},
    {"slug": "/es/reparacion-express/", "name": "Reparación Express", "price": "$1,500", "per": "", "extra": "+ $300 por partida eliminada",
     "note": "Las rondas suelen durar de 15 a 30 días. Se cobra después del trabajo. Los $300 aplican solo a partidas realmente eliminadas.",
     "offer": "¿Le financiamos? Le devolvemos los $1,500.",
     "blurb": "Para dueños con un préstamo en la mesa. Una ronda enfocada en lo que está bloqueando la aprobación.", "feature": True,
     "points": ["Archivo prioritario", "Enfocado en lo que el prestamista señaló", "Paga por eliminación, no por carta", "Reporte posterior de los 3 burós", "Pase directo al financiamiento de iFinancial"]},
    {"slug": "/es/contabilidad-e-impuestos/", "name": "Contabilidad y Planificación de Impuestos", "price": "$500", "per": "/mes",
     "note": "Negocios con ingresos de $500K a $1M. De $1M a $3M: $1,000/mes.",
     "blurb": "Libros listos para el banco y un plan de impuestos que muestra lo que realmente gana: lo primero que piden los evaluadores.",
     "points": ["Contabilidad y conciliaciones mensuales", "Estado de resultados y balance que el banco acepta", "Planificación de impuestos todo el año", "Seguimiento de cobertura de deuda", "Paquete de documentos para su préstamo"]},
]

def product_cards():
    out = []
    for p in PRODUCTS_ES:
        feat = " feature" if p.get("feature") else ""
        tag = '<span class="tag">Préstamo en la mesa</span>' if p.get("feature") else ""
        pts = "".join(f"<li>{x}</li>" for x in p["points"])
        extra = f'<div class="price-extra">{p["extra"]}</div>' if p.get("extra") else ""
        offer = f'<div class="offer-pill">{p["offer"]}</div>' if p.get("offer") else ""
        out.append(f"""<div class="product{feat}">{tag}<h3>{p['name']}</h3><p>{p['blurb']}</p>
<div class="price">{p['price']}<small>{p['per']}</small></div>{extra}<div class="price-note">{p['note']}</div>{offer}
<ul class="checks">{pts}</ul><a class="btn btn-navy" href="{p['slug']}">Vea cómo funciona</a></div>""")
    return '<div class="grid-3">' + "".join(out) + "</div>"

CASES_ES = [
    ("Ragtop", "6 préstamos en 6 meses", "Enterrado en MCA y deuda de alto interés, con pagos diarios que se comían el flujo de caja.",
     ["6 préstamos en 6 meses", "Todos los MCA pagados", "Abrió una nueva división que hoy factura más de $2M al año"]),
    ("DMLPA", "De MCA a 3 líneas de crédito", "Tarjetas de alto interés, deuda de MCA y otras deudas del negocio hundiendo su perfil de crédito.",
     ["Perfil de crédito reparado", "Tarjetas de alto interés y MCA pagados", "3 líneas de crédito comerciales abiertas", "En camino a un préstamo SBA"]),
    ("Burning Hearts Tattoo", "2 MCA pagados antes de tiempo", "Dos adelantos de efectivo y un perfil de crédito que no les dejaba llegar al banco.",
     ["Reparación de crédito completada", "Ambos MCA pagados antes de tiempo", "Ahorro en el costo total de devolución"]),
]

LANDSCAPE_ES = [
    ("Los prestamistas ven con quién más aplicó.", "Cada consulta dura aparece en su crédito personal y del negocio. Los adelantos dejan registros UCC. Sus estados de cuenta muestran cada pago a otro prestamista. Y en el mundo del financiamiento a corto plazo, los fondeadores comparten información entre ellos."),
    ("Dónde y cuándo aplica importa.", "Si aplica después de un mal mes de depósitos, antes de presentar sus impuestos o con cinco prestamistas a la vez, le pueden negar quienes le habrían dicho que sí un mes después. Las consultas de préstamos comerciales en general no tienen la protección que tienen las hipotecas y los préstamos de auto."),
    ("Los MCA se están poniendo más estrictos.", "Lo que estamos viendo: muchos fondeadores ya piden crédito de 620 en adelante, más documentos y reglas más duras contra el apilamiento. Así evaluaban los bancos antes. Si el dinero de MCA es más difícil, el del banco está fuera de alcance sin un plan."),
    ("Impuestos y capacidad de préstamo se jalan entre sí.", "Si descuenta todo, ahorra en impuestos, pero su declaración muestra un negocio que no puede pagar un préstamo. La planificación correcta encuentra el balance: paga menos al Tío Sam y aun así muestra el ingreso que el banco necesita ver."),
]

def landscape_es():
    return '<div class="grid-2 land">' + "".join(f'<div class="land-card"><span class="land-n">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(LANDSCAPE_ES)) + "</div>"

def ladder_es():
    rungs = [("Hoy", "Préstamo puente o reestructura", "Un préstamo puente, o reestructurar su deuda actual sin caer en impago, si necesita alivio ya."),
             ("Meses 1–3", "Arreglar su huella", "Perfil de crédito, libros, estados de cuenta y plan de impuestos. Sin más apilamiento."),
             ("Meses 3–6", "Líneas y préstamos a plazo", "Líneas de crédito y préstamos más baratos que pagan el dinero caro."),
             ("Meses 6–12", "Banco y SBA", "Financiamiento bancario y SBA a largo plazo. Y luego la siguiente ronda.")]
    return '<div class="ladder">' + "".join(f'<div class="rung"><span class="when">{w}</span><h3>{h}</h3><p>{p}</p></div>' for w, h, p in rungs) + "</div>"

def offer_es():
    return offer_strip("Consiga su préstamo y recupere sus $1,500.",
                       "Empiece con Reparación Express. Si iFinancial financia su préstamo, le reembolsamos los $1,500 del programa Express. Los términos están en su contrato.",
                       "Agendar una llamada")

FAQS_ES = [
    ("¿Me pueden sacar de mis adelantos de efectivo (MCA)?", "Muchas veces, sí, con un plan y no con otro adelanto. Paramos el apilamiento, limpiamos sus estados de cuenta, libros y crédito, y lo pasamos a una línea de crédito, préstamo a plazo o SBA cuando su archivo lo permita."),
    ("¿Me perjudica aplicar con muchos prestamistas?", "Puede perjudicarle. Cada consulta dura aparece y los prestamistas ven con quién más aplicó. Por eso enviamos su solicitud de forma estratégica: al prestamista correcto, en el momento correcto, con el archivo completo."),
    ("¿Garantizan que mi puntaje sube o que me aprueban?", "No, y ninguna empresa honesta puede. La ley le permite disputar información incorrecta, obsoleta o no verificable. La información correcta y vigente puede quedarse. Lo que sí prometemos es un plan claro, trabajo real cada ciclo y una opinión honesta de cuándo está listo para aplicar."),
    ("¿Cuándo pago?", "Después de hacer el trabajo. El programa mensual se cobra después de cada ronda. Express se cobra después de la ronda, y los $300 por partida solo aplican a partidas eliminadas. Si iFinancial financia su préstamo, le reembolsamos los $1,500 de Express."),
    ("¿Atienden en español?", "Sí. Puede llamarnos, visitarnos en North Palm Beach o agendar una videollamada."),
]

LOANS_ES = [
    ("sba", "Préstamos SBA", "7(a), 504 y SBA Express. Los plazos más largos y algunas de las tasas más bajas. También el papeleo más exigente: crédito de cada dueño con 20% o más, 2–3 años de declaraciones, flujo que cubra el pago con margen y estados financieros al día."),
    ("equipo", "Financiamiento de equipo", "El equipo es la garantía, pero su tasa depende de su crédito y tiempo en el negocio. Unos pocos puntos pueden cambiarle de nivel de tasa."),
    ("linea", "Línea de crédito comercial", "Capital de trabajo que usa cuando lo necesita. Los bancos miran de cerca el crédito, el saldo promedio diario y si tiene MCA abiertos."),
    ("plazo", "Préstamos a plazo", "Una suma fija con pago fijo, para crecer, refinanciar deuda cara o comprar inventario. Las ganancias en papel deben cubrir el pago."),
    ("comercial", "Bienes raíces comerciales", "Comprar, refinanciar o construir. Crédito y reservas de cada garante, ingresos de la propiedad o del negocio y un estado financiero personal que cuadre."),
    ("activos", "Préstamos basados en activos", "Préstamos según sus cuentas por cobrar, inventario o equipo. Aquí la contabilidad al día lo es todo."),
    ("rapido", "Financiamiento rápido y a corto plazo", "Existe y iFinancial lo puede conseguir, pero cuesta más. Lo usamos como puente, no como costumbre."),
    ("hipoteca", "Hipotecas", "El precio depende de su puntaje medio de los tres burós. Para dueños de negocio, sus impuestos deben mostrar el ingreso que califica."),
]

# ---------------------------------------------------------------- /es/ home
home_es = f"""
<section class="hero on-dark"><div class="wrap">
<div>
<div class="eyebrow">North Palm Beach · Condado de Palm Beach · Atendemos en español</div>
<h1>¿Le negaron un préstamo? <em>Le preparamos para que le aprueben.</em></h1>
<p class="lede"><b style="color:#fff">Arreglamos su huella financiera y su perfil de crédito para que sea bancable.</b> Reparación de crédito, contabilidad y planificación de impuestos bajo un mismo techo. Luego iFinancial le financia, una y otra vez, mientras su negocio crece.</p>
<ul class="hero-points"><li>Salga de los MCA</li><li>Pase a banco y SBA</li><li>Líneas de crédito</li><li>Equipo</li><li>Bienes raíces</li></ul>
<div class="btn-row"><a class="btn btn-gold" href="/es/soy-bancable/">¿Soy bancable? (60 seg)</a><a class="btn btn-line" {BOOK_A}>Agendar una llamada</a><a class="btn btn-call" href="tel:{TEL}">o llame al {PHONE}</a></div>
</div>
<div class="score-card" aria-label="Ejemplo de Loan Score">
<div class="sc-head"><b>Loan Score</b><small>Archivo de ejemplo</small></div>
<div class="sc-row"><span>Crédito personal (3 burós)</span><span class="pill fix">2 cobranzas</span></div>
<div class="sc-row"><span>Consultas duras</span><span class="pill wip">11 en 12 meses</span></div>
<div class="sc-row"><span>Libros cuadran con impuestos</span><span class="pill fix">No</span></div>
<div class="sc-row"><span>Cobertura de deuda</span><span class="pill wip">1.05x</span></div>
<div class="sc-row"><span>Tiempo en el negocio</span><span class="pill ok">4 años</span></div>
<div class="sc-foot"><b>Plan:</b> Ronda Express + puesta al día de la contabilidad. Meta: SBA 7(a) en unos 6 meses.</div>
</div>
</div><span class="tri" aria-hidden="true"></span></section>
<div class="wrap stats-wrap">{stats_block(STATS_ES)}</div>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">Los préstamos cambiaron</div>
<h2>Los bancos ahora lo ven todo. Su archivo tiene que estar listo antes de aplicar.</h2>
<p>Conseguir un préstamo bancario está más difícil que en años. Los prestamistas consultan entre ellos, los fondeadores a corto plazo se están poniendo estrictos y una solicitud equivocada le puede seguir por meses.</p></div>
{landscape_es()}
<div class="btn-row" style="margin-top:28px"><a class="btn btn-navy" href="/es/como-cambiaron-los-prestamos/">Cómo aplicar con estrategia →</a><a class="btn btn-gold" href="/es/soy-bancable/">¿Soy bancable ahora?</a></div>
</div></section>

{mca_compare(CALC_ES)}

<section><div class="wrap">
<div class="section-head"><div class="eyebrow">No es un préstamo. Es una relación.</div>
<h2>Le sacamos de los MCA al dinero de banco y SBA, y nos quedamos con usted.</h2>
<p>La mayoría de los fondeadores le dan dinero una vez y desaparecen. Nosotros estructuramos cada ronda para el préstamo de hoy <i>y</i> el del próximo año. Cada paso baja su costo de capital.</p></div>
{ladder_es()}
<div class="btn-row" style="margin-top:28px"><a class="btn btn-gold" href="/es/salir-de-mca/">Salir de los MCA</a><a class="btn btn-line dark-line" {BOOK_A}>Agendar una llamada</a></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><div class="eyebrow">Tres formas de prepararle</div>
<h2>Arreglamos el archivo. Luego le financiamos.</h2>
<p>Nuestros contadores, CPA, tenedores de libros y especialistas en crédito trabajan juntos, en la misma oficina, para que su crédito, sus libros y sus impuestos cuenten la misma historia.</p></div>
{product_cards()}
<div style="margin-top:28px">{offer_es()}</div>
</div></section>

<section><div class="wrap">
<div class="section-head"><div class="eyebrow">Negocios reales, resultados reales</div><h2>De los MCA al dinero del banco.</h2><p>Compartido con permiso de nuestros clientes.</p></div>
{cases_block(CASES_ES, ("Antes", "Después"))}
</div></section>

<section class="alt"><div class="wrap grid-2">
<div><div class="eyebrow">Preguntas</div><h2>Respuestas directas.</h2><p>¿Otra pregunta? Llame al <a href="tel:{TEL}">{PHONE}</a>.</p></div>
{faq_block(FAQS_ES)}
</div></section>
{visit_block()}
{band("No se quede atascado en esta economía. Esté listo para mañana.", "Vea en 60 segundos cómo un banco leería su archivo. Luego arreglamos lo que esté en el camino.")}
"""
page("/es/", "Reparación de Crédito y Préstamos para Negocios en North Palm Beach, FL | Loan Ready",
     "Arreglamos su huella financiera y su crédito para que sea bancable. Reparación de crédito, contabilidad e impuestos en North Palm Beach. Salga de los MCA y pase a préstamos de banco y SBA.",
     home_es, [faq_schema(FAQS_ES)], priority="0.9")

# ---------------------------------------------------------------- product pages ES
PROD_ES = {
"/es/reparacion-de-credito/": ("Reparación de Crédito en North Palm Beach — $250/mes | Loan Ready",
  "Reparación de crédito mensual en los tres burós, desde nuestra oficina en North Palm Beach. $250 al mes, cobrado después del trabajo.",
  "Reparación de crédito con un objetivo: su aprobación.", "$250 al mes, cobrado después de terminar el trabajo de cada mes. Cada ronda apunta a lo que de verdad le importa al prestamista.", """
<h2>Lo que recibe cada mes</h2>
<ul><li><b>Revisión completa de los tres reportes.</b> Equifax, Experian y TransUnion, línea por línea: cuentas mal reportadas, saldos que no cuadran, cobranzas duplicadas, partidas obsoletas e información personal que no debería estar.</li>
<li><b>Rondas de disputas.</b> Disputamos lo que es incorrecto, obsoleto o no verificable, y le decimos qué se envió, a quién y qué respondieron.</li>
<li><b>Limpieza de consultas</b> que usted no autorizó.</li>
<li><b>Asesoría</b> sobre saldos de tarjetas, cuándo aplicar y cuándo no abrir cuentas nuevas.</li>
<li><b>Reporte de progreso</b> con puntajes de antes y después.</li></ul>
<h2>Lo que la reparación de crédito puede y no puede hacer</h2>
<p>La ley federal (Fair Credit Reporting Act) le da derecho a disputar información incorrecta, incompleta o que no se puede verificar. La información correcta y vigente puede quedarse. Quien le prometa borrar información correcta o le garantice un puntaje no le está diciendo la verdad.</p>
<h2>Terminamos en el prestamista</h2>
<p>Somos parte de iFinancial. El objetivo no es solo subir el puntaje, es el préstamo. Mientras trabajamos su crédito, nuestro equipo de contabilidad e impuestos prepara sus libros, y cuando todo está listo, iFinancial presenta su archivo al prestamista correcto.</p>
<h2>Cómo se cobra</h2>
<p>Se cobran $250 después de completar la ronda de cada mes, nunca antes. Puede cancelar cuando quiera. Su contrato explica sus derechos bajo la ley federal y de Florida, incluido su derecho a cancelar.</p>"""),
"/es/reparacion-express/": ("Reparación de Crédito Express — Rondas de 15 a 30 días | Loan Ready",
  "Reparación Express para dueños con un préstamo en la mesa. $1,500 + $300 por partida eliminada, cobrado después del trabajo. Le devolvemos los $1,500 si iFinancial le financia.",
  "Reparación Express para cuando el préstamo está esperando.", "$1,500 más $300 por partida eliminada. Las rondas suelen durar de 15 a 30 días. Se cobra después del trabajo y los $300 solo aplican a partidas que realmente se eliminan.", """
<h2>Para quién es Express</h2>
<p>Tiene un negocio en frente: un local, un equipo, un SBA o una casa. El prestamista le devolvió una lista corta de cosas por arreglar. Express es una ronda concentrada en esas partidas, y su archivo pasa al frente de la fila.</p>
[[OFFER]]
<h2>Cómo funciona</h2>
<ul><li><b>Día 1: revisión</b> en la oficina o por video. Vemos sus tres reportes y las condiciones del prestamista.</li>
<li><b>Días 2–30: ronda prioritaria.</b> Preparamos y enviamos las disputas y damos seguimiento a cada respuesta.</li>
<li><b>Al final: reporte y cobro.</b> Los $1,500 se cobran después de la ronda. Los $300 aplican solo a partidas eliminadas.</li>
<li><b>Después: de vuelta al prestamista</b> con iFinancial, y si le financiamos, le reembolsamos los $1,500.</li></ul>
<h2>Una nota honesta sobre el tiempo</h2>
<p>Los burós generalmente tienen 30 días para investigar una disputa. No controlamos su tiempo ni garantizamos ninguna eliminación. Sí nos aseguramos de que su ronda salga bien preparada y rápido.</p>"""),
"/es/contabilidad-e-impuestos/": ("Contabilidad y Planificación de Impuestos para Negocios | North Palm Beach | Loan Ready",
  "Contabilidad lista para el banco y planificación de impuestos todo el año. $500/mes ($500K–$1M en ingresos), $1,000/mes ($1M–$3M).",
  "Libros que el banco acepta. Impuestos que muestran lo que gana.", "$500 al mes para negocios con ingresos de $500K a $1M. $1,000 al mes de $1M a $3M. Contadores, CPA y tenedores de libros en casa, trabajando junto al equipo de crédito.", """
<h2>Ahorre en impuestos sin matar su capacidad de préstamo</h2>
<p>A la mayoría de los dueños les dicen que descuenten todo. Eso ahorra en abril, y luego el banco ve un negocio que apenas sale tablas. Nuestros contadores y CPA planifican sus impuestos pensando en su próximo préstamo: legalmente paga menos al Tío Sam y sus declaraciones siguen mostrando el ingreso que el evaluador necesita.</p>
<h2>Qué incluye</h2>
<ul><li><b>Contabilidad mensual</b> con conciliaciones y cierre de mes.</li>
<li><b>Estados financieros</b> (resultados y balance) en el formato que pide el banco.</li>
<li><b>Planificación de impuestos todo el año</b>, no solo en temporada.</li>
<li><b>Seguimiento de cobertura de deuda:</b> sabrá cuánto puede pedir antes de aplicar.</li>
<li><b>Paquete para su préstamo</b> con estados, declaraciones y estado financiero personal.</li></ul>
<h2>Precios</h2>
<p><b>$500K–$1M en ingresos:</b> $500/mes. <b>$1M–$3M:</b> $1,000/mes. ¿Menos de $500K o más de $3M? <a href="/es/contacto/">Llámenos</a> y le cotizamos.</p>"""),
}
for path, (title, desc, h1, lede, body_html) in PROD_ES.items():
    body = page_hero([("Inicio", "/es/"), (h1, path)], h1, lede) + f"""
<section><div class="wrap layout"><article class="content">{body_html.replace('[[OFFER]]', offer_es())}
<h2>Preguntas frecuentes</h2>{faq_block(FAQS_ES[2:4])}</article>{sidebar()}</div></section>
<section class="alt"><div class="wrap"><div class="section-head"><div class="eyebrow">Negocios reales</div><h2>De los MCA al dinero del banco.</h2></div>{cases_block(CASES_ES, ("Antes", "Después"))}</div></section>
{band("¿Listo para ver qué le está frenando?", "Prueba gratis de 60 segundos. Sin consulta de crédito.")}"""
    page(path, title, desc, body, priority="0.8")

# ---------------------------------------------------------------- salir de MCA
body = page_hero([("Inicio", "/es/"), ("Salir de los MCA", "/es/salir-de-mca/")],
                 "¿Atrapado en los MCA? Le pasamos a dinero de banco y SBA.",
                 "¿Pagos diarios comiéndose su flujo de caja? Paramos el apilamiento, reconstruimos su archivo y le pasamos a financiamiento a largo plazo. Y seguimos financiándole mientras crece.",
                 eyebrow="De MCA a banco y SBA") + f"""
<section><div class="wrap layout"><article class="content">
<h2>La trampa del MCA</h2>
<p>Empieza con un adelanto para cubrir un mes flojo. Luego los pagos diarios aprietan el flujo de caja y toma un segundo. Luego un tercero. Cada uno hace ver peor sus estados de cuenta, y los bancos miran esos estados. Al final, los únicos que le financian son los que le mantienen atrapado.</p>
<h2>Cómo le sacamos</h2>
<ol><li><b>Parar la hemorragia.</b> No más posiciones nuevas. Revisamos cada adelanto, su pago y su saldo, y trazamos el orden para salir.</li>
<li><b>Arreglar la huella.</b> Reparación de crédito, contabilidad al día y estados de cuenta limpios en los meses que el banco va a revisar.</li>
<li><b>Planificar impuestos para el préstamo.</b> Su próxima declaración tiene que mostrar el ingreso que soporta un pago bancario. Nuestro CPA se encarga, sin que pague de más.</li>
<li><b>Bajar el costo del capital.</b> De adelantos a línea de crédito o préstamo a plazo, y luego a banco y SBA.</li>
<li><b>Seguir financiado.</b> No le financiamos una vez y desaparecemos. Estamos con usted en la siguiente ronda.</li></ol>
{ladder_es()}
<h2>Negocios que sacamos de los MCA</h2>{cases_block(CASES_ES, ("Antes", "Después"))}
<p class="fineprint">El refinanciamiento depende de la aprobación del prestamista, su flujo de caja y su perfil financiero completo. No todo adelanto se puede refinanciar con deuda bancaria o SBA.</p>
</article>{sidebar()}</div></section>
{mca_compare(CALC_ES)}
{band("Cada mes en un MCA le cuesta. Planifiquemos su salida.", "Agende una llamada hoy. Traiga sus estados de cuenta y salga con un plan.")}"""
page("/es/salir-de-mca/", "Salga de los Adelantos de Efectivo (MCA) y Pase a Préstamos de Banco y SBA | Loan Ready",
     "¿Atrapado en MCA apilados? Loan Ready by iFinancial arregla su crédito, libros, estados de cuenta e impuestos para pasarle a financiamiento de banco y SBA. North Palm Beach, FL.", body, priority="0.9")

# ---------------------------------------------------------------- cómo cambiaron los préstamos
body = page_hero([("Inicio", "/es/"), ("Cómo cambiaron los préstamos", "/es/como-cambiaron-los-prestamos/")],
                 "Los préstamos bancarios cambiaron. Así le aprueban de todos modos.",
                 "Los bancos consultan con otros prestamistas. Los fondeadores a corto plazo se están poniendo estrictos. Hoy, dónde, cuándo y cómo aplica decide si le dicen que sí.", eyebrow="El panorama de préstamos 2026") + f"""
<section><div class="wrap layout"><article class="content">
<h2>Los prestamistas ven más de lo que usted cree</h2>
<ul><li><b>Cada consulta dura reciente</b> en su crédito personal y, muchas veces, en el de su negocio. Saben con quién más aplicó y cuándo.</li>
<li><b>Registros UCC.</b> La mayoría de los MCA registran un gravamen UCC. Es público y los prestamistas lo revisan.</li>
<li><b>Sus estados de cuenta:</b> pagos diarios y semanales a otros fondeadores, sobregiros, días en negativo y cambios en los depósitos.</li>
<li><b>Información compartida:</b> en el mundo del financiamiento a corto plazo, los fondeadores comparten datos de a quién han financiado.</li></ul>
<p>"Aplicar en todos lados a ver quién dice que sí" es hoy la forma más rápida de que le digan que no.</p>
<h2>Envío estratégico: dónde, cuándo y cómo</h2>
<p><b>Dónde.</b> Cada prestamista tiene su caja: nivel de crédito, industria, tiempo en el negocio, ingresos y cuánta deuda tolera. Emparejamos su archivo con prestamistas cuyos requisitos ya cumple.</p>
<p><b>Cuándo.</b> Después de un buen mes de depósitos, después de presentar una declaración que muestre el ingreso correcto, después de que se resuelvan las disputas y antes de que se acumulen consultas nuevas.</p>
<p><b>Cómo.</b> Un archivo completo y consistente: crédito, estados de cuenta, declaraciones y estados financieros que cuentan la misma historia.</p>
<div class="aside-cta"><h3>Sepa si está listo antes que el prestamista.</h3><p style="margin:0 0 14px">Nuestra prueba de 60 segundos le muestra cómo un banco leería su archivo.</p><div class="btn-row"><a class="btn btn-gold" href="/es/soy-bancable/">¿Soy bancable?</a><a class="btn btn-navy" {BOOK_A}>Agendar una llamada</a></div></div>
<h2>Los MCA evalúan como antes evaluaban los bancos</h2>
<p>En nuestra experiencia, muchos fondeadores ya piden crédito de 620 en adelante, más documentos, estados de cuenta más limpios y límites más estrictos al apilamiento. Esperar a estar desesperado es el plan más caro que existe.</p>
<h2>Qué significa "bancable"</h2>
<ul class="checks"><li>Perfil de crédito limpio y fuerte</li><li>Pocas consultas recientes</li><li>Estados de cuenta sin sobregiros ni pagos diarios apilados</li><li>Libros al día que cuadran con sus impuestos</li><li>Declaraciones que muestran ingreso suficiente para el nuevo pago</li><li>Un plan de qué prestamista va primero y cuál después</li></ul>
<p><b>Arreglamos su huella financiera y su perfil de crédito para que sea bancable.</b> Luego iFinancial lo presenta, con estrategia.</p>
<p class="fineprint">Los criterios varían por prestamista y cambian con el tiempo. Esta información refleja prácticas generales de la industria y nuestra experiencia.</p>
</article>{sidebar()}</div></section>
{band("No se quede atascado en esta economía. Esté listo para mañana.", "Sepa dónde está parado antes de aplicar en cualquier lado.")}"""
page("/es/como-cambiaron-los-prestamos/", "Por Qué Es Más Difícil Conseguir un Préstamo Bancario en 2026 | Loan Ready",
     "Los bancos consultan con otros prestamistas y ven con quién aplicó. Los MCA se están poniendo estrictos. Cómo aplicar con estrategia y volverse bancable.", body, priority="0.8")

# ---------------------------------------------------------------- préstamos hub
items = "".join(f'<div class="land-card" id="{s}"><h3>{n}</h3><p>{d}</p></div>' for s, n, d in LOANS_ES)
body = page_hero([("Inicio", "/es/"), ("Préstamos", "/es/prestamos/")], "Le preparamos para todo tipo de préstamo.",
                 "Cada prestamista revisa algo distinto. Esto es lo que miran y cómo le preparamos.", eyebrow="Tipos de préstamo") + f"""
<section><div class="wrap"><div class="grid-2 land">{items}</div>
<div class="btn-row" style="margin-top:28px"><a class="btn btn-gold" href="/es/soy-bancable/">¿Soy bancable?</a><a class="btn btn-navy" href="/es/calculadora/">Calcular mi pago</a></div></div></section>
{band("¿No sabe qué préstamo le conviene?", "Díganos para qué necesita el dinero. Le decimos qué préstamo encaja y qué hace falta para calificar.")}"""
page("/es/prestamos/", "Préstamos SBA, Equipo, Líneas de Crédito, Bienes Raíces e Hipotecas | Loan Ready",
     "Qué revisan los prestamistas en préstamos SBA, de equipo, líneas de crédito, a plazo, bienes raíces comerciales, basados en activos e hipotecas, y cómo le preparamos.", body, priority="0.8")

# ---------------------------------------------------------------- Bankable ES
BK_ES = {
    "path": "/es/soy-bancable/",
    "title": "¿Soy Bancable? Prueba Gratis de 60 Segundos para Préstamos de Negocio | Loan Ready",
    "desc": "Responda 8 preguntas y vea cómo un banco leería su archivo: crédito, consultas, MCA, libros, impuestos y estados de cuenta. Gratis y sin consulta de crédito.",
    "home": "Inicio", "crumb": "¿Soy bancable?",
    "eyebrow": "Prueba de bancabilidad gratis",
    "h1": "¿Es usted <em>bancable</em> hoy?",
    "lede": "Los bancos ahora lo revisan todo. Responda 8 preguntas rápidas como las vería un evaluador. Verá su puntaje, sus alertas y qué arreglar primero.",
    "chips": ["8 preguntas", "60 segundos", "Sin consulta de crédito"],
    "count": "Pregunta {i} de {n}", "back": "← Atrás",
    "side_title": "Lo que mira un banco",
    "cats": ["Puntaje de crédito", "Consultas recientes", "MCA y pagos diarios", "Tiempo en el negocio", "Libros vs. impuestos", "Ganancia declarada", "Pagos atrasados", "Estados de cuenta"],
    "stats": STATS_ES,
    "trust_quote": "Me guió en el proceso SBA para conseguir financiamiento clave para mi negocio cuando nadie más pudo.",
    "trust_name": "Peter C., CFO (traducido del inglés)",
    "tiers": {
        "high": ["Bancable", "Puede que esté listo para dinero de banco o SBA.", "No lo desperdicie. Una solicitud equivocada le puede costar la aprobación. Le emparejamos con el prestamista correcto y aplicamos en el momento correcto."],
        "mid": ["Cerca: tiene arreglo", "Unas pocas cosas le separan de un sí del banco.", "Esto es exactamente lo que arreglamos. La mayoría de los archivos como el suyo necesitan un plan enfocado de unos meses, no de años."],
        "low": ["Todavía no: armemos el camino", "Hoy, un banco probablemente le diría que no.", "Eso no es el final, es el punto de partida. Arreglamos su huella financiera y le llevamos del dinero caro al financiamiento de banco y SBA."],
    },
    "flags_title": "Lo que un prestamista señalaría", "clean": "Sin alertas mayores en sus respuestas. Ahora importa la estrategia: dónde aplica, cuándo y en qué orden.",
    "next_title": "Qué sigue",
    "next": ["Agende una llamada de 15 minutos.", "Revisamos su panorama completo: crédito, estados, libros e impuestos.", "Recibe un plan y aplicamos con el prestamista correcto cuando esté listo."],
    "book": "Agendar mi llamada ahora", "form": "Mi evaluación completa", "form_path": "/es/evaluacion-gratis/",
    "call": "o llame al {phone}",
    "offer": "Empiece con Reparación Express y le reembolsamos los $1,500 cuando iFinancial financie su préstamo.",
    "disclaimer": "Prueba educativa. No es una decisión de crédito ni una garantía de aprobación. Cada prestamista tiene sus propios requisitos.",
    "retake": "Repetir la prueba", "of": "de 18", "err": "Responda las 8 preguntas para ver su resultado.", "submit": "Ver mi resultado",
    "band_h": "No se quede atascado en esta economía. Esté listo para mañana.", "band_p": "Hable con nosotros antes de hablar con un banco.",
    "q": [
        ("¿Cuál es su puntaje de crédito, más o menos?", [("720 o más", 3, ""), ("680–719", 2, ""), ("620–679", 1, "Su puntaje está en un rango donde muchos bancos niegan o cobran caro."), ("Menos de 620 / no sé", 0, "Su puntaje está por debajo de lo que aceptan la mayoría de los bancos y hoy muchos fondeadores de MCA.")]),
        ("¿Consultas duras en los últimos 12 meses?", [("0–3", 2, ""), ("4–8", 1, "Los prestamistas ven que ha estado buscando por todos lados."), ("9 o más", 0, "Una larga lista de solicitudes le dice al prestamista que otros dijeron que no.")]),
        ("¿Tiene MCA abiertos o pagos diarios/semanales a fondeadores?", [("Ninguno", 3, ""), ("Uno", 1, "Un adelanto abierto aparece en sus estados de cuenta y muchas veces como registro UCC."), ("Dos o más", 0, "Los adelantos apilados son una de las mayores alertas para un banco.")]),
        ("¿Cuánto tiempo tiene su negocio?", [("2 años o más", 2, ""), ("1–2 años", 1, "Muchos bancos y prestamistas SBA prefieren 2 años o más."), ("Menos de 1 año", 0, "Menos de un año le limita a muy pocos prestamistas.")]),
        ("¿Sus libros están al día y cuadran con sus impuestos?", [("Sí", 2, ""), ("Atrasados o no sé", 1, "Libros que no cuadran con sus declaraciones frenan la evaluación."), ("No llevo contabilidad", 0, "Sin estados financieros, los préstamos de banco y SBA no son posibles.")]),
        ("¿Qué mostró su última declaración de impuestos del negocio?", [("Buena ganancia", 2, ""), ("Poca ganancia", 1, "Poca ganancia en papel limita cuánto le presta un banco."), ("Pérdida", 0, "Una pérdida en su declaración casi siempre significa un no, aunque venda mucho.")]),
        ("¿Pagos atrasados o cobranzas en los últimos 2 años?", [("Ninguno", 2, ""), ("1–2", 1, "Pagos atrasados o cobranzas recientes bajan su perfil."), ("3 o más", 0, "Varias partidas negativas recientes detienen la mayoría de las aprobaciones.")]),
        ("¿Sobregiros o días en negativo en los últimos 3 meses?", [("Ninguno", 2, ""), ("Algunos", 1, "Los evaluadores cuentan sobregiros y días en negativo."), ("Frecuentes", 0, "Sobregiros frecuentes le dicen al prestamista que el flujo no aguanta un pago.")]),
    ],
}
bankable_page(BK_ES)

calc_page(CALC_ES)

# ---------------------------------------------------------------- evaluación gratis (form)
form_es = f"""
<form class="form" name="loan-score-es" method="POST" action="/es/gracias/" data-netlify="true" netlify-honeypot="company_website">
<input type="hidden" name="form-name" value="loan-score-es">
<p class="hidden"><label>Deje esto vacío <input name="company_website"></label></p>
<input type="hidden" name="bankable_check" id="f-check" value="">
<input type="hidden" name="idioma" value="Español">
<div class="row"><div class="field"><label for="f-name">Nombre completo</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-phone">Teléfono</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div></div>
<div class="row"><div class="field"><label for="f-email">Correo electrónico</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="f-biz">Nombre del negocio (si aplica)</label><input id="f-biz" name="business" autocomplete="organization"></div></div>
<div class="row"><div class="field"><label for="f-loan">¿Qué busca conseguir?</label><select id="f-loan" name="loan_type" required><option value="">Elija uno</option>{''.join(f'<option>{n}</option>' for _, n, _ in LOANS_ES)}<option>Salir de mis MCA</option><option>Todavía no sé</option></select></div>
<div class="field"><label for="f-amt">¿Cuánto?</label><select id="f-amt" name="amount"><option>Menos de $50K</option><option>$50K–$150K</option><option>$150K–$500K</option><option>$500K–$1M</option><option>Más de $1M</option><option>No sé</option></select></div></div>
<div class="row"><div class="field"><label for="f-score">Su puntaje de crédito, más o menos</label><select id="f-score" name="score_range"><option>Menos de 580</option><option>580–639</option><option>640–679</option><option>680–719</option><option>720+</option><option>No sé</option></select></div>
<div class="field"><label for="f-meet">¿Cómo prefiere reunirse?</label><select id="f-meet" name="meeting"><option>En la oficina de North Palm Beach</option><option>Videollamada</option><option>Llamada</option></select></div></div>
<div class="field"><label for="f-notes">¿Algo más que debamos saber?</label><textarea id="f-notes" name="notes" rows="3"></textarea></div>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> Acepto que iFinancial me contacte por teléfono, mensaje de texto o correo sobre mi solicitud. El consentimiento no es condición de compra. Pueden aplicar tarifas de mensajes y datos. Responda STOP para cancelar.</label>
<button class="btn btn-gold" type="submit">Quiero mi evaluación gratis</button>
</form>
<script>(function(){{var q=new URLSearchParams(location.search);var c=q.get('check');if(c){{var f=document.getElementById('f-check');if(f)f.value=c+' / 18 ('+(q.get('tier')||'')+')';}}}})();</script>"""
body = f"""<section class="hero page-hero on-dark"><div class="wrap grid-2" style="grid-template-columns:1fr 1fr;align-items:start">
<div><div class="crumbs"><a href="/es/">Inicio</a> / Evaluación gratis</div><div class="eyebrow">Gratis · Sin compromiso</div>
<h1>Su evaluación gratis (Loan Score).</h1>
<p class="lede">Díganos qué busca conseguir. Revisamos su crédito, libros e impuestos contra lo que los prestamistas realmente piden, y le mostramos qué arreglar.</p>
<ul class="hero-points" style="flex-direction:column"><li>Toma unos 2 minutos</li><li>Le llamamos en un día hábil</li><li>En la oficina, por video o por teléfono</li><li>No afecta su crédito</li></ul>
<div class="book-box"><b>¿Prefiere escoger la hora ahora?</b><span>Elija un horario en nuestro calendario.</span><a class="btn btn-gold" {BOOK_A}>Agendar una llamada</a></div>
<p>¿Prefiere hablar ya? <a style="color:#fff;font-weight:700" href="tel:{TEL}">Llame al {PHONE}</a></p></div>
<div>{form_es}</div></div></section>"""
page("/es/evaluacion-gratis/", "Evaluación Gratis para Préstamos (Loan Score) | Loan Ready by iFinancial",
     "Evaluación gratis: revisamos su crédito, contabilidad e impuestos contra lo que piden los prestamistas. North Palm Beach, FL. Atendemos en español.", body, priority="0.8")

page("/es/gracias/", "Gracias | Loan Ready by iFinancial", "Recibimos su solicitud.",
     page_hero([("Inicio", "/es/"), ("Gracias", "/es/gracias/")], "Recibido. Le contactamos en un día hábil.",
               f"¿No quiere esperar? Escoja un horario en nuestro calendario ahora mismo y queda confirmado. O llame al {PHONE} ({HOURS_ES}).", book_first=True), noindex=True)

# ---------------------------------------------------------------- contacto
body = page_hero([("Inicio", "/es/"), ("Visítenos", "/es/contacto/")], "Visite Loan Ready en North Palm Beach.",
                 f"{ADDR_ONE}. {HOURS_ES}. Atendemos en español.", eyebrow="Contacto") + visit_block() + f"""
<section class="alt"><div class="wrap grid-2">
<div><div class="eyebrow">Quiénes somos</div><h2>Parte de iFinancial. Hechos para cerrar la brecha.</h2>{stats_block(STATS_ES)}
<p>iFinancial conecta a los dueños de pequeños negocios con los banqueros que les prestan: desde financiamiento el mismo día hasta SBA, préstamos basados en activos y a largo plazo. Loan Ready es la otra mitad: preparamos el archivo y luego iFinancial lo financia.</p></div>
<div><h3>Nuestro equipo</h3><ul class="checks"><li>Especialistas en reparación de crédito, mensual y Express</li><li>Contadores, CPA y tenedores de libros en casa, trabajando junto al equipo de crédito</li><li>Asesores de financiamiento de iFinancial</li></ul>
<a class="btn btn-gold" {BOOK_A}>Agendar una llamada</a></div></div></section>"""
page("/es/contacto/", "Contacto — 751 Northlake Blvd, North Palm Beach | Loan Ready", f"Visite Loan Ready by iFinancial en {ADDR_ONE}. {HOURS_ES}. Llame al {PHONE}.", body, priority="0.7")

# ---------------------------------------------------------------- sus derechos
body = page_hero([("Inicio", "/es/"), ("Sus derechos", "/es/sus-derechos/")], "Sus derechos y nuestras divulgaciones.",
                 "Resumen en lenguaje sencillo. Su contrato por escrito contiene las divulgaciones completas que exige la ley.") + f"""
<section><div class="wrap"><article class="content">
<h2>Usted lo puede hacer por su cuenta</h2><p>Tiene derecho a disputar información incorrecta en su reporte de crédito directamente con el buró, sin costo. Ni usted ni ninguna empresa de reparación de crédito tiene derecho a que se elimine información correcta, vigente y verificable.</p>
<h2>Lo que prometemos y lo que no</h2><ul><li>No garantizamos ningún aumento de puntaje, eliminación ni resultado específico.</li><li>No garantizamos la aprobación de préstamos. Las decisiones las toma el prestamista.</li><li>Nunca le aconsejaremos crear una identidad de crédito nueva ni dar información falsa.</li></ul>
<h2>Cuándo paga</h2><p>No cobramos por servicios de reparación de crédito antes de prestarlos. El programa mensual se cobra después de completar los servicios de cada mes. Express se cobra después de la ronda, y los cargos por partida aplican solo a partidas eliminadas.</p>
<h2>Su derecho a cancelar</h2><p>Puede cancelar su contrato sin penalidad dentro del plazo indicado en su contrato, como lo exigen la ley federal (Credit Repair Organizations Act) y la ley de Florida.</p>
<h2>Reportes de crédito gratis</h2><p>Puede obtener sus reportes gratis de los tres burós en AnnualCreditReport.com.</p>
<h2>Preguntas o quejas</h2><p>Escríbanos a <a href="mailto:{EMAIL}">{EMAIL}</a> o llame al {PHONE}. También puede contactar a la Oficina para la Protección Financiera del Consumidor (CFPB), la Comisión Federal de Comercio (FTC) o el Fiscal General de Florida.</p>
</article></div></section>"""
page("/es/sus-derechos/", "Sus Derechos y Divulgaciones | Loan Ready by iFinancial", "Derechos del consumidor y divulgaciones de Loan Ready by iFinancial.", body, priority="0.3")

LANG = "en"
