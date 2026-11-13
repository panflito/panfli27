b=open("cuerpo.html").read()
# sello de versión: hace que el navegador pida los datos nuevos en vez de usar los que tenía guardados
import time
b=b.replace("__V__",time.strftime("%Y%m%d%H%M"))
head,rest=b.split("<style>",1); css,body=rest.split("</style>",1)
head=head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
html='<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="description" content="Panflito: la casa del árbol de Theo Fernandez Noguera, con sus líneas: Theo y Simón, YouTube, cuentos y columnitas, arte visual y más.">\n'+head+'<link rel="icon" href="favicon.ico" sizes="any">\n<link rel="icon" href="img/icono-32.png" type="image/png">\n<link rel="apple-touch-icon" href="img/icono-180.png">\n<meta name="theme-color" content="#fbfaf7">\n<style>\nbody{margin:0}\n'+css+'</style>\n</head>\n<body>\n'+body.strip()+'\n</body>\n</html>\n'
open("index.html","w").write(html)
open("artifact.html","w").write(b)
