"""Genererar Snö-demons produktsidor + shop-sida från katalogen.
Kör från projektroten: python3 build_site.py
"""
from pathlib import Path

ROOT = Path(__file__).parent

# ---- katalog ----------------------------------------------------------------
PRODUCTS = [
    dict(
        slug="rule-big-coin-neck-50", name="Rule big coin neck 50", price=499,
        category="Halsband", collection="Rule", material="Gold plated",
        colors=["gold", "silver"], sizes=["40 cm", "50 cm", "60 cm"], size_default="50 cm",
        reviews=128, tag="Bestseller",
        desc=("Kollektionens tyngdpunkt. En chunky men förfinad länk i 18k guldplätering "
              "med ett avtagbart mynthänge på 15 mm. Bär det solo mot en öppen skjorta, "
              "eller lägg det lågt under Flora daisy för en lager-på-lager-look."),
        specs=["18k guldplätering på mässing", "Kedjelängd 50 cm", "Mynthänge Ø 15 mm",
               "Nickelfritt och hypoallergent"],
        lifestyle="fb-rule-livingroom-2",
        lifestyle_cap="Buren i en sekelskiftesvåning på Östermalm",
        related=["flora-daisy-neck-40", "rule-charm-brace-sclear", "rule-coin-pendant-ear"],
    ),
    dict(
        slug="tulum-pearl-neck-40-45", name="Tulum pearl neck", price=299,
        category="Halsband", collection="Tulum", material="Guld / mix",
        colors=["gold"], sizes=[], size_label="40–45 cm, justerbar",
        reviews=86, tag="",
        desc=("Sötvattenspärlor och små färgglada glaspärlor på en justerbar guldkedja. "
              "Sitter högt mot huden och lyfter både linne och stickat. Tulum är "
              "sommarens lättaste lager."),
        specs=["14k guldplätering på mässing", "Längd 40–45 cm (justerbar)", "Pärlor 6 mm",
               "Sötvattenspärlor + glaspärlor"],
        lifestyle="ls-tulum-window-2",
        lifestyle_cap="Morgonljus genom höga fönster",
        related=["tulum-elastic-pearl-brace", "rule-coin-pendant-ear", "flora-daisy-ear"],
    ),
    dict(
        slug="flora-daisy-neck-40", name="Flora daisy neck 40", price=399,
        category="Halsband", collection="Flora", material="Gold plated",
        colors=["gold", "silver"], sizes=[], size_label="40 cm",
        reviews=64, tag="Nyhet",
        desc=("En tunn guldkedja med pyttesmå blommor — knappt större än en knappnål. "
              "Diskret nog för vardag, vacker nog för fest. Perfekt som det kortare "
              "lagret i en halsbandsstapel."),
        specs=["18k guldplätering på mässing", "Kedjelängd 40 cm", "Blomma 4 mm",
               "Nickelfritt och hypoallergent"],
        lifestyle="ls-kakelugn-3",
        lifestyle_cap="Vid kakelugnen, lager på lager",
        related=["rule-big-coin-neck-50", "flora-daisy-ear", "rule-charm-brace-sclear"],
    ),
    dict(
        slug="flora-daisy-ear", name="Flora daisy ear", price=249,
        category="Örhängen", collection="Flora", material="Silver plated",
        colors=["silver", "gold"], sizes=[], size_label="10 × 10 mm",
        reviews=152, tag="Bestseller",
        desc=("Silverblomman som lyser mot höga kragar och uppsatt hår. 10 mm, lätt och "
              "exakt — gjord för att bäras varje dag."),
        specs=["Silverpläterad mässing", "Storlek 10 × 10 mm", "Stift i sterling silver",
               "Nickelfritt och hypoallergent"],
        lifestyle="cu-daisy-ear-mirror-3",
        lifestyle_cap="Detalj mot spegeldörr",
        related=["flora-daisy-neck-40", "rule-coin-pendant-ear", "tulum-pearl-neck-40-45"],
    ),
    dict(
        slug="rule-coin-pendant-ear", name="Rule coin pendant ear", price=349,
        category="Örhängen", collection="Rule", material="Gold plated",
        colors=["gold"], sizes=[], size_label="25 mm",
        reviews=71, tag="",
        desc=("Ett litet mynthänge på 25 mm som rör sig med dig. Vardaglig elegans i "
              "18k guldplätering — bär ensamt eller matcha med Rule big coin neck."),
        specs=["18k guldplätering på mässing", "Längd 25 mm", "Mynt Ø 10 mm",
               "Stift i sterling silver"],
        lifestyle="fb-tulum-doorway-2",
        lifestyle_cap="I dörröppningen mellan två rum",
        related=["rule-big-coin-neck-50", "flora-daisy-ear", "rule-charm-brace-sclear"],
    ),
    dict(
        slug="rule-charm-brace-sclear", name="Rule charm brace", price=449,
        category="Armband", collection="Rule", material="Gold plated",
        colors=["gold"], sizes=[], size_label="One size",
        reviews=58, tag="",
        desc=("Hjärta och klöver i räfflat guld på en fin länk. Charmsen är kollektionens "
              "personliga signatur — bygg på med fler över tid."),
        specs=["18k guldplätering på mässing", "Charms 10 mm", "Justerbar länk",
               "Nickelfritt och hypoallergent"],
        lifestyle="cu-charm-brace-table-2",
        lifestyle_cap="Vid marmorbordet",
        related=["rule-big-coin-neck-50", "tulum-elastic-pearl-brace", "rule-coin-pendant-ear"],
    ),
    dict(
        slug="tulum-elastic-pearl-brace", name="Tulum elastic pearl brace", price=249,
        category="Armband", collection="Tulum", material="Guld / mix",
        colors=["gold"], sizes=[], size_label="17,5 cm, elastisk",
        reviews=43, tag="",
        desc=("Pärlor och guld på elastisk tråd — trär du bara på. Bär ett eller stapla "
              "flera. Sommarens enklaste armband."),
        specs=["14k guldplätering på mässing", "Längd 17,5 cm (elastisk)", "Pärlor 6 mm",
               "Sötvattenspärlor + glaspärlor"],
        lifestyle="ls-tulum-window-2",
        lifestyle_cap="Tulum, mot morgonljus",
        related=["tulum-pearl-neck-40-45", "rule-charm-brace-sclear", "flora-daisy-ear"],
    ),
]

