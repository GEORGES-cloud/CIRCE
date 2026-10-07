def photo(src,pos='center',size='cover',extra=''):
    return f'<div class="ph" style="background-image:url({src});background-position:{pos};background-size:{size};{extra}"></div>'
def light(over,title,para='',cta=''):
    return f'''<section class="s light"><div class="c">
 <div class="ov">{over}</div><h1>{title}</h1>{f'<p>{para}</p>' if para else ''}{f'<div class="cta">{cta}</div>' if cta else ''}
</div></section>'''
def dark_over(src,over,title,pos='center',cta='Explorar',tint='.45'):
    return f'''<section class="s dark">{photo(src,pos)}<div class="ph" style="background:rgba(0,0,0,{tint})"></div><div class="c w">
 <div class="ov">{over}</div><h1>{title}</h1><div class="cta">{cta}</div></div></section>'''

posts=[]
# 1 · portada: olivar aéreo + escudo (como el hero de la web)
posts.append(f'''<section class="s">{photo('foto_hileras-1440.jpg','35% 45%','150%')}<div class="ph" style="background:radial-gradient(ellipse 60% 45% at 50% 52%,rgba(11,11,12,.5),rgba(11,11,12,.15) 60%,rgba(11,11,12,0))"></div>
<img src="logo-gold.png" class="abs" style="width:360px;left:360px;top:420px">
<div class="abs tag" style="left:72px;bottom:72px">Aceite de oliva virgen extra</div></section>''')
# 2 · texto claro
posts.append(dark_over('muro-2400.jpg','Real de Cote','Cinco aceites.<br>Una sola casa.','50% 50%','Descubrir','.35'))
# 3 · botella coupage sobre negro (foto de estudio)
posts.append(f'''<section class="s">{photo('botellas_coupage_estudio.webp')}<div class="abs cap" style="left:0;width:1080px;text-align:center;bottom:84px">Coupage<small>De la casa</small></div></section>''')
# 4 · plato
posts.append(f'<section class="s">{photo("mesa-1-1920.jpg","50% 40%")}</section>')
# 5 · En la mesa (texto claro, como la sección)
posts.append(dark_over('mesa-5-1920.jpg','Real de Cote','En la mesa','50% 45%','@realdecote','.3'))
# 6 · plato
posts.append(f'<section class="s">{photo("mesa-3-1920.jpg","50% 50%")}</section>')
# 7 · almazara
posts.append(dark_over('foto_bodega-1920.jpg','Real de Cote','La almazara','60% 30%','Explorar','.5'))
# 8 · botella BIO
posts.append(f'''<section class="s">{photo('botellas_bio_estudio.webp')}<div class="abs cap" style="left:0;width:1080px;text-align:center;bottom:84px">BIO<small>Ecológico</small></div></section>''')
# 9 · legado
posts.append(dark_over('finca-1920.jpg','Legado','Montellano, Sevilla','50% 50%','Explorar','.35'))
# 10 · castillo
posts.append(f'<section class="s">{photo("foto_castillo-cote-1920.jpg","45% 35%")}</section>')
# 11 · colección: cinco botellas sobre negro
bots=''.join(f'<img src="{v}-cutout.png" class="abs" style="width:{w}px;left:{x}px;top:{t}px">' for v,w,x,t in [('bio',1100,-400,40),('arbequina',1100,-205,40),('hojiblanca',1100,185,40),('manzanilla',1100,380,40),('coupage',1180,-50,-10)])
posts.append(f'''<section class="s" style="background:radial-gradient(ellipse 70% 50% at 50% 55%,#1c1c1e,#0b0b0c 70%)">{bots}
<div class="abs tag" style="left:72px;bottom:72px;color:#fff">La colección</div></section>''')
# 12 · profesionales
posts.append(dark_over('olivar-colinas-1920.jpg','Distribución, hostelería, tiendas gourmet y marca blanca.','Profesionales<br>y exportación','50% 60%','Contactar','.25'))

html='''<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0}body{background:#222}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0b0b0c;font-family:'Inter Tight',sans-serif;color:#111}
.abs{position:absolute}.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.light{background:#f7f7f7}.dark{color:#fff}
.c{position:absolute;left:96px;right:96px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.ov{font-size:20px;letter-spacing:.12em;text-transform:uppercase;color:#777;font-weight:400;margin-bottom:26px}
.w .ov{color:rgba(255,255,255,.75)}
h1{font-size:64px;font-weight:500;letter-spacing:-.025em;line-height:1.08;text-transform:uppercase}
p{font-size:25px;line-height:1.55;color:#666;font-weight:300;margin-top:30px;max-width:720px}
.cta{margin-top:56px;font-size:19px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;border-bottom:1.5px solid currentColor;padding-bottom:4px}
.dark .cta{border:0;background:#0b0b0c;color:#fff;padding:22px 44px}
.tag{font-size:34px;font-weight:500;letter-spacing:-.02em;text-transform:uppercase;color:#fff}
.cap{font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#fff;font-weight:500}
.cap small{display:block;font-size:17px;color:#999;margin-top:8px;font-weight:300}
</style></head><body>'''+''.join(p.replace('<section class="s',f'<section id="p{i+1}" class="s',1) for i,p in enumerate(posts))+'</body></html>'
open('grid.html','w').write(html)
