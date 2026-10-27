#!/usr/bin/env python3
"""Build the generated pages. Spanish index.html is the source of truth.

    python3 scripts/build.py

1. Fills the <!-- areas-* --> / /* areas-css */ marker blocks in index.html
   (Áreas dropdown, city links, dropdown CSS/JS) and refreshes its JSON-LD areaServed.
2. Generates en/index.html by translating index.html.
3. Generates the city pages (/areas/<city>/ and /en/areas/<city>/) and the
   /areas/ hubs from scripts/areas.py, reusing the home's CSS, nav, services,
   contact block and footer so the design stays in sync.
4. Writes sitemap.xml.

Every replacement is asserted, so if the Spanish markup changes in a way this
script doesn't know about, it fails loudly instead of shipping broken pages.
"""
import datetime
import html
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from areas import CITIES, COUNTIES, MENU, PROPERTIES, RECENT  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.alejandragranillorealestate.com'
WA = 'https://wa.me/14154239973'
BY_SLUG = {c['slug']: c for c in CITIES}
# Cities the home page mentions that don't have their own page (yet).
EXTRA_PINS = ['San Jose', 'San Anselmo', 'Daly City']


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def pre(lang):
    return '' if lang == 'es' else '/en'


def write(rel, s):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)


def fill(s, name, content, css=False):
    a, b = (f'/* {name} */', f'/* /{name} */') if css else (f'<!-- {name} -->', f'<!-- /{name} -->')
    assert s.count(a) == 1 and s.count(b) == 1, f'marker {name} missing'
    i, j = s.index(a) + len(a), s.index(b)
    return s[:i] + '\n' + content + '\n' + s[j:]


def between(s, start, end, include=True):
    i = s.index(start)
    j = s.index(end, i) + len(end)
    return s[i:j] if include else s[i + len(start):j - len(end)]


# ---------------------------------------------------------------- UI strings

UI = {
    'es': {
        'home': 'Inicio', 'areas': 'Áreas', 'all_areas': 'Ver todas las áreas',
        'menu_label': 'Áreas que atiendo',
        'title': 'Realtor que habla español en {name}, CA | Alejandra Granillo',
        'eyebrow': 'Agente de bienes raíces que habla español · {county}',
        'h1': 'Realtor en <b>{name}</b>, CA',
        'btn_wa': 'Hablemos por WhatsApp', 'btn_hoods': 'Ver barrios',
        'intro_eye': 'Sobre {name}', 'intro_h': 'Comprar y vender casa en <em>{name}</em>',
        'facts_h': 'Datos rápidos',
        'hoods_eye': 'Barrios', 'hoods_h': 'Barrios y zonas de <em>{name}</em>',
        'why_eye': '¿Por qué {name}?', 'why_h': 'Lo que hace atractiva a <em>{name}</em>',
        'svc_h': 'Cómo te ayudo en <em>{name}</em>',
        'work_eye': 'Portafolio', 'work_h_city': 'Mis ventas en <em>{name}</em>',
        'work_h': 'Trabajo reciente en el <em>Bay Area</em>', 'work_more': 'Ver portafolio completo',
        'sold': 'Vendida',
        'faq_eye': 'Preguntas frecuentes', 'faq_h': 'Preguntas sobre <em>{name}</em>',
        'faq_generic': [
            ('¿Me atiendes en español en {name}?',
             'Sí. Te acompaño en español o en inglés en todo el proceso: búsqueda, visitas, oferta, negociación, inspecciones y cierre.'),
            ('¿Cuánto vale mi casa en {name}?',
             'Depende del barrio, el tamaño y el estado de la casa. Escríbeme por WhatsApp y te preparo un análisis comparativo de mercado (CMA) con ventas recientes cerca de tu casa.'),
        ],
        'near_h': 'Ciudades cercanas',
        'contact_h': 'Hablemos de tu casa en <em>{name}</em>',
        'wa_text': 'Hola Alejandra, vi tu página de {name} y me gustaría más información.',
        'credit': 'Foto de portada', 'adapted': 'recortada', 'via': 'vía Wikimedia Commons',
        'hub_title': 'Áreas que atiendo en el Bay Area | Alejandra Granillo',
        'hub_desc': 'Realtor que habla español en Oakland, San Francisco, Concord, Walnut Creek, Pittsburg, Antioch, Brentwood, Richmond, Hayward y San Leandro. Elige tu ciudad.',
        'hub_eyebrow': 'Bay Area, California', 'hub_h1': 'Áreas que <b>atiendo</b>',
        'hub_lead': 'Trabajo con compradores, vendedores e inversionistas en todo el Bay Area. Elige tu ciudad para ver sus barrios, transporte y cómo te puedo ayudar ahí.',
        'hub_more': 'Ver {name}', 'hub_wa': 'Hola Alejandra, vi tu página web y me gustaría más información.',
        'hub_contact_h': 'Hablemos de tu <em>próximo paso</em>',
        'hub_alt': 'El Golden Gate y la bahía de San Francisco',
    },
    'en': {
        'home': 'Home', 'areas': 'Areas', 'all_areas': 'See all areas',
        'menu_label': 'Areas I serve',
        'title': 'Bilingual Realtor in {name}, CA | Alejandra Granillo',
        'eyebrow': 'Bilingual real estate agent · {county}',
        'h1': 'Realtor in <b>{name}</b>, CA',
        'btn_wa': 'Message me on WhatsApp', 'btn_hoods': 'See neighborhoods',
        'intro_eye': 'About {name}', 'intro_h': 'Buying and selling in <em>{name}</em>',
        'facts_h': 'Quick facts',
        'hoods_eye': 'Neighborhoods', 'hoods_h': '{name} <em>neighborhoods</em>',
        'why_eye': 'Why {name}?', 'why_h': 'What makes <em>{name}</em> attractive',
        'svc_h': 'How I can help in <em>{name}</em>',
        'work_eye': 'Portfolio', 'work_h_city': 'My sales in <em>{name}</em>',
        'work_h': 'Recent work in the <em>Bay Area</em>', 'work_more': 'See full portfolio',
        'sold': 'Sold',
        'faq_eye': 'FAQ', 'faq_h': 'Questions about <em>{name}</em>',
        'faq_generic': [
            ('Can you help me in Spanish in {name}?',
             'Yes. I work with you in English or Spanish through the whole process: search, showings, offer, negotiation, inspections and closing.'),
            ("What's my home worth in {name}?",
             "It depends on the neighborhood, size and condition of the home. Message me on WhatsApp and I'll prepare a comparative market analysis (CMA) with recent sales near you."),
        ],
        'near_h': 'Nearby cities',
        'contact_h': "Let's talk about your home in <em>{name}</em>",
        'wa_text': "Hi Alejandra, I saw your {name} page and I'd like more information.",
        'credit': 'Cover photo', 'adapted': 'cropped', 'via': 'via Wikimedia Commons',
        'hub_title': 'Areas I Serve in the Bay Area | Alejandra Granillo',
        'hub_desc': 'Bilingual Realtor in Oakland, San Francisco, Concord, Walnut Creek, Pittsburg, Antioch, Brentwood, Richmond, Hayward and San Leandro. Choose your city.',
        'hub_eyebrow': 'Bay Area, California', 'hub_h1': 'Areas I <b>serve</b>',
        'hub_lead': 'I work with buyers, sellers and investors across the Bay Area. Choose your city to see its neighborhoods, transit and how I can help there.',
        'hub_more': 'See {name}', 'hub_wa': "Hi Alejandra, I saw your website and I'd like more information.",
        'hub_contact_h': "Let's talk about your <em>next step</em>",
        'hub_alt': 'The Golden Gate Bridge and San Francisco Bay',
    },
}