BY_SLUG = {p["slug"]: p for p in PRODUCTS}

COLOR_LABEL = {"gold": "Gold plated", "silver": "Silver plated"}


def nav(prefix=""):
    return f'''<header class="nav">
  <div class="container nav-inner">
    <button class="nav-burger" aria-label="Meny">
      <svg fill="none" stroke-width="1.5" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav-links">
      <a href="{prefix}shop.html">Nyheter</a>
      <a href="{prefix}shop.html">Bestsellers</a>
      <a href="{prefix}shop.html?cat=Halsband">Halsband</a>
      <a href="{prefix}shop.html?cat=Örhängen">Örhängen</a>
      <a href="{prefix}shop.html?cat=Armband">Armband</a>
    </nav>
    <a class="nav-logo" href="{prefix}index.html" aria-label="Snö of Sweden">
      <img src="{prefix}images/logo.svg" alt="Snö of Sweden">
    </a>
    <div class="nav-icons">
      <svg fill="none" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <svg fill="none" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.7-9.5-9C1 8.5 3 5 6.5 5c2 0 3.5 1 4.5 2.5C12 6 13.5 5 15.5 5 19 5 21 8.5 20.5 12c-2 4.3-8.5 9-8.5 9z"/></svg>
      <span class="cart-dot"><svg fill="none" stroke-width="1.5" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7L6 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg></span>
    </div>
  </div>
</header>'''


def footer(prefix=""):
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="{prefix}images/logo.svg" alt="Snö of Sweden">
        <p>Smycken designade i Sverige sedan 2006.<br>För alla tillfällen — och alla dagar däremellan.</p>
      </div>
      <div>
        <h4>Shoppa</h4>
        <ul>
          <li><a href="{prefix}shop.html">Alla smycken</a></li>
          <li><a href="{prefix}shop.html?cat=Halsband">Halsband</a></li>
          <li><a href="{prefix}shop.html?cat=Örhängen">Örhängen</a></li>
          <li><a href="{prefix}shop.html?cat=Armband">Armband</a></li>
        </ul>
      </div>
      <div>
        <h4>Kundservice</h4>
        <ul>
          <li><a href="#">Leverans &amp; retur</a></li>
          <li><a href="#">Smyckesvård</a></li>
          <li><a href="#">Kontakta oss</a></li>
        </ul>
      </div>
      <div>
        <h4>Om Snö</h4>
        <ul>
          <li><a href="#">Vår historia</a></li>
          <li><a href="#">Butiker</a></li>
          <li><a href="#">Återförsäljare</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-note">
      <span>© 2026 Snö of Sweden</span>
      <span>Konceptdemo — exempelinnehåll, ej ett officiellt erbjudande</span>
    </div>
  </div>
