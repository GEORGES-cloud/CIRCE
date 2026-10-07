import re
CSS='''<!doctype html><html lang="es"><head><meta charset="utf-8">
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
.w p{color:rgba(255,255,255,.8)}
.cta{margin-top:56px;font-size:19px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;border-bottom:1.5px solid currentColor;padding-bottom:4px}
.dark .cta{border:0;background:#0b0b0c;color:#fff;padding:22px 44px}
.tag{font-size:34px;font-weight:500;letter-spacing:-.02em;text-transform:uppercase;color:#fff}
.cap{font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#fff;font-weight:500}
.cap small{display:block;font-size:17px;color:#999;margin-top:8px;font-weight:300}
.num{position:absolute;right:72px;top:64px;font-size:18px;letter-spacing:.2em;color:#999}
.dark .num,.s:not(.light) .num{color:rgba(255,255,255,.6)}
</style></head><body>'''

def photo(src,pos='center',size='cover'):
    return f'<div class="ph" style="background-image:url({src});background-position:{pos};background-size:{size}"></div>'
def light(over,title,para='',cta=''):
    return f'<section class="s light"><div class="c"><div class="ov">{over}</div><h1>{title}</h1>{f"<p>{para}</p>" if para else ""}{f"<div class=cta>{cta}</div>" if cta else ""}</div></section>'
def dark(src,over,title,pos='center',cta='',tint='.45',para=''):
    return f'<section class="s dark">{photo(src,pos)}<div class="ph" style="background:rgba(0,0,0,{tint})"></div><div class="c w"><div class="ov">{over}</div><h1>{title}</h1>{f"<p>{para}</p>" if para else ""}{f"<div class=cta>{cta}</div>" if cta else ""}</div></section>'
def foto(src,pos='center',size='cover',label=''):
    l=f'<div class="abs cap" style="left:72px;bottom:72px">{label}</div>' if label else ''
    return f'<section class="s">{photo(src,pos,size)}{l}</section>'
def botella(v,name,sub):
    return f'<section class="s">{photo(f"botellas_{v}_estudio.webp")}<div class="abs cap" style="left:0;width:1080px;text-align:center;bottom:84px">{name}<small>{sub}</small></div></section>'
def detalle(v,pos='50% 26%'):
    return f'<section class="s">{photo(f"botellas_{v}_estudio.webp",pos,"2600px auto")}<div class="ph" style="background:radial-gradient(ellipse 70% 70% at 50% 50%,rgba(0,0,0,0) 55%,rgba(0,0,0,.6))"></div></section>'
CIERRE='<section class="s" style="background:linear-gradient(180deg,#0b0b0c,#0a1626)"><img src="logo-gold.png" class="abs" style="width:230px;left:425px;top:520px"><div class="abs cap" style="left:0;width:1080px;text-align:center;top:800px;font-weight:300;letter-spacing:.3em;font-size:17px">realdecote.es · @realdecote</div></section>'
CONTACTO='<section class="s light"><div class="c"><div class="ov">Contacto</div><h1>Hablemos</h1><p style="margin-top:40px;line-height:2">info@realdecote.es<br>+34 680 40 85 80 · WhatsApp<br>realdecote.es</p><p style="font-size:19px;color:#999;margin-top:40px">Ctra. de Coripe, km 2,3 — Finca Cote · 41770 Montellano, Sevilla</p></div></section>'