# ------------------------------------------------- dropdown + home city pins

AREAS_CSS = '''/* Áreas dropdown (generated by scripts/build.py) */
.nav-dd{position:relative;}
.nav-dd-btn{display:flex;align-items:center;gap:6px;background:none;border:none;padding:8px 0;cursor:pointer;font-family:inherit;font-size:11px;font-weight:500;letter-spacing:0.14em;text-transform:uppercase;color:rgba(250,246,240,0.55);transition:color 0.2s;}
.nav-dd-btn:hover,.nav-dd.open .nav-dd-btn{color:var(--gold2);}
.nav-dd-caret{transition:transform 0.25s;}
.nav-dd.open .nav-dd-caret{transform:rotate(180deg);}
.nav-dd-menu{position:absolute;top:calc(100% + 14px);right:-28px;display:none;grid-template-columns:repeat(2,minmax(180px,1fr));gap:0 36px;padding:26px 30px 20px;background:rgba(10,21,37,0.98);border:1px solid rgba(201,168,76,0.18);box-shadow:0 24px 60px rgba(0,0,0,0.45);}
.nav-dd-menu::before{content:'';position:absolute;left:0;right:0;top:-18px;height:18px;}
.nav-dd.open .nav-dd-menu{display:grid;}
.nav-dd-col{display:flex;flex-direction:column;}
.nav-dd-h{font-family:'DM Mono',monospace;font-size:9.5px;letter-spacing:0.18em;text-transform:uppercase;color:var(--gold);margin:14px 0 6px;}
.nav-dd-col .nav-dd-h:first-child{margin-top:0;}
.nav-dd-menu a{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:400;line-height:1.25;color:#FAF6F0;text-decoration:none;padding:4px 0;transition:color 0.2s;}
.nav-dd-menu a:hover,.nav-dd-menu a[aria-current]{color:var(--gold2);}
.nav-dd-menu a.nav-dd-all{grid-column:1/-1;margin-top:16px;padding-top:14px;border-top:1px solid rgba(201,168,76,0.15);font-family:'DM Sans',system-ui,sans-serif;font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold);}
@media(hover:hover) and (min-width:901px){.nav-dd:hover .nav-dd-menu{display:grid;}.nav-dd:hover .nav-dd-btn{color:var(--gold2);}}
@media(max-width:900px){
  .nav-dd{position:static;}
  .nav-dd-menu{position:fixed;top:calc(72px + env(safe-area-inset-top,0px));left:0;right:0;grid-template-columns:1fr 1fr;gap:0 20px;padding:22px 24px 24px;max-height:calc(100vh - 72px);overflow:auto;border-left:none;border-right:none;background:#0A1525;}
  .nav-dd-menu::before{display:none;}
}
@media(max-width:480px){.nav-cta span{display:none;}.nav-cta{padding:11px 13px;}}
a.area-pin{text-decoration:none;transition:border-color 0.2s,color 0.2s,background 0.2s;}
a.area-pin:hover{border-color:var(--gold);color:var(--gold2);background:rgba(201,168,76,0.08);}'''

AREAS_JS = '''<script>
/* Áreas dropdown (generated by scripts/build.py) */
(function(){
  var dd=document.getElementById('navAreas');if(!dd)return;
  var btn=dd.querySelector('.nav-dd-btn');
  function set(o){dd.classList.toggle('open',o);btn.setAttribute('aria-expanded',o?'true':'false');}
  btn.addEventListener('click',function(e){e.stopPropagation();set(!dd.classList.contains('open'));});
  document.addEventListener('click',function(e){if(!dd.contains(e.target))set(false);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&dd.classList.contains('open')){set(false);btn.focus();}});
})();
</script>'''

CARET = '<svg class="nav-dd-caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'


def city_url(lang, slug):
    return f'{pre(lang)}/areas/{slug}/'