</footer>'''


def head(title, prefix=""):
    return f'''<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex">
<title>{title}</title>
<link rel="icon" href="{prefix}images/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>'''


def prod_card(slug, reveal=True):
    p = BY_SLUG[slug]
    cls = "prod-card reveal" if reveal else "prod-card"
    tag = f'<span class="prod-tag">{p["tag"]}</span>' if p["tag"] else ""
    return f'''<a class="{cls}" href="{p['slug']}.html" data-cat="{p['category']}">
        <div class="prod-media">
          {tag}
          <img class="main" src="images/ecom/pack-{p['slug']}-1.jpg" alt="{p['name']}">
          <img class="alt" src="images/ecom/worn-{p['slug']}-1.jpg" alt="" aria-hidden="true">
        </div>
        <div class="prod-name">{p['name']}</div>
        <div class="prod-meta"><span>{p['material']}</span><span class="price">{p['price']} SEK</span></div>
      </a>'''


def build_product(p):
    slug = p["slug"]
    # galleri: burna + packshots + lifestyle
    thumbs = [
        f"images/ecom/worn-{slug}-1.jpg",
        f"images/ecom/worn-{slug}-2.jpg",
        f"images/ecom/pack-{slug}-1.jpg",
        f"images/ecom/pack-{slug}-2.jpg",
        f"images/campaign/{p['lifestyle']}.jpg",
    ]
    main = thumbs[0]
    thumb_html = "\n        ".join(
        f'<button class="{"active" if i==0 else ""}" onclick="swap(this,\'{t}\')"><img src="{t}" alt="Bild {i+1}"></button>'
        for i, t in enumerate(thumbs)
    )

    # färgswatchar
    swatches = "\n        ".join(
        f'<button class="swatch {c} {"active" if i==0 else ""}" aria-label="{COLOR_LABEL[c]}" onclick="pick(this,\'.swatch\')"></button>'
        for i, c in enumerate(p["colors"])
    )

    # storlek: pills vid flera, annars note-rad
    if p["sizes"]:
        pills = "\n        ".join(
            f'<button class="pill {"active" if s==p["size_default"] else ""}" onclick="pick(this,\'.pill\')">{s}</button>'
            for s in p["sizes"]
        )
        size_block = f'''<div class="opt-label">Längd</div>
      <div class="opt-row">
        {pills}
      </div>'''
    else:
        size_block = f'<div class="pdp-size-note">Storlek: <b>{p["size_label"]}</b></div>'

    specs = "\n          ".join(f"<li>{s}</li>" for s in p["specs"])

    related = "\n      ".join(prod_card(r) for r in p["related"])

    return f'''{head(f"{p['name']} — Snö of Sweden (konceptdemo)")}

<div class="announce">Fri frakt över 499 SEK <em>◆</em> 30 dagars öppet köp <em>◆</em> Skickas inom 24 h</div>

{nav()}

<div class="container">
  <div class="crumbs"><a href="index.html">Hem</a><span>/</span><a href="shop.html?cat={p['category']}">{p['category']}</a><span>/</span>{p['name']}</div>

  <div class="pdp-grid">
    <div class="pdp-gallery">
      <div class="pdp-main">
        <img id="mainImg" src="{main}" alt="{p['name']}">
      </div>
      <div class="pdp-thumbs">
        {thumb_html}
      </div>
    </div>

    <div class="pdp-info">
      <div class="pdp-kicker">{p['collection']}-kollektionen</div>
      <h1>{p['name']}</h1>
      <div class="pdp-price">{p['price']} SEK</div>
      <div class="pdp-rating"><span class="stars">★★★★★</span>{p['reviews']} recensioner</div>

      <div class="opt-label">Färg — <small>{COLOR_LABEL[p['colors'][0]]}</small></div>
      <div class="opt-row">
        {swatches}
      </div>

      {size_block}

      <div class="pdp-cta">
        <button class="btn btn-solid btn-block" onclick="addToCart()">Lägg i varukorgen — {p['price']} SEK</button>
        <button class="btn btn-ghost btn-block">Köp nu med Klarna</button>
      </div>

      <div class="pdp-usps">
        <span>Skickas inom 24 h</span>
        <span>Fri frakt</span>
        <span>30 dagars öppet köp</span>
      </div>

      <details class="acc" open>
        <summary>Beskrivning</summary>
        <p>{p['desc']}</p>
      </details>
      <details class="acc">
        <summary>Material &amp; mått</summary>
        <ul>
          {specs}
        </ul>
      </details>
      <details class="acc">
        <summary>Leverans &amp; retur</summary>
        <p>Skickas inom 24 timmar med spårbar frakt. Fri frakt över 499 SEK. 30 dagars öppet köp — returnera enkelt via vår returportal.</p>
      </details>
    </div>
  </div>
</div>

<figure class="pdp-editorial">
  <img src="images/campaign/{p['lifestyle']}.jpg" alt="{p['name']} buren">
  <figcaption>
    <div class="kicker">Autumn/Winter 2026</div>
    <p>{p['lifestyle_cap']}</p>
  </figcaption>
</figure>

<section class="section" style="padding-top:64px">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <div class="kicker">Styla looken</div>
        <h2>Passar med</h2>
      </div>
      <a class="head-link" href="shop.html">Se alla smycken</a>
    </div>
    <div class="prod-grid">
      {related}
    </div>
  </div>
</section>

{footer()}

<div class="buybar" id="buybar">
  <div>
    <div class="bb-name">{p['name']}</div>
    <div class="bb-price">{p['price']} SEK</div>
  </div>
  <button class="btn btn-solid" onclick="addToCart()">Lägg i varukorg</button>
</div>

<div class="toast" id="toast">Tillagd i varukorgen ✨</div>

<script>
function swap(btn, src) {{
  document.getElementById('mainImg').src = src;
  document.querySelectorAll('.pdp-thumbs button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}}
function pick(btn, sel) {{
  btn.parentElement.querySelectorAll(sel).forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}}
function addToCart() {{
  const t = document.getElementById('toast');
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2400);
}}
const cta = document.querySelector('.pdp-cta');
const bar = document.getElementById('buybar');
new IntersectionObserver(([e]) => {{
  bar.classList.toggle('show', !e.isIntersecting && e.boundingClientRect.top < 0);
}}, {{ threshold: 0 }}).observe(cta);
const io = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
}}, {{ threshold: 0.12 }});
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
setTimeout(() => document.querySelectorAll('.reveal').forEach(el => el.classList.add('in')), 1600);
</script>

</body>
</html>'''