portada=lambda i: open('grid.html').read()  # no usado: las portadas son los post-XX.png ya hechos
C={
 1:[light('Real de Cote','Aceite de oliva<br>virgen extra','Sin filtrar. Montellano, Sevilla.'),
    foto('foto_hoja-1920.jpg','40% 50%'),
    light('La casa','Cinco aceites.<br>Una sola casa.','Coupage, Manzanilla, Arbequina, Hojiblanca y BIO.','Descubrir'),
    foto('foto_hileras-1440.jpg','35% 45%','150%'),CIERRE],
 2:[botella('coupage','Coupage','De la casa'),botella('manzanilla','Manzanilla','Monovarietal'),botella('arbequina','Arbequina','Monovarietal'),botella('hojiblanca','Hojiblanca','Monovarietal'),botella('bio','BIO','Ecológico'),
    light('Formatos','500 ml · 250 ml','Cada aceite con su ficha técnica: variedad, información nutricional, formatos y conservación.','Más información')],
 3:[detalle('coupage'),light('Coupage','De la casa','Varias variedades, un solo carácter. El aceite con el que empezar.'),
    foto('mesa-2-1920.jpg','50% 50%'),light('Coupage','Para todo','Crudo sobre pan, verdura, pescado o carne.'),CIERRE],
 4:[light('En la mesa','Un hilo<br>al final','El aceite se añade al terminar, en crudo. Así conserva aroma y sabor.'),
    foto('mesa-6-1440.jpg','50% 50%'),light('En la mesa','Pescado y aceite','Bonito, conserva, marinado. Un monovarietal suave acompaña sin cubrir.'),
    foto('mesa-4-1920.jpg','50% 50%'),CIERRE],
 5:[foto('mesa-2-1920.jpg'),light('En la mesa','Crudo','Donde el aceite se nota es en el plato terminado.'),
    foto('mesa-5-1920.jpg','50% 45%'),light('En la mesa','También en dulce','Un virgen extra de perfil suave en repostería.'),CIERRE],
 6:[light('En la mesa','Pulpo, patata<br>y aceite','Un plato sencillo pide un aceite con carácter.'),
    botella('hojiblanca','Hojiblanca','Monovarietal'),light('Hojiblanca','Con cuerpo','Frutado intenso, ligero amargor y picante final.'),CIERRE],
 7:[light('La almazara','Sin filtrar','El aceite pasa a la botella tal como sale de la almazara. Por eso no es transparente.'),
    foto('foto_hileras-1440.jpg','35% 45%','150%'),light('La almazara','Del olivo<br>a la botella','Cosecha, extracción y embotellado en la misma casa.'),
    foto('foto_bodega-1920.jpg','60% 30%'),CIERRE],
 8:[detalle('bio','50% 30%'),light('BIO','Ecológico','Olivar en ecológico, con certificación de la Unión Europea.'),
    foto('olivo-centenario-1920.jpg','50% 50%'),light('BIO','La tierra manda','Sin tratamientos de síntesis. El mismo cuidado, otro camino.'),CIERRE],
 9:[foto('foto_castillo-cote-1920.jpg','45% 35%'),light('Legado','Montellano','Al sur de la provincia de Sevilla, donde la campiña se encuentra con la sierra.'),
    foto('finca-1920.jpg','50% 50%'),light('Legado','Finca Cote','Ctra. de Coripe, km 2,3. Entre colinas de olivar.'),CIERRE],
 10:[light('Legado','El castillo<br>de Cote','En lo alto de un cerro, cerca del pueblo. El nombre de la casa viene de aquí.'),
    foto('olivar-colinas-1920.jpg','50% 60%'),light('Legado','Un paisaje','Olivar, campiña y sierra. Lo que se ve desde el castillo.'),
    foto('muro-2400.jpg','50% 50%'),CIERRE],
 11:[light('La colección','Cinco tapones.<br>Cinco aceites.','Cada variedad tiene su color. La botella es la misma.'),
     detalle('coupage','50% 8%'),foto('muro-2400.jpg','50% 50%'),light('La colección','500 ml · 250 ml','Para la mesa y para regalar.','Descubrir'),CIERRE],
 12:[light('Profesionales','Distribución<br>y hostelería','Restaurantes, tiendas gourmet y distribuidores.'),
     light('Profesionales','Marca blanca','Tu etiqueta, nuestro aceite.'),
     foto('muro-2400.jpg','50% 50%'),light('Profesionales','Exportación','Enviamos a todo el mundo.'),CONTACTO],
}
for i,slides in C.items():
    html=CSS+''.join(s.replace('<section ',f'<section id="p{k+2}" ',1).replace('</section>',f'<div class="num">{k+2} / {len(slides)+1}</div></section>',1) for k,s in enumerate(slides))+'</body></html>'
    open(f'carrusel-{i:02d}.html','w').write(html)
    print(i,len(slides)+1)
