#!/usr/bin/env python3
"""Gera as páginas de produto da Ervena (/ervena-shampoo, /ervena-conditioner).

Textos de rótulo (INCI, modo de uso, avisos) vêm de ~/Documents/Ervena-Rotulos/_fonte/gen.py
e devem continuar iguais ao rótulo. Rode `python3 build.py` depois de editar.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

WARN = ("For external use only. Keep out of reach of children. Avoid contact with eyes; if contact occurs, "
        "rinse immediately with plenty of water. Discontinue use if irritation or redness develops.")
ALLERGY = ("Contains natural plant extracts and essential oils. Perform a patch test 24 hours prior to first use.")
FOOTNOTE = "*Naturally occurring components in essential oils and botanical extracts."

PRODUCTS = {
    'shampoo': dict(
        name='Shampoo',
        slug='ervena-shampoo',
        other='conditioner',
        tagline='Clarifying botanical cleanse',
        headline='A clean start, <em>rooted in nature.</em>',
        indications=("Designed for thorough cleansing, clarifying, and refreshing hair and scalp without "
                     "stripping essential moisture."),
        intro=("A gentle, plant-based shampoo that lifts away buildup with sugar-derived cleansers, while argan "
               "and jojoba oils, aloe and pro-vitamin B5 keep hair soft and balanced. Finished with a bright scent "
               "of mandarin and cardamom."),
        steps=["Apply a generous amount to wet hair.",
               "Gently massage the scalp and hair until a rich lather forms.",
               "Rinse thoroughly. Repeat if necessary.",
               "For best results, follow with Ervena Conditioner."],
        directions=("Apply a generous amount to wet hair, gently massage the scalp and hair until a rich lather "
                    "forms, then rinse thoroughly. Repeat if necessary. For best results, follow with Ervena "
                    "Conditioner."),
        key=[
            ('Gentle plant cleansers', 'Decyl &amp; Caprylyl/Capryl Glucoside',
             'Mild, plant-derived cleansers that create a soft lather and clean without a harsh feel.'),
            ('Argan oil', 'Argania Spinosa Kernel Oil',
             'A nourishing oil that helps leave hair soft, smooth and glossy.'),
            ('Jojoba oil', 'Simmondsia Chinensis Seed Oil',
             'A lightweight oil that helps keep the scalp feeling balanced and comfortable.'),
            ('Aloe vera', 'Aloe Barbadensis Leaf Extract',
             'Soothing and hydrating for scalp and lengths.'),
            ('Pro-vitamin B5', 'Panthenol',
             'Helps hair hold on to moisture for a fuller, healthier feel.'),
            ('Hibiscus &amp; green tea', 'Hibiscus Sabdariffa · Camellia Sinensis',
             'Botanical extracts rich in naturally occurring antioxidants.'),
            ('Mandarin &amp; cardamom', 'Citrus Reticulata · Elettaria Cardamomum',
             'Essential oils that give Ervena its fresh, warm citrus-spice scent.'),
        ],
        inci=("Aqua, Decyl Glucoside, Cocamidopropyl Betaine, Caprylyl/Capryl Glucoside, Glycerin, "
              "Leuconostoc/Radish Root Ferment Filtrate, Aloe Barbadensis Leaf Extract, Argania Spinosa Kernel "
              "Oil, Simmondsia Chinensis Seed Oil, Xanthan Gum, Panthenol, Tocopherol, Citrus Reticulata Peel "
              "Oil, Elettaria Cardamomum Seed Oil, Hibiscus Sabdariffa Flower Extract, Camellia Sinensis Leaf "
              "Extract, Citric Acid, Limonene*, Linalool*, Citral*, Geraniol*, Citronellol*."),
        upc='860016462045',
    ),
    'conditioner': dict(
        name='Conditioner',
        slug='ervena-conditioner',
        other='shampoo',
        tagline='Nourishing botanical conditioning',
        headline='Softness that <em>grows with every wash.</em>',
        indications=("Formulated to detangle, smooth, hydrate, and nourish hair fibers, enhancing softness and "
                     "manageability."),
        intro=("A rich, plant-based conditioner with shea butter, chamomile, argan and jojoba oils that melts into "
               "damp hair to detangle and smooth. Hair is left soft, manageable and lightly scented with mandarin "
               "and cardamom."),
        steps=["Cleanse with Ervena Shampoo.",
               "Apply evenly to damp hair, from mid-lengths to ends.",
               "Leave on for 2 to 3 minutes to allow deep conditioning.",
               "Rinse thoroughly."],
        directions=("After cleansing with Ervena Shampoo, apply evenly to damp hair from mid-lengths to ends. "
                    "Leave on for 2 to 3 minutes to allow deep conditioning, then rinse thoroughly."),
        key=[
            ('Shea butter', 'Butyrospermum Parkii Butter',
             'A creamy plant butter that wraps hair in softness and helps reduce dryness.'),
            ('Chamomile', 'Chamomilla Recutita Flower Extract',
             'A calming botanical traditionally used in gentle hair care.'),
            ('Argan oil', 'Argania Spinosa Kernel Oil',
             'A nourishing oil that helps smooth the hair surface and add shine.'),
            ('Jojoba oil', 'Simmondsia Chinensis Seed Oil',
             'A lightweight oil that conditions without weighing hair down.'),
            ('Aloe vera &amp; B5', 'Aloe Barbadensis · Panthenol',
             'Hydrating partners that help hair feel supple and manageable.'),
            ('Hibiscus &amp; green tea', 'Hibiscus Sabdariffa · Camellia Sinensis',
             'Botanical extracts rich in naturally occurring antioxidants.'),
            ('Mandarin &amp; cardamom', 'Citrus Reticulata · Elettaria Cardamomum',
             'Essential oils that give Ervena its fresh, warm citrus-spice scent.'),
        ],
        inci=("Aqua, Cetearyl Alcohol, Distearoylethyl Dimonium Chloride"
              ", Caprylic/Capric Triglyceride, Glycerin, Butyrospermum Parkii Butter, Chamomilla Recutita "
              "Flower Extract, Leuconostoc/Radish Root Ferment Filtrate, Decyl Glucoside, Argania Spinosa Kernel "
              "Oil, Simmondsia Chinensis Seed Oil, Aloe Barbadensis Leaf Extract, Hydroxypropyl Guar "
              "Hydroxypropyltrimonium Chloride, Panthenol, Tocopherol, Citrus "
              "Reticulata Peel Oil, Elettaria Cardamomum Seed Oil, Hibiscus Sabdariffa Flower Extract, Camellia "
              "Sinensis Leaf Extract, Citric Acid, Limonene*, Linalool*, Citral*, Geraniol*, Citronellol*."),
        upc='860016462052',
    ),
}

LEAF = 'M0 0 C22 31 68 26 100 0 C70 -22 24 -27 0 0Z'


def bottle(prod, uid, cls='bottle'):
    """Frasco âmbar quadrado 250 mL (corpo 47 x 147 mm, 172 mm com válvula) com o rótulo 40 x 125 mm.
    Unidades do viewBox = mm."""
    return f'''<svg class="{cls}" viewBox="0 0 70 186" role="img" aria-label="Ervena {PRODUCTS[prod]['name']} 250 mL bottle">
<defs>
 <linearGradient id="amb{uid}" x1="0" x2="1">
  <stop offset="0" stop-color="#2a1004"/><stop offset=".12" stop-color="#6b300b"/><stop offset=".3" stop-color="#a5521a"/>
  <stop offset=".52" stop-color="#8a4013"/><stop offset=".8" stop-color="#5a260a"/><stop offset="1" stop-color="#220c03"/>
 </linearGradient>
 <linearGradient id="cap{uid}" x1="0" x2="1">
  <stop offset="0" stop-color="#050505"/><stop offset=".3" stop-color="#3a3a3a"/><stop offset=".55" stop-color="#151515"/><stop offset="1" stop-color="#000"/>
 </linearGradient>
 <linearGradient id="shade{uid}" x1="0" x2="1">
  <stop offset="0" stop-color="#000" stop-opacity=".28"/><stop offset=".1" stop-color="#000" stop-opacity=".04"/>
  <stop offset=".22" stop-color="#fff" stop-opacity=".16"/><stop offset=".3" stop-color="#fff" stop-opacity="0"/>
  <stop offset=".88" stop-color="#000" stop-opacity=".04"/><stop offset="1" stop-color="#000" stop-opacity=".3"/>
 </linearGradient>
 <radialGradient id="shadow{uid}"><stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
 <clipPath id="lbl{uid}"><rect x="15" y="47" width="40" height="125" rx="2.6"/></clipPath>
</defs>
<ellipse cx="35" cy="182" rx="30" ry="3.2" fill="url(#shadow{uid})"/>
<!-- válvula -->
<path d="M28.5 6.2 H44.5 a1.6 1.6 0 0 1 1.6 1.6 V10 H27 V7.8 a1.6 1.6 0 0 1 1.5-1.6Z" fill="url(#cap{uid})"/>
<path d="M28.6 6.4 C22 6.2 15 7 9.2 9.6 C7.6 10.3 7.4 11.6 8.6 11.8 C9.4 11.9 9.8 11.4 10.6 11 C16 9.3 22 9.1 28.6 9.4Z" fill="#111"/>
<rect x="32.5" y="10" width="8" height="10" fill="url(#cap{uid})"/>
<rect x="31.3" y="18.5" width="10.4" height="2" rx=".6" fill="#0a0a0a"/>
<rect x="25.5" y="20.5" width="22" height="14.5" rx="1.6" fill="url(#cap{uid})"/>
<g stroke="#000" stroke-opacity=".55" stroke-width=".35">{''.join(f'<line x1="{26.8 + i * 1.18:.2f}" y1="21.3" x2="{26.8 + i * 1.18:.2f}" y2="34.2"/>' for i in range(17))}</g>
<rect x="29.5" y="35" width="14" height="2.4" fill="#4a1f07"/>
<!-- corpo -->
<path d="M11.5 37.4 H58.5 a3 3 0 0 1 3 3 V176 a4 4 0 0 1 -4 4 H12.5 a4 4 0 0 1 -4 -4 V40.4 a3 3 0 0 1 3 -3Z" fill="url(#amb{uid})"/>
<line x1="35.4" y1="38" x2="35.8" y2="178" stroke="#e8b27a" stroke-opacity=".18" stroke-width="1.6"/>
<!-- rótulo -->
<image href="/assets/label-{prod}-front.jpg" x="15" y="47" width="40" height="125" preserveAspectRatio="none" clip-path="url(#lbl{uid})"/>
<rect x="15" y="47" width="40" height="125" rx="2.6" fill="url(#shade{uid})"/>
<!-- brilho do vidro/PET -->
<path d="M14 39.5 C13 80 13 130 14 176" stroke="#fff" stroke-opacity=".22" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<path d="M57.6 40 V176" stroke="#ffd7a6" stroke-opacity=".1" stroke-width=".9"/>
</svg>'''


def sprig(cls):
    L = [(70, 214, -70, 1), (110, 190, 10, .95), (170, 154, -80, .9), (220, 125, 0, .8), (280, 90, -85, .72), (330, 62, -10, .6)]
    g = ''.join(f'<g transform="translate({x} {y}) rotate({r}) scale({s})"><path class="lf" style="--d:{i * .37:.2f}s" d="{LEAF}"/></g>'
                for i, (x, y, r, s) in enumerate(L))
    return (f'<svg class="sprig {cls}" viewBox="0 0 400 260" aria-hidden="true"><g class="sway">'
            f'<path class="stem" d="M10 250 C90 200 200 140 390 30"/>{g}</g></svg>')


def page(key):
    p = PRODUCTS[key]
    o = PRODUCTS[p['other']]
    title = f"Ervena {p['name']} — Natural Hair Care | 250 mL"
    desc = f"Ervena {p['name']}: {p['indications']} Plant based, with botanical extracts and essential oils. 250 mL / 8.5 fl oz."
    keys = ''.join(f'''<li class="ing"><svg viewBox="-4 -30 108 60" aria-hidden="true"><path d="{LEAF}"/></svg>
<h3>{n}</h3><p class="inci-name">{i}</p><p>{t}</p></li>''' for n, i, t in p['key'])
    steps = ''.join(f'<li><span>{n + 1:02d}</span><p>{s}</p></li>' for n, s in enumerate(p['steps']))
    ld = {
        "@context": "https://schema.org", "@type": "Product",
        "name": f"Ervena {p['name']}", "brand": {"@type": "Brand", "name": "Ervena"},
        "description": p['indications'], "gtin12": p['upc'],
        "image": f"https://ervenacosmetics.com/assets/label-{key}-front.jpg",
        "size": "250 mL / 8.5 fl oz", "url": f"https://ervenacosmetics.com/{p['slug']}/",
    }
    import json
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://ervenacosmetics.com/{p['slug']}/">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{p['indications']}">
<meta property="og:image" content="https://ervenacosmetics.com/assets/label-{key}-front.jpg">
<meta property="og:type" content="product">
<meta name="theme-color" content="#f5eedb">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/product.css">
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body>
<header class="top">
 <a class="brand" href="/" aria-label="Ervena home"><img src="/assets/logo.svg" alt="Ervena" width="74" height="60"></a>
</header>

<main>
<section class="hero">
 {sprig('s1')}{sprig('s2')}
 <div class="hero-media">
  <div class="halo" aria-hidden="true"></div>
  {bottle(key, 'h')}
 </div>
 <div class="hero-copy">
  <p class="eyebrow">Ervena · Natural Hair Care</p>
  <h1>{p['name']}</h1>
  <p class="headline">{p['headline']}</p>
  <p class="lede">{p['intro']}</p>
  <ul class="badges">
   <li>Plant based</li><li>Botanical extracts</li><li>Essential oils</li>
  </ul>
  <dl class="facts">
   <div><dt>Size</dt><dd>250 mL · 8.5 fl oz</dd></div>
   <div><dt>For</dt><dd>{p['tagline']}</dd></div>
   <div><dt>Made in</dt><dd>USA</dd></div>
  </dl>
  <a class="btn" href="#ingredients">Explore ingredients</a>
 </div>
</section>

<section class="why">
 <p class="kicker">What it does</p>
 <p class="statement">{p['indications']}</p>
</section>

<section class="keys" id="ingredients">
 <div class="sec-head"><p class="kicker">Key ingredients</p><h2>Botanicals with a purpose</h2></div>
 <ul class="ing-grid">{keys}</ul>
 <p class="swipe" aria-hidden="true">Swipe to see more &rarr;</p>
</section>

<section class="ritual">
 <div class="sec-head"><p class="kicker">Directions for use</p><h2>The ritual</h2></div>
 <ol class="steps">{steps}</ol>
</section>

<section class="details">
 <details open>
  <summary>Full ingredients (INCI)</summary>
  <p class="inci">{p['inci']}</p>
  <p class="note">{FOOTNOTE}</p>
 </details>
 <details>
  <summary>Directions</summary>
  <p>{p['directions']}</p>
 </details>
 <details>
  <summary>Warnings &amp; allergy alert</summary>
  <p><strong>Warnings:</strong> {WARN}</p>
  <p><strong>Allergy alert:</strong> {ALLERGY}</p>
 </details>
 <details>
  <summary>Product information</summary>
  <dl class="spec">
   <div><dt>Volume</dt><dd>250 mL / 8.5 fl oz</dd></div>
   <div><dt>Packaging</dt><dd>Amber square bottle with pump</dd></div>
   <div><dt>Shelf life</dt><dd>1 year</dd></div>
   <div><dt>UPC</dt><dd>{p['upc']}</dd></div>
   <div><dt>Origin</dt><dd>Made in USA</dd></div>
  </dl>
 </details>
</section>

<section class="pair">
 <div class="pair-media">{bottle(p['other'], 'p', 'bottle small')}</div>
 <div class="pair-copy">
  <p class="kicker">Complete the ritual</p>
  <h2>Ervena {o['name']}</h2>
  <p>{o['indications']}</p>
  <a class="btn ghost" href="/{o['slug']}/">Discover the {o['name'].lower()}</a>
 </div>
</section>
</main>

<footer class="foot">
 <img src="/assets/logo.svg" alt="" width="52" height="42">
 <p>&copy; <span class="y">2026</span> Ervena Cosmetics · Natural Hair Care · Made in USA</p>
</footer>
<script>document.querySelector('.y').textContent=new Date().getFullYear()</script>
</body>
</html>
'''


if __name__ == '__main__':
    for k, p in PRODUCTS.items():
        os.makedirs(os.path.join(ROOT, p['slug']), exist_ok=True)
        with open(os.path.join(ROOT, p['slug'], 'index.html'), 'w') as f:
            f.write(page(k))
        print('ok', p['slug'])