def build_shop():
    cards = "\n      ".join(prod_card(p["slug"]) for p in PRODUCTS)
    return f'''{head("Alla smycken — Snö of Sweden (konceptdemo)")}

<div class="announce">Fri frakt över 499 SEK <em>◆</em> 30 dagars öppet köp <em>◆</em> Skickas inom 24 h</div>

{nav()}

<section class="shop-hero">
  <div class="container">
    <div class="kicker">Kollektionen</div>
    <h1>Alla smycken</h1>
    <p>Guld och silver designat i Sverige — för varje dag och varje tillfälle däremellan.</p>
  </div>
</section>

<div class="shop-filters" id="filters">
  <button class="active" data-f="all">Allt</button>
  <button data-f="Halsband">Halsband</button>
  <button data-f="Örhängen">Örhängen</button>
  <button data-f="Armband">Armband</button>
</div>

<div class="container">
  <div class="shop-grid" id="grid">
      {cards}
  </div>
</div>

{footer()}

<div class="toast" id="toast">Tillagd i varukorgen ✨</div>

<script>
const params = new URLSearchParams(location.search);
const cards = [...document.querySelectorAll('#grid .prod-card')];
const btns = [...document.querySelectorAll('#filters button')];
function filter(f) {{
  cards.forEach(c => c.classList.toggle('hide', f !== 'all' && c.dataset.cat !== f));
  btns.forEach(b => b.classList.toggle('active', b.dataset.f === f));
}}
btns.forEach(b => b.onclick = () => filter(b.dataset.f));
filter(params.get('cat') || 'all');
const io = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
}}, {{ threshold: 0.1 }});
cards.forEach(el => io.observe(el));
setTimeout(() => cards.forEach(el => el.classList.add('in')), 1600);
</script>

</body>
</html>'''


def main():
    for p in PRODUCTS:
        (ROOT / f"{p['slug']}.html").write_text(build_product(p), encoding="utf-8")
        print("byggd:", p["slug"] + ".html")
    (ROOT / "shop.html").write_text(build_shop(), encoding="utf-8")
    print("byggd: shop.html")


if __name__ == "__main__":
    main()
