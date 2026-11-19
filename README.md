# panfli27

Página personal de Theo Fernandez Noguera (panflito.com). HTML, CSS y JS sin frameworks, publicada con GitHub Pages.

## Dónde está cada cosa

- `cuerpo.html`: diseño y funcionamiento de toda la página. `build.py` lo convierte en `index.html` (ese no se edita a mano).
- `mapa.json`: las líneas, sus colores, las paradas y sus links.
- `columnitas.json`: las columnitas que se muestran.
- `cuentos.json`: la lista de cuentos. El texto de cada uno está en `cuentos/<nombre>.md`.
- `docente.json`: los proyectos de Design&T. y el taller de animación.
- `docente-fotos.json` + `fotos.py`: recortes de las fotos (salen de la mesa de fotos) y el script que genera las fotos web desde los originales.
- `img/`: todo lo que carga la página, en versión liviana.
- `archivo/`: originales y contenido guardado que la página no usa.

## Cuentos

Cada cuento es un `.md` en `cuentos/`, y la página lo muestra tal cual: párrafos separados por una línea en blanco, cada renglón respetado, `*cursiva*` y `**negrita**`. Se puede editar directo en github.com (lápiz, pegar, "Commit changes") y en un minuto se actualiza.

## Fotos y dibujos para la web

Cada imagen se exporta al tamaño en que se ve en la página (por ejemplo, 800 px de ancho para una columna de dos, contando pantallas de alta densidad). Si cambia el diseño y una imagen se muestra más grande, hay que volver a exportarla desde su original en `archivo/media/`.

## Regla

Los textos de los cuentos y de las columnitas no se corrigen ni se reformatean nunca: ni ortografía, ni puntuación, ni saltos de línea. Se publican exactamente como los escribió Theo.
