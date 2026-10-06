# ZiNGS · rebranding — entrega de prototipos

Prototipos de portada, logotipos y sistema de marca para zings.es (regalos y souvenirs taurinos y de España, Calle Alcalá 231, Madrid). Cada archivo HTML es autónomo (un solo archivo, sin dependencias salvo Google Fonts) y se abre directamente en el navegador.

## Portadas

| Archivo | Contenido |
|---|---|
| `zings-rebrand.html` | Página principal: las once portadas en pestañas, galería de miniaturas, tabla comparativa y recomendación |
| `zings-apple-s1.html` | **G · Apple Store · Sistema 1**: la estructura de la Apple Store con el manual de marca aplicado (anagrama de cuatro Z, fucsia y blanco, Inter, texturas de papel, arena y tinta). Archivo limpio e independiente, base para el tema hijo de PrestaShop |
| `zings-apple.html` | F · Apple Store, con el logo Hombrera |
| `zings-funcional.html` | A · Upfront |
| `zings-editorial.html` | B · Dolce & Gabbana |
| `zings-sobria.html` | C · Gucci |
| `zings-clasica.html` | D · Hermès |
| `zings-artesana.html` | E · Loewe |

Las cuatro portadas de estilo propio (Plaza de toros, Feria de Jerez, Cartel de toros, Traje de luces) están en las pestañas de `zings-rebrand.html`.

## Apple Store · Sistema 1 (la web definitiva)

`zings-apple-s1.html` aplica el manual `branding/ZiNGS-manual-de-marca-S1-anagrama.pdf` a la portada de estilo Apple Store:

- **Logotipos**: icono fucsia con el anagrama en blanco en la barra de navegación (el avatar elegido), anagrama blanco a gran tamaño sobre la portada fucsia con textura, avatar circular en el bloque «Síguenos» y logotipo horizontal completo (anagrama + ZINGS + REGALOS DE ESPAÑA) en el pie, a 68 px para que el descriptor sea legible.
- **Color**: tinta #0E0C0D, fucsia capote #E3177F (único acento; #C8106B en enlaces pequeños sobre blanco y #FF8AC6 sobre tinta), papel #F6F0E6, arena #E6C086 y blanco. El amarillo solo aparece dentro de los productos dibujados.
- **Tipografía**: Inter 800 en titulares (tracking negativo), 600 en etiquetas en versalitas con tracking amplio, precios y subtítulos, 500/400 en texto corrido.
- **Texturas**: manchas suaves y grano fino generados con filtros SVG (sin imágenes) sobre fucsia, papel, arena y tinta, como en el manual.
- **Estructura de regalos**: categorías, «Lo último», regalos por precio, regalos para quién, apartado taurino en la navegación y el pie, «La diferencia ZiNGS» y «Síguenos». Los huecos de foto siguen siendo marcadores neutros.

## Marca

| Archivo | Contenido |
|---|---|
| `zings-logos.html` | 90 logotipos, diez por versión, sobre cuatro fondos |
| `zings-sistema.html` | Sistema de marca de las versiones A, B y C: logotipo, isotipo, imagotipo, isologo, tamaños mínimos, área de respeto, favicon y avatar |
| `zings-torero.html` | Dos siluetas: escena de torero, capote y toro, y torero a pincel |

## Fotografías

No hay fotografías: todos los huecos de imagen, incluida la portada de cada versión y las zonas de foto de las plantillas de redes, llevan un marcador neutro («Foto» / «Tu foto») a la espera de la fotografía propia de ZiNGS.

## Guías de marca (PDF)

En `branding/`, una guía por estilo (diez páginas, A4 apaisado): la idea, paleta con hex y proporciones, tipografía, las diez propuestas de logotipo con las tres recomendadas (o el símbolo Hombrera en la versión Apple Store), el logotipo en uso sobre cuatro fondos, la portada web en escritorio y móvil, producto y componentes, plantillas de redes y plan de redes (tono, pilares, ritmo del feed, hashtags, sí y no).

En `branding/plantillas-redes/`, las plantillas de cada estilo en PNG listas para usar: post cuadrado (1080 × 1080), feed 4:5 (1080 × 1350) e historia (1080 × 1920).

## Logos para redes sociales

En `branding/logos-redes/`: veintiocho avatares en cinco familias (A · Anagrama de cuatro Z, B · Hombrera, C · ZINGS tipográfico, D · Bandera de capote, E · ZiNGS con filetes), cinco portadas de 1500 × 500 y cinco marcas de agua blancas con fondo transparente. `png/` a 1080 px, `svg/` con la tipografía Inter embebida, `zings-logos-redes.zip` con todo y `zings-logos-redes.html` con la vista previa recortada en círculo.

## Logotipos definitivos y manuales de marca

Dos sistemas definitivos, con todo el texto convertido a trazados (no dependen de fuentes), en `branding/logos-definitivos/`:

- **Sistema 1 · Anagrama**: cuatro Z geométricas + «ZINGS» + «REGALOS DE ESPAÑA». Recomendado como identidad principal: tiene símbolo propio, aguanta a 16 px, se borda y reproduce a una tinta.
- **Sistema 2 · Motto**: «ZiNGS» en Bodoni Moda con doble filete y el lema «MADRID · DESDE LAS VENTAS». Firma de producto y packaging.

Cada sistema incluye versión principal, horizontal, símbolo o monograma, logotipo, versiones reducidas, avatares, portadas e iconos (512/192/64/32/16), en tinta, negativo, fucsia y con acento; `svg/`, `png/`, `editables/` (texto vivo), `zings-logos-definitivos.html` (presentación con construcción y pruebas de tamaño) y las hojas de contacto.

Los manuales de marca, uno por sistema, están en `branding/ZiNGS-manual-de-marca-S1-anagrama.pdf` y `branding/ZiNGS-manual-de-marca-S2-motto.pdf` (19 páginas A4 apaisado: logo completo, logotipo, horizontal, símbolos, área de respeto y tamaños mínimos, colores y texturas, tipografía, medidas para redes y look & feel).