def nav_areas(lang):
    t = UI[lang]
    cols = []
    for counties in (MENU[:1] + MENU[2:], MENU[1:2]):  # Alameda + SF | Contra Costa
        parts = []
        for county, slugs in counties:
            parts.append(f'<span class="nav-dd-h">{esc(COUNTIES[county][lang])}</span>')
            parts += [f'<a href="{city_url(lang, s)}">{esc(BY_SLUG[s]["name"])}</a>' for s in slugs]
        cols.append('<div class="nav-dd-col">' + ''.join(parts) + '</div>')
    return (f'<div class="nav-dd" id="navAreas">'
            f'<button class="nav-dd-btn" type="button" aria-expanded="false" aria-controls="ddAreas">{t["areas"]}{CARET}</button>'
            f'<div class="nav-dd-menu" id="ddAreas" role="region" aria-label="{attr(t["menu_label"])}">'
            + ''.join(cols)
            + f'<a class="nav-dd-all" href="{pre(lang)}/areas/">{esc(t["all_areas"])} &rarr;</a></div></div>')


def area_pins(lang):
    pins = [f'<a class="area-pin" href="{city_url(lang, s)}"><span class="area-pin-dot"></span>{esc(BY_SLUG[s]["name"])}</a>'
            for _, slugs in MENU for s in slugs]
    pins += [f'<span class="area-pin"><span class="area-pin-dot"></span>{esc(n)}</span>' for n in EXTRA_PINS]
    return '\n'.join('      ' + p for p in pins)


def fill_home(s, lang):
    s = fill(s, 'areas-nav', nav_areas(lang))
    s = fill(s, 'areas-pins', area_pins(lang))
    s = fill(s, 'areas-css', AREAS_CSS, css=True)
    return fill(s, 'areas-js', AREAS_JS)


def refresh_home_jsonld(s):
    m = re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)', s, re.S)
    data = json.loads(m.group(2))
    agent = next(n for n in data['@graph'] if n['@type'] == 'RealEstateAgent')
    agent['areaServed'] = (
        [{'@type': 'City', 'name': f'{c["name"]}, CA'} for c in CITIES]
        + [{'@type': 'City', 'name': f'{n}, CA'} for n in EXTRA_PINS]
        + [{'@type': 'AdministrativeArea', 'name': 'San Francisco Bay Area'}])
    return s[:m.start(2)] + json.dumps(data, indent=2, ensure_ascii=False) + s[m.end(2):]


# ------------------------------------------------------- English home page

EN_TEXT = {
    'nav_about': 'About', 'nav_portfolio': 'Portfolio', 'nav_services': 'Services', 'nav_cta': 'Contact',
    'hero_tag': 'Real Estate Agent · Bay Area, California',
    'hero_tl1': 'Your strategic ally for buying & selling in the Bay Area.',
    'hero_tl2': 'Specialist in investments and Fix & Flip properties.',
    'hero_tl3': 'Personalized service in Spanish and English.',
    'hero_tl4': 'Your ally to buy, sell and invest with confidence.',
    'hero_pill1': '8+ Years', 'hero_pill2': 'Bay Area', 'hero_pill3': 'ES / EN',
    'hero_btn1': "Let's talk now",
    'stat_l1': 'Years of experience', 'stat_l4': 'Average rating',
    'about_eye': 'About me',
    'about_p1': "I'm Alejandra Granillo, a licensed real estate agent with deep knowledge of the Bay Area market. My mission is to guide you every step of the way—whether you're buying your first home, selling a property, or looking for solid investment opportunities.",
    'about_p2': 'With years of experience in the local market, I understand the unique complexities and opportunities of this region. I offer you strategy, honesty, and personalized service that turns a major decision into a successful experience.',
    'about_q': '“My commitment is to find you not just a property, but the right opportunity at the right time.”',
    'port_eye': 'Portfolio', 'port_hint': 'Tap to view details', 'modal_ask': 'Ask about this property',
    'svc_eye': 'Services',
    'svc_t1': 'Home Buying & Selling',
    'svc_d1': 'I represent you with strategy and dedication in every negotiation—from finding the ideal home to closing, maximizing your investment or sale price.',
    'svc_cta': 'Contact',
    'svc_t2': 'Investment Management',
    'svc_d2': 'For investors seeking returns: I identify, evaluate, and manage high-potential properties across the Bay Area with a long-term strategic vision.',
    'svc_t3': 'Fix & Flip',
    'svc_d3': 'Specialist in renovation and resale opportunities. I help you find properties with potential, calculate ROI, and coordinate the entire process from start to finish.',
    'area_eye': 'Coverage',
    'area_desc': 'I operate throughout the Bay Area with deep knowledge of the local market, providing strategic advantage in every transaction.',
    'contact_eye': 'Contact',
    'contact_p': "Ready to buy, sell, or invest? Message me on WhatsApp and I'll assist you personally, in Spanish or English.",
    'btn_sms': 'Send message', 'btn_call': 'Call now',
}
EN_HTML = {
    'about_h': 'Meet your <em>agent</em>',
    'svc_h': 'How I can <em>help you</em>',
    'contact_h': "Let's talk about your <em>next step</em>",
}
EN_TITLE = 'Alejandra Granillo | Bilingual Realtor in Oakland &amp; Bay Area'
EN_DESC = ('Bilingual Bay Area Realtor (English &amp; Spanish): buying, selling, investments and '
           'Fix &amp; Flip in Oakland, San Francisco and San Jose. Message me on WhatsApp.')
