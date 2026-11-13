# Arma las fotos de la línea docente: recorta según docente-fotos.json (lo que sale de la mesa de fotos),
# guarda las versiones web en img/docente/ y reescribe la parte de fotos de docente.json.
# c = [izquierda, arriba, derecha, abajo], la fracción que se corta de cada lado. Los originales no se tocan.
import json,os,re
from PIL import Image
CFG=json.load(open('docente-fotos.json'))['proyectos']
D=json.load(open('docente.json'))
alts=json.load(open('archivo/media/docente/alts.json')) if os.path.exists('archivo/media/docente/alts.json') else {}
for it in D:
    for m in re.finditer(r'<img src="img/docente/([^"]+)"[^>]*alt="([^"]*)">',it['html']): alts.setdefault(m.group(1),m.group(2))
json.dump(alts,open('archivo/media/docente/alts.json','w'),ensure_ascii=False,indent=1)
for f in os.listdir('img/docente'): os.remove('img/docente/'+f)
def img(p,estilo):
    im=Image.open('archivo/media/docente/'+p['f']).convert('RGB'); l,t,r,b=p.get('c',[0,0,0,0]); w,h=im.size
    im=im.crop((round(w*l),round(h*t),round(w*(1-r)),round(h*(1-b)))); im.thumbnail((900,900),Image.LANCZOS)
    if p.get('margen'):   # margen del color del papel de la foto (se toma del borde), para que la figura respire
        import numpy as np
        A=np.asarray(im).astype(int); k=max(3,im.width//60); borde=np.concatenate([A[:k].reshape(-1,3),A[-k:].reshape(-1,3),A[:,:k].reshape(-1,3),A[:,-k:].reshape(-1,3)])
        claro=borde[borde.sum(1)>600]; col=tuple(int(x) for x in np.median(claro if len(claro)>50 else borde,axis=0))
        m=round(im.width*p['margen']); lienzo=Image.new('RGB',(im.width+2*m,im.height+2*m),col); lienzo.paste(im,(m,m)); im=lienzo; print(p['f'],'margen',m,'px color',col)
    im.save('img/docente/'+p['f'],quality=74,optimize=True,progressive=True)
    p['_a']=im.width/im.height; p['_w'],p['_h']=im.size
    return lambda est:f'<img src="img/docente/{p["f"]}" width="{p["_w"]}" height="{p["_h"]}" decoding="async" alt="{alts.get(p["f"],"")}"'+(f' style="{est}"' if est else '')+'>'
def arma(disp,ps):
    g=[img(p,None) for p in ps]; a=[p['_a'] for p in ps]; n=len(ps)
    fila=lambda idx:'<div class="ff">'+''.join(g[i](f'flex:{a[i]:.4f} 1 0;aspect-ratio:{a[i]:.4f}') for i in idx)+'</div>' if len(idx)>1 else g[idx[0]]('')
    if disp=='columna' or n==1: return ''.join(x('') for x in g)
    if disp=='lado' and n>2:
        ac=1/sum(1/x for x in a[1:])
        return f'<div class="ff estira">'+g[0](f'flex:{a[0]:.4f} 1 0')+f'<div class="fc" style="flex:{ac:.4f} 1 0">'+''.join(g[i](f'aspect-ratio:{a[i]:.4f}') for i in range(1,n))+'</div></div>'
    if disp=='dos-una' and n>2: return fila([0,1])+''.join(g[i]('') for i in range(2,n))
    if disp=='una-dos' and n>2: return g[0]('')+fila(list(range(1,n)))
    return fila(list(range(n)))
for it in D:
    if it['id'] not in CFG: continue   # secciones sin fotos de proyecto (taller de animación)
    c=CFG[it['id']]; ps=[p for p in c['fotos'] if p.get('usar',True)]
    texto=re.split(r'<div class="fotos|<img',it['html'])[0]
    it['html']=texto+'<div class="fotos'+('' if c.get('redondo',True) else ' recto')+'">'+arma(c['disp'],ps)+'</div>'
json.dump(D,open('docente.json','w'),ensure_ascii=False,separators=(',',':'))
print('fotos:',len(os.listdir('img/docente')),'peso:',sum(os.path.getsize('img/docente/'+f) for f in os.listdir('img/docente'))//1024,'KB')
