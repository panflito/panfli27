b=open("cuerpo.html").read()
head,rest=b.split("<style>",1); css,body=rest.split("</style>",1)
head=head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
html='<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="description" content="Panflito: la casa del árbol de Theo Fernandez Noguera, con cuatro líneas: Theo y Simón, YouTube, escritos y arte visual.">\n'+head+'<link rel="icon" href="img/verde-parada.webp">\n<style>\nbody{margin:0}\n'+css+'</style>\n</head>\n<body>\n'+body.strip()+'\n</body>\n</html>\n'
open("index.html","w").write(html)
open("artifact.html","w").write(b)