# (spanish, english, expected count): text with no data-t key, head tags, toggle state
EN_LITERAL = [
    ('<html lang="es">', '<html lang="en">', 1),
    ('<head>\n', '<head>\n<!-- Generated by scripts/build.py from index.html. Do not edit by hand. -->\n', 1),
    ('<title>Alejandra Granillo | Realtor bilingüe en Oakland y Bay Area</title>', f'<title>{EN_TITLE}</title>', 1),
    ('content="Alejandra Granillo | Realtor bilingüe en Oakland y Bay Area"', f'content="{EN_TITLE}"', 1),
    ('content="Realtor que habla español en el Bay Area: compra, venta, inversiones y Fix &amp; Flip en Oakland, San Francisco y San Jose. Escríbeme por WhatsApp."', f'content="{EN_DESC}"', 2),
    (f'<link rel="canonical" href="{SITE}/">', f'<link rel="canonical" href="{SITE}/en/">', 1),
    (f'<meta property="og:url" content="{SITE}/">', f'<meta property="og:url" content="{SITE}/en/">', 1),
    ('<meta property="og:locale" content="es_US">\n<meta property="og:locale:alternate" content="en_US">',
     '<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="es_US">', 1),
    ('img/og-alejandra-granillo.jpg', 'img/og-alejandra-granillo-en.jpg', 1),
    ('content="Alejandra Granillo, Realtor en el Bay Area, California"', 'content="Alejandra Granillo, Realtor in the Bay Area, California"', 1),
    ('"description": "Agente de bienes raíces bilingüe (español e inglés) en el Bay Area: compra y venta de casas, inversiones y Fix & Flip."',
     '"description": "Bilingual (English and Spanish) real estate agent in the Bay Area: home buying and selling, investments and Fix & Flip."', 1),
    ('<a class="lang-btn active" href="/" hreflang="es" aria-current="page">ES</a>', '<a class="lang-btn" href="/" hreflang="es" lang="es">ES</a>', 1),
    ('<a class="lang-btn" href="/en/" hreflang="en" lang="en">EN</a>', '<a class="lang-btn active" href="/en/" hreflang="en" aria-current="page">EN</a>', 1),
    ('aria-label="Men&#250;"', 'aria-label="Menu"', 1),
    ('aria-label="Contactar por WhatsApp"', 'aria-label="Contact on WhatsApp"', 1),
    ('>Ver portafolio <svg', '>View portfolio <svg', 1),
    ('<span class="stat-l">En toda el Área de la Bahía</span>', '<span class="stat-l">All over the Bay Area</span>', 1),
    ('<span class="stat-l">Español e inglés</span>', '<span class="stat-l">Spanish &amp; English</span>', 1),
    ('alt="Alejandra Granillo, Realtor en el Bay Area"', 'alt="Alejandra Granillo, Bay Area Realtor"', 1),
    ('<h2 class="dh light">Propiedades <em>cerradas</em></h2>', '<h2 class="dh light">Closed <em>properties</em></h2>', 1),
    ('<span class="pc-type">Residencial</span>', '<span class="pc-type">Residential</span>', 2),
    ('</svg> Ver detalles</div>', '</svg> View details</div>', 5),
    ('aria-label="Detalle de propiedad"', 'aria-label="Property details"', 1),
    ('aria-label="Cerrar"', 'aria-label="Close"', 1),
]


def build_home_en(es):
    s = es
    for a, b, n in EN_LITERAL:
        assert s.count(a) == n, f'expected {n}x: {a[:70]!r} (found {s.count(a)})'
        s = s.replace(a, b)

    def swap(attr_name, key, value):
        nonlocal s
        pat = re.compile(r'(<(\w+)\b[^>]*\s' + attr_name + r'="' + key + r'"[^>]*>)(.*?)(</\2>)', re.S)
        s, n = pat.subn(lambda m: m.group(1) + value + m.group(4), s)
        assert n, f'{attr_name}="{key}" not found in index.html'

    for key, value in EN_TEXT.items():
        swap('data-t', key, esc(value))
    for key, value in EN_HTML.items():
        swap('data-t-html', key, value)
    missing = set(re.findall(r'data-t(?:-html)?="(\w+)"', s)) - set(EN_TEXT) - set(EN_HTML)
    assert not missing, f'no English for: {sorted(missing)}'
    return fill_home(s, 'en')


# ------------------------------------------------- pieces shared with home

class Pieces:
    """Chunks lifted from a built home page (ES or EN) for the city pages."""

    def __init__(self, home, lang):
        self.lang = lang
        self.head = between(home, '<!-- Meta Pixel', '<style>', include=False)
        self.head = '<!-- Meta Pixel' + self.head
        self.style = between(home, '<style>', '</style>')
        self.noscript = between(home, '<noscript>', '</noscript>')
        self.wa = between(home, '<a href="https://wa.me/14154239973" class="wa"', '</a>')
        self.nav = between(home, '<nav id="nav">', '</nav>')
        self.services = between(home, '<section class="services" id="servicios">', '\n</section>')
        self.contact = between(home, '<section class="contact">', '\n</section>')
        self.footer = between(home, '<footer>', '</footer>')
        self.areas_js = AREAS_JS

    def nav_for(self, es_url, en_url, current=None):
        p = pre(self.lang)
        n = self.nav
        for a, b in [('href="#" class="nav-logo"', f'href="{p}/" class="nav-logo"'),
                     ('href="#sobre-mi"', f'href="{p}/#sobre-mi"'),
                     ('href="#portafolio"', f'href="{p}/#portafolio"'),
                     ('href="#servicios"', f'href="{p}/#servicios"'),
                     ('href="/" hreflang="es"', f'href="{es_url}" hreflang="es"'),
                     ('href="/en/" hreflang="en"', f'href="{en_url}" hreflang="en"')]:
            assert n.count(a) == 1, a
            n = n.replace(a, b)
        if current:
            a = f'<a href="{current}">'
            assert n.count(a) == 1, a
            n = n.replace(a, f'<a href="{current}" aria-current="page">')
        return n


def wa_link(text):
    return f'{WA}?text={urllib.parse.quote(text)}'


def with_wa(chunk, text):
    """Point every plain WhatsApp link in a chunk at a prefilled message."""
    return chunk.replace(f'href="{WA}"', f'href="{wa_link(text)}"')


# ---------------------------------------------------------------- page CSS

