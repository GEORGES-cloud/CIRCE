import random
def leaves(n,color,blur=16,seed=1,scale=(0.9,1.8),box=(1080,1350)):
    random.seed(seed);out=[]
    for _ in range(n):
        x,y=random.uniform(-80,box[0]+80),random.uniform(-80,box[1]+80);r=random.uniform(0,360);s=random.uniform(*scale);o=random.uniform(.25,.7)
        out.append(f'<path d="M0,-80 C22,-40 22,40 0,80 C-22,40 -22,-40 0,-80Z" transform="translate({x:.0f},{y:.0f}) rotate({r:.0f}) scale({s:.2f})" fill="{color}" opacity="{o:.2f}"/>')
    return f'<svg class="abs" style="left:0;top:0" width="{box[0]}" height="{box[1]}"><defs><filter id="b{seed}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="{blur}"/></filter></defs><g filter="url(#b{seed})">{"".join(out)}</g></svg>'

def plinth(top,light,seed):
    # bloque de piedra: cara superior clara, frente con degradado y la luz proyectada encima
    return f'''<div class="abs" style="left:300px;top:{top}px;width:480px;height:{1350-top}px;overflow:hidden;background:linear-gradient(180deg,#3a3f4b 0%,#262a33 30%,#13161c 100%)">
  <div class="abs" style="left:-300px;top:-{top}px;opacity:.45">{leaves(60,light,14,seed)}</div>
  <div class="abs" style="left:0;top:0;width:480px;height:10px;background:linear-gradient(90deg,#596071,#7a8296,#596071)"></div>
  <div class="abs" style="left:0;top:0;width:480px;height:100%;background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(0,0,0,0) 30%,rgba(0,0,0,0) 70%,rgba(0,0,0,.45))"></div>
</div>
<div class="abs" style="left:300px;top:{top-6}px;width:480px;height:40px;background:radial-gradient(ellipse 30% 50% at 50% 40%,rgba(0,0,0,.85),rgba(0,0,0,0) 70%)"></div>'''

def bottle(src,glow,top=-196):
    return f'<img src="{src}" class="abs" style="left:-60px;top:{top}px;width:1200px;filter:drop-shadow(0 0 36px {glow})">'

html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0}}body{{background:#222}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0a1626;font-family:'Inter Tight',sans-serif}}
.abs{{position:absolute}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.wm{{position:absolute;left:0;width:1080px;text-align:center;color:#fff;font-weight:300;font-size:22px;letter-spacing:.4em;text-transform:uppercase;text-shadow:0 2px 24px rgba(0,0,0,.5)}}
</style></head><body>

<section class="s" id="s1" style="background:radial-gradient(ellipse 80% 60% at 50% 40%,#1b3f7a,#0a1a36 60%,#050a14)">
{leaves(70,'#5f8fe6',14,1)}{leaves(30,'#a9c6ff',6,2,(0.4,0.9))}
{plinth(990,'#5f8fe6',11)}{bottle('coupage-cutout.png','rgba(80,130,230,.35)')}
</section>

<section class="s" id="s2">
 <div class="ph" style="background-image:url(botellas_coupage_estudio.webp);background-size:2600px auto;background-position:50% 26%"></div>
 <div class="abs" style="inset:0;mix-blend-mode:screen;opacity:.85">{leaves(60,'#3f6fd0',22,3)}</div>
 <div class="abs" style="inset:0;background:radial-gradient(ellipse 70% 70% at 50% 50%,rgba(0,0,0,0) 50%,rgba(0,0,0,.7) 100%)"></div>
</section>

<section class="s" id="s3">
 <div class="ph" style="background-image:url(foto_hileras-1440.jpg);background-size:150%;background-position:40% 50%"></div>
 <div class="abs" style="inset:0;background:rgba(10,22,38,.18)"></div>
</section>

<section class="s" id="s4" style="background:radial-gradient(ellipse 80% 60% at 50% 40%,#5a2a3a,#241018 60%,#0a0608)">
{leaves(70,'#e07a8a',14,4)}{leaves(30,'#ffc9a0',6,5,(0.4,0.9))}
{plinth(990,'#e07a8a',12)}{bottle('arbequina-cutout.png','rgba(230,120,140,.3)')}
</section>

<section class="s" id="s5">
 <div class="ph" style="background-image:url(foto_castillo-cote-1920.jpg);background-position:45% 35%"></div>
 <div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(0,0,0,.1),rgba(0,0,0,.35))"></div>
</section>

<!-- 6 · silueta a contraluz: una hoja de luz azul detrás de la botella -->
<section class="s" id="s6" style="background:#05070d">
 <svg class="abs" style="left:0;top:0" width="1080" height="1350"><defs><filter id="bl" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="30"/></filter><radialGradient id="rg" cx="50%" cy="50%" r="55%"><stop offset="0" stop-color="#b8d4ff"/><stop offset=".5" stop-color="#2f6bd0"/><stop offset="1" stop-color="#0a1a36"/></radialGradient></defs>
  <g filter="url(#bl)" transform="translate(540,560)">
   <path d="M0,-640 C420,-380 420,380 0,640 C-420,380 -420,-380 0,-640Z" fill="url(#rg)" transform="rotate(18)"/>
   <path d="M0,-620 C260,-360 260,360 0,620 C-260,360 -260,-360 0,-620Z" fill="url(#rg)" transform="rotate(-42) scale(.7)" opacity=".6"/>
  </g></svg>
 {plinth(1000,'#2f6bd0',13).replace('#3a3f4b','#1b2436').replace('#262a33','#111827').replace('#596071,#7a8296,#596071','#2b3a5c,#3c5080,#2b3a5c')}
 <img src="coupage-cutout.png" class="abs" style="left:-60px;top:-186px;width:1200px;filter:brightness(.1)">
 <div class="wm" style="bottom:80px;font-size:18px">Real de Cote</div>
</section>
</body></html>'''
open('carrusel.html','w').write(html)