PAGE_CSS = '''/* City + areas pages (generated by scripts/build.py) */
.city-hero{position:relative;min-height:78vh;display:flex;align-items:flex-end;background:#050d1a;overflow:hidden;}
.city-hero-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(0.55) contrast(1.05) saturate(0.9);}
.city-hero-c{position:relative;z-index:2;width:100%;max-width:1300px;margin:0 auto;padding:150px 52px 88px;}
/* the home styles every <nav> as the fixed top bar; undo that for breadcrumbs */
.crumbs-nav{position:static;inset:auto;z-index:auto;height:auto;padding:0;display:block;background:none;box-shadow:none;}
.crumbs{display:flex;flex-wrap:wrap;gap:8px;font-family:'DM Mono',monospace;font-size:10px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(250,246,240,0.4);margin:0 0 24px;padding:0;list-style:none;}
.crumbs li+li::before{content:'/';margin-right:8px;color:rgba(250,246,240,0.3);}
.crumbs a{color:rgba(250,246,240,0.7);text-decoration:none;}
.crumbs a:hover{color:var(--gold2);}
.crumbs [aria-current]{color:var(--gold);}
.city-h1{font-family:'Cormorant Garamond',serif;font-size:clamp(46px,7.4vw,104px);font-weight:300;line-height:0.95;color:#FAF6F0;margin:0 0 26px;letter-spacing:-0.02em;opacity:0;animation:fadeUp 0.9s 0.45s forwards;}
.city-h1 b{font-weight:600;font-style:italic;color:var(--gold);}
.city-lead{max-width:660px;font-size:clamp(16px,1.5vw,19px);font-weight:300;line-height:1.75;color:rgba(250,246,240,0.78);margin:0 0 40px;opacity:0;animation:fadeUp 0.9s 0.7s forwards;}
.city-sec{padding:120px 0;}
.city-in{max-width:1300px;margin:0 auto;padding:0 52px;}
.city-intro{background:#F7F4EF;}
.city-grid{display:grid;grid-template-columns:1.35fr 1fr;gap:80px;align-items:start;}
.city-p{font-size:16.5px;line-height:1.9;color:#5A6B80;margin:28px 0 0;}
.facts{background:#0A1525;padding:40px 40px 36px;border-top:2px solid var(--gold);}
.facts-h{font-family:'DM Mono',monospace;font-size:10px;font-weight:500;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold);margin:0 0 24px;}
.facts dl{margin:0;display:grid;gap:20px;}
.facts dt{font-family:'DM Mono',monospace;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(250,246,240,0.45);margin:0 0 5px;}
.facts dd{margin:0;font-size:15px;line-height:1.6;color:rgba(250,246,240,0.9);}
.city-hoods{background:#FFFFFF;}
.hood-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:56px;}
.hood{background:#F7F4EF;border:1px solid #E5E0D8;padding:32px 30px;}
.hood h3{font-family:'Cormorant Garamond',serif;font-size:27px;font-weight:400;line-height:1.15;color:#0A1525;margin:0 0 12px;}
.hood p{font-size:14.5px;line-height:1.75;color:#5A6B80;margin:0;}
.city-why{background:#0A1525;}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:56px;margin-top:56px;}
.why-n{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:0.2em;color:var(--gold);}
.why h3{font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:300;color:#FAF6F0;margin:14px 0 12px;}
.why p{font-size:15px;line-height:1.85;color:rgba(250,246,240,0.62);margin:0;}
.city-work{background:#050D1A;}
.work-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:48px;}
.work-card{position:relative;display:block;overflow:hidden;aspect-ratio:3/4;text-decoration:none;background:#0A1525;}
.work-card img{width:100%;height:100%;object-fit:cover;display:block;filter:brightness(0.78);transition:transform 0.7s cubic-bezier(0.25,0.46,0.45,0.94),filter 0.5s;}
.work-card:hover img{transform:scale(1.05);filter:brightness(0.6);}
.work-info{position:absolute;left:0;right:0;bottom:0;padding:26px 22px 22px;background:linear-gradient(to top,rgba(5,13,26,0.94),rgba(5,13,26,0));}
.work-badge{display:inline-block;font-family:'DM Mono',monospace;font-size:9.5px;letter-spacing:0.18em;text-transform:uppercase;background:var(--gold);color:#0A1525;padding:4px 10px;}
.work-addr{display:block;font-family:'Cormorant Garamond',serif;font-size:23px;color:#FAF6F0;margin:12px 0 4px;}
.work-meta{display:block;font-family:'DM Mono',monospace;font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(250,246,240,0.55);}
.work-price{display:block;font-family:'Cormorant Garamond',serif;font-size:19px;color:var(--gold2);margin-top:6px;}
.work-more{margin-top:40px;}
.city-faq{background:#F7F4EF;}
.faq-list{margin-top:48px;border-top:1px solid #E5E0D8;max-width:920px;}
.faq-list details{border-bottom:1px solid #E5E0D8;padding:24px 0;}
.faq-list summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:baseline;gap:24px;font-family:'Cormorant Garamond',serif;font-size:25px;line-height:1.3;color:#0A1525;}
.faq-list summary::-webkit-details-marker{display:none;}
.faq-list summary::after{content:'+';flex-shrink:0;font-family:'DM Sans',system-ui,sans-serif;font-size:24px;font-weight:300;color:var(--gold);transition:transform 0.3s;}
.faq-list details[open] summary::after{transform:rotate(45deg);}
.faq-list p{font-size:15.5px;line-height:1.85;color:#5A6B80;margin:14px 0 0;max-width:820px;}
.near{margin-top:88px;}
.near-h{font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:300;color:#0A1525;margin:0;}
.near .area-pins{justify-content:flex-start;margin-top:24px;gap:12px;}
.near .area-pin{color:#0A1525;border-color:rgba(201,168,76,0.6);}
.near a.area-pin:hover{color:#0A1525;background:rgba(201,168,76,0.14);}
.hub-county{margin-top:72px;}
.hub-county:first-child{margin-top:0;}
.hub-county-h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:var(--gold);margin:0 0 24px;font-weight:500;}
.hub-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
.hub-card{display:flex;flex-direction:column;text-decoration:none;background:#FFFFFF;border:1px solid #E5E0D8;overflow:hidden;transition:border-color 0.25s,transform 0.25s,box-shadow 0.25s;}
.hub-card:hover{border-color:var(--gold);transform:translateY(-3px);box-shadow:0 18px 40px rgba(10,21,37,0.08);}
.hub-card img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block;}
.hub-card-b{padding:26px 26px 24px;display:flex;flex-direction:column;flex:1;}
.hub-card h3{font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:400;color:#0A1525;margin:0 0 10px;}
.hub-card p{font-size:14.5px;line-height:1.7;color:#5A6B80;margin:0 0 20px;flex:1;}
.hub-go{font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold);}
.credit{max-width:1300px;margin:14px auto 0;font-size:11px;line-height:1.6;color:#9AAABB;}
.credit a{color:inherit;}
@media(max-width:900px){
  .city-hero{min-height:74vh;}
  .city-hero-c{padding:128px 24px 64px;}
  .city-sec{padding:80px 0;}
  .city-in{padding:0 24px;}
  .city-grid{grid-template-columns:1fr;gap:48px;}
  .hood-grid,.hub-grid{grid-template-columns:1fr 1fr;}
  .why-grid{grid-template-columns:1fr;gap:36px;}
}
@media(max-width:600px){
  .hood-grid,.hub-grid{grid-template-columns:1fr;}
  .facts{padding:30px 24px;}
  .faq-list summary{font-size:22px;}
  .work-grid{grid-template-columns:1fr 1fr;gap:10px;}
  .work-info{padding:18px 14px 14px;}
  .work-addr{font-size:19px;}
  .near-h{font-size:28px;}
}'''

PAGE_JS = '''<script>
(function(){
  var nav=document.getElementById('nav'),bar=document.getElementById('prog');
  function onScroll(){
    nav.classList.toggle('up',window.scrollY>60);
    var max=document.documentElement.scrollHeight-window.innerHeight;
    if(bar)bar.style.width=(max>0?window.scrollY/max*100:0)+'%';
  }
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
})();
</script>'''

WA_ICON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'
LEAD = "onclick=\"if(typeof fbq!=='undefined')fbq('track','Lead')\""


def head(lang, pieces, *, title, desc, url, es_url, en_url, preload, ld):
    og = f'{SITE}/img/og-alejandra-granillo{"" if lang == "es" else "-en"}.jpg'
    loc, alt_loc = ('es_US', 'en_US') if lang == 'es' else ('en_US', 'es_US')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<!-- Generated by scripts/build.py from scripts/areas.py. Do not edit by hand. -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{attr(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{SITE}{url}">
<link rel="alternate" hreflang="es" href="{SITE}{es_url}">
<link rel="alternate" hreflang="en" href="{SITE}{en_url}">
<link rel="alternate" hreflang="x-default" href="{SITE}{es_url}">
<meta name="theme-color" content="#0A1525">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Alejandra Granillo Real Estate">
<meta property="og:locale" content="{loc}">
<meta property="og:locale:alternate" content="{alt_loc}">
<meta property="og:url" content="{SITE}{url}">
<meta property="og:title" content="{attr(title)}">
<meta property="og:description" content="{attr(desc)}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" as="image" href="{preload}" fetchpriority="high">
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
{pieces.head}{pieces.style}
<style>
{PAGE_CSS}
</style>
</head>
<body>
{pieces.noscript}

<div id="prog"></div>
'''


def agent_node(lang):
    return {
        '@type': 'RealEstateAgent', '@id': f'{SITE}/#agent', 'name': 'Alejandra Granillo',
        'url': f'{SITE}{pre(lang)}/', 'telephone': '+1-415-423-9973',
        'image': f'{SITE}/img/alejandra-granillo-realtor.webp',
        'knowsLanguage': ['es', 'en'],
        'areaServed': [{'@type': 'City', 'name': f'{c["name"]}, CA'} for c in CITIES],
        'sameAs': ['https://www.facebook.com/alejandra.granillo.615305',
                   'https://www.instagram.com/alejandra__granillo/'],
    }


def crumbs(lang, items):
    """items: [(name, url or None)]; last item is the current page."""
    li = []
    for name, url in items:
        li.append(f'<li><a href="{url}">{esc(name)}</a></li>' if url
                  else f'<li><span aria-current="page">{esc(name)}</span></li>')
    label = 'Ruta de navegación' if lang == 'es' else 'Breadcrumb'
    return f'<nav class="crumbs-nav" aria-label="{label}"><ol class="crumbs">{"".join(li)}</ol></nav>'


def eye(text, center=False):
    style = ' style="justify-content:center"' if center else ''
    return f'<div class="eye"{style}><span class="eye-line"></span><span class="eye-txt">{esc(text)}</span></div>'


def footer_with_credit(pieces, lang, photo):
    if not photo:
        return pieces.footer
    t = UI[lang]
    lic = (f'<a href="{photo["license_url"]}" rel="license noopener" target="_blank">{esc(photo["license"])}</a>'
           if photo['license_url'] else esc(photo['license']))
    credit = (f'<p class="credit">{t["credit"]}: <a href="{photo["source"]}" rel="noopener" target="_blank">{esc(photo["author"])}</a>'
              f' · {lic} ({t["adapted"]}), {t["via"]}.</p>')
    return pieces.footer.replace('</div></footer>', '</div>' + credit + '</footer>')


def city_page(lang, c, pieces):
    t, d, name = UI[lang], c[lang], c['name']
    county = COUNTIES[c['county']][lang]
    url, es_url, en_url = city_url(lang, c['slug']), city_url('es', c['slug']), city_url('en', c['slug'])
    title = t['title'].format(name=name)
    wa_text = t['wa_text'].format(name=name)
    img = f'/img/areas/{c["photo"]["file"]}'
    faqs = [(q.format(name=name), a) for q, a in t['faq_generic']] + d['faq']

    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': f'{SITE}{url}#webpage', 'url': f'{SITE}{url}', 'name': title,
         'description': d['desc'], 'inLanguage': lang, 'isPartOf': {'@id': f'{SITE}/#website'},
         'primaryImageOfPage': f'{SITE}{img}',
         'about': {'@type': 'City', 'name': name,
                   'containedInPlace': {'@type': 'AdministrativeArea', 'name': f'{COUNTIES[c["county"]]["en"]}, California'}},
         'breadcrumb': {'@id': f'{SITE}{url}#breadcrumb'}, 'provider': {'@id': f'{SITE}/#agent'}},
        {'@type': 'BreadcrumbList', '@id': f'{SITE}{url}#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': t['home'], 'item': f'{SITE}{pre(lang)}/'},
            {'@type': 'ListItem', 'position': 2, 'name': t['areas'], 'item': f'{SITE}{pre(lang)}/areas/'},
            {'@type': 'ListItem', 'position': 3, 'name': name, 'item': f'{SITE}{url}'}]},
        agent_node(lang),
        {'@type': 'FAQPage', '@id': f'{SITE}{url}#faq', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs]},
    ]}

    out = [head(lang, pieces, title=title, desc=d['desc'], url=url, es_url=es_url, en_url=en_url, preload=img, ld=ld)]
    out.append(with_wa(pieces.wa, wa_text))
    out.append(with_wa(pieces.nav_for(es_url, en_url, current=url), wa_text))

    out.append(f'''
<header class="city-hero">
  <img class="city-hero-img" src="{img}" alt="{attr(d['alt'])}" fetchpriority="high">
  <div class="hero-veil"></div>
  <div class="city-hero-c">
    {crumbs(lang, [(t['home'], pre(lang) + '/'), (t['areas'], pre(lang) + '/areas/'), (name, None)])}
    <div class="hero-tag"><span class="hero-dot"></span><span class="hero-tag-text">{esc(t['eyebrow'].format(county=county))}</span></div>
    <h1 class="city-h1">{t['h1'].format(name=esc(name))}</h1>
    <p class="city-lead">{esc(d['lead'])}</p>
    <div class="hero-btns">
      <a href="{wa_link(wa_text)}" class="btn-g" target="_blank" rel="noopener" {LEAD}>{WA_ICON}<span>{esc(t['btn_wa'])}</span></a>
      <a href="#barrios" class="btn-o">{esc(t['btn_hoods'])} <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg></a>
    </div>
  </div>
</header>

<section class="city-sec city-intro">
  <div class="city-in city-grid">
    <div>
      {eye(t['intro_eye'].format(name=name))}
      <h2 class="dh">{t['intro_h'].format(name=esc(name))}</h2>
      {''.join(f'<p class="city-p">{esc(p)}</p>' for p in d['intro'])}
    </div>
    <aside class="facts">
      <p class="facts-h">{esc(t['facts_h'])}</p>
      <dl>{''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in d['facts'])}</dl>
    </aside>
  </div>
</section>

<section class="city-sec city-hoods" id="barrios">
  <div class="city-in">
    {eye(t['hoods_eye'])}
    <h2 class="dh">{t['hoods_h'].format(name=esc(name))}</h2>
    <div class="hood-grid">
      {''.join(f'<article class="hood"><h3>{esc(h)}</h3><p>{esc(p)}</p></article>' for h, p in d['hoods'])}
    </div>
  </div>
</section>

<section class="city-sec city-why">
  <div class="city-in">
    {eye(t['why_eye'].format(name=name))}
    <h2 class="dh light">{t['why_h'].format(name=esc(name))}</h2>
    <div class="why-grid">
      {''.join(f'<div class="why"><span class="why-n">0{i}</span><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for i, (h, p) in enumerate(d['why'], 1))}
    </div>
  </div>
</section>
''')

    svc = with_wa(pieces.services, wa_text)
    svc, n = re.subn(r'<h2 class="dh" data-t-html="svc_h">.*?</h2>',
                     f'<h2 class="dh">{t["svc_h"].format(name=esc(name))}</h2>', svc)
    assert n == 1
    out.append(svc.replace(' id="servicios"', ''))

    work = c.get('work') or RECENT
    work_h = t['work_h_city'] if c.get('work') else t['work_h']
    cards = []
    for key in work:
        p = PROPERTIES[key]
        cards.append(
            f'<a class="work-card" href="{pre(lang)}/#portafolio">'
            f'<img src="/img/{p["img"]}" alt="{attr(p["addr"] + ", " + p["city"])}" loading="lazy" decoding="async">'
            f'<span class="work-info"><span class="work-badge">{esc(t["sold"])}</span>'
            f'<span class="work-addr">{esc(p["addr"])}</span>'
            f'<span class="work-meta">{esc(p["city"])} · {esc(p["type"][lang])}</span>'
            f'<span class="work-price">{esc(p["price"])}</span></span></a>')
    out.append(f'''
<section class="city-sec city-work">
  <div class="city-in">
    {eye(t['work_eye'])}
    <h2 class="dh light">{work_h.format(name=esc(name))}</h2>
    <div class="work-grid">{''.join(cards)}</div>
    <a href="{pre(lang)}/#portafolio" class="btn-o work-more">{esc(t['work_more'])}</a>
  </div>
</section>

<section class="city-sec city-faq">
  <div class="city-in">
    {eye(t['faq_eye'])}
    <h2 class="dh">{t['faq_h'].format(name=esc(name))}</h2>
    <div class="faq-list">
      {''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs)}
    </div>
    <div class="near">
      <h2 class="near-h">{esc(t['near_h'])}</h2>
      <div class="area-pins">
        {''.join(f'<a class="area-pin" href="{city_url(lang, s)}"><span class="area-pin-dot"></span>{esc(BY_SLUG[s]["name"])}</a>' for s in c['near'])}
        <a class="area-pin" href="{pre(lang)}/areas/"><span class="area-pin-dot"></span>{esc(t['all_areas'])}</a>
      </div>
    </div>
  </div>
</section>
''')

    contact = with_wa(pieces.contact, wa_text)
    contact, n = re.subn(r'<h2 class="dh" data-t-html="contact_h">.*?</h2>',
                         f'<h2 class="dh">{t["contact_h"].format(name=esc(name))}</h2>', contact)
    assert n == 1
    out.append(contact)
    out.append('\n' + footer_with_credit(pieces, lang, c['photo']) + '\n' + PAGE_JS + '\n' + pieces.areas_js + '\n</body>\n</html>\n')
    return ''.join(out)


def hub_page(lang, pieces):
    t = UI[lang]
    url, es_url, en_url = f'{pre(lang)}/areas/', '/areas/', '/en/areas/'
    img = '/img/bay-area-golden-gate.webp'
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CollectionPage', '@id': f'{SITE}{url}#webpage', 'url': f'{SITE}{url}', 'name': t['hub_title'],
         'description': t['hub_desc'], 'inLanguage': lang, 'isPartOf': {'@id': f'{SITE}/#website'},
         'breadcrumb': {'@id': f'{SITE}{url}#breadcrumb'}, 'provider': {'@id': f'{SITE}/#agent'},
         'hasPart': [{'@type': 'WebPage', 'url': f'{SITE}{city_url(lang, c["slug"])}', 'name': c['name']} for c in CITIES]},
        {'@type': 'BreadcrumbList', '@id': f'{SITE}{url}#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': t['home'], 'item': f'{SITE}{pre(lang)}/'},
            {'@type': 'ListItem', 'position': 2, 'name': t['areas'], 'item': f'{SITE}{url}'}]},
        agent_node(lang),
    ]}
    out = [head(lang, pieces, title=t['hub_title'], desc=t['hub_desc'], url=url, es_url=es_url, en_url=en_url, preload=img, ld=ld)]
    out.append(with_wa(pieces.wa, t['hub_wa']))
    out.append(pieces.nav_for(es_url, en_url))
    groups = []
    for county, slugs in MENU:
        cards = []
        for s in slugs:
            c = BY_SLUG[s]
            cards.append(
                f'<a class="hub-card" href="{city_url(lang, s)}">'
                f'<img src="/img/areas/{c["photo"]["file"]}" alt="{attr(c[lang]["alt"])}" loading="lazy" decoding="async">'
                f'<div class="hub-card-b"><h3>{esc(c["name"])}</h3><p>{esc(c[lang]["card"])}</p>'
                f'<span class="hub-go">{esc(t["hub_more"].format(name=c["name"]))} &rarr;</span></div></a>')
        groups.append(f'<div class="hub-county"><h2 class="hub-county-h">{esc(COUNTIES[county][lang])}</h2>'
                      f'<div class="hub-grid">{"".join(cards)}</div></div>')
    out.append(f'''
<header class="city-hero">
  <img class="city-hero-img" src="{img}" alt="{attr(t['hub_alt'])}" fetchpriority="high">
  <div class="hero-veil"></div>
  <div class="city-hero-c">
    {crumbs(lang, [(t['home'], pre(lang) + '/'), (t['areas'], None)])}
    <div class="hero-tag"><span class="hero-dot"></span><span class="hero-tag-text">{esc(t['hub_eyebrow'])}</span></div>
    <h1 class="city-h1">{t['hub_h1']}</h1>
    <p class="city-lead">{esc(t['hub_lead'])}</p>
  </div>
</header>

<section class="city-sec city-intro">
  <div class="city-in">
    {''.join(groups)}
  </div>
</section>
''')
    contact = with_wa(pieces.contact, t['hub_wa'])
    contact, n = re.subn(r'<h2 class="dh" data-t-html="contact_h">.*?</h2>',
                         f'<h2 class="dh">{t["hub_contact_h"]}</h2>', contact)
    assert n == 1
    out.append(contact)
    out.append('\n' + pieces.footer + '\n' + PAGE_JS + '\n' + pieces.areas_js + '\n</body>\n</html>\n')
    return ''.join(out)


# ------------------------------------------------------------------ sitemap

def sitemap(today):
    imgs = ['alejandra-granillo-realtor.webp', '2-hillcrest-ct-san-anselmo.webp', '672-27th-ave-oakland.webp',
            '2311-57th-ave-oakland.webp', '3228-hyde-st-oakland.webp', '5614-dover-st-oakland.webp']
    pages = [('/', '/en/', imgs), ('/areas/', '/en/areas/', [])]
    pages += [(city_url('es', c['slug']), city_url('en', c['slug']), ['areas/' + c['photo']['file']]) for c in CITIES]
    rows = []
    for es_url, en_url, images in pages:
        for loc in (es_url, en_url):
            img_xml = ''.join(f'\n    <image:image><image:loc>{SITE}/img/{i}</image:loc></image:image>'
                              for i in (images if loc == es_url else []))
            rows.append(f'''  <url>
    <loc>{SITE}{loc}</loc>
    <lastmod>{today}</lastmod>
    <xhtml:link rel="alternate" hreflang="es" href="{SITE}{es_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{es_url}"/>{img_xml}
  </url>''')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + '\n'.join(rows) + '\n</urlset>\n')


def main():
    es = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    es = refresh_home_jsonld(fill_home(es, 'es'))
    write('index.html', es)
    en = build_home_en(es)
    write('en/index.html', en)

    for lang, home in (('es', es), ('en', en)):
        pieces = Pieces(home, lang)
        for c in CITIES:
            write(city_url(lang, c['slug']).lstrip('/') + 'index.html', city_page(lang, c, pieces))
        write(f'{pre(lang)}/areas/index.html'.lstrip('/'), hub_page(lang, pieces))

    write('sitemap.xml', sitemap(datetime.date.today().isoformat()))
    print(f'built: index.html, en/index.html, {len(CITIES) * 2} city pages, 2 hubs, sitemap.xml')


if __name__ == '__main__':
    main()
