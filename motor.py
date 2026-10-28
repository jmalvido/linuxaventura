#!/usr/bin/env python3
"""LinuxAventura 0.1 — motor para Bash real, Python 3.8+, sin dependencias."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import urllib.request
import interfaz as ui

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'datos'
CATALOG = ROOT / 'actividades'

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def write(p, value):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=p.parent, prefix='.guardado-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(value, f, ensure_ascii=False, indent=2)
            f.write('\n')
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def settings():
    return read(DATA/'preferencias.json') if (DATA/'preferencias.json').exists() else {'idioma':'es'}

def lang(): return settings()['idioma']
def tr(es, eu): return eu if lang() == 'eu' else es
def loc(value, language=None):
    return value[language or lang()] if isinstance(value, dict) else value

def safe(base, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError('Ruta no válida / Bide baliogabea')
    p = base / relative
    try:
        p.resolve().relative_to(base.resolve())
    except ValueError:
        raise ValueError('Ruta fuera del escenario / Eszenatokitik kanpoko bidea')
    return p

def validate(a):
    assert re.fullmatch(r'actividad_[0-9]{3,}', a['id']), 'ID inválido'
    assert isinstance(a['version'], int) and a['version'] > 0
    assert a['schema'] == 1
    assert a.get('motor_minimo', 1) <= 3, 'Actualiza el motor del juego'
    for k in ('titulo','final'):
        assert all(isinstance(a[k][l], str) for l in ('es','eu'))
    assert isinstance(a['pasos'], list) and a['pasos']
    for name, content in a['archivos'].items():
        safe(Path('/tmp/escenario-validacion'), name)
        assert all(isinstance(content[l],str) for l in ('es','eu'))
    for d in a.get('carpetas',[]): safe(Path('/tmp/escenario-validacion'), d)
    for step in a['pasos']:
        for l in ('es','eu'):
            assert isinstance(step['texto'][l],str)
            assert isinstance(step['pistas'][l],list) and step['pistas'][l]
        assert step['pruebas']
        for test in step['pruebas']:
            assert test['tipo'] in ('respuesta','carpeta','contenido','ausente','vacio','respuesta_sistema','salida','alias','sin_alias','ejecutado','historial_limpio','reentrada')
            if test['tipo']=='respuesta':
                assert all(isinstance(test['pregunta'][l],str) for l in ('es','eu'))
                assert all(isinstance(test['respuestas'][l],list) and test['respuestas'][l] for l in ('es','eu'))
            elif test['tipo'] in ('respuesta_sistema','salida'):
                from retos import QUERIES
                assert test['consulta'] in QUERIES
                if test['tipo']=='salida': safe(Path('/tmp/escenario-validacion'),test['ruta'])
                else: assert all(isinstance(test['pregunta'][l],str) for l in ('es','eu'))
            elif test['tipo']=='alias':
                assert re.fullmatch(r'[a-z][a-z0-9_]*',test['nombre'])
                assert test['valores'] and all(isinstance(v,str) for v in test['valores'])
            elif test['tipo']=='sin_alias':
                assert isinstance(test['nombre'],str)
            elif test['tipo']=='ejecutado':
                assert test['comandos'] and all(isinstance(v,str) for v in test['comandos'])
            elif test['tipo'] in ('historial_limpio','reentrada'):
                pass
            else:
                safe(Path('/tmp/escenario-validacion'), test['ruta'])
                if test['tipo']=='contenido':
                    assert test['origen'] in a['archivos']
    return a

def available():
    found=[]
    ids=set()
    for p in sorted(CATALOG.glob('*.json')):
        try:
            a=validate(read(p))
            if a['id'] in ids: raise ValueError('ID duplicado')
            ids.add(a['id']); found.append(a)
        except (ValueError, KeyError, AssertionError, TypeError) as e:
            print(f'{p.name}: {e}')
    return sorted(found,key=lambda a:a['id'])

def folder(aid):
    if not re.fullmatch(r'actividad_[0-9]{3,}', aid): raise ValueError('ID inválido')
    p=DATA/aid
    if p.is_symlink(): raise ValueError('Directorio de datos enlazado')
    return p

def load(aid):
    d=folder(aid)
    return read(d/'actividad.json'), read(d/'estado.json'), d/'escenario'

def start(a):
    d=folder(a['id'])
    if (d/'estado.json').exists(): return load(a['id'])
    if (d/'escenario').exists():
        raise ValueError('Escenario sin estado: recupera tus archivos antes de continuar.')
    d.mkdir(parents=True, exist_ok=True)
    w=d/'escenario'; w.mkdir()
    for name in a.get('carpetas',[]): safe(w,name).mkdir(parents=True,exist_ok=True)
    language=lang()
    for name, content in a['archivos'].items():
        p=safe(w,name); p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(loc(content,language),encoding='utf-8')
    write(d/'actividad.json',a)
    write(d/'estado.json',{'paso':0,'pistas':{},'idioma_escenario':language,'cwd':'.'})
    return load(a['id'])

def show(aid, fresh=False, notice=None):
    a,s,w=load(aid)
    if fresh: ui.clear()
    if notice: print(ui.color(notice, "success"))
    print('\n'+ui.color(loc(a['titulo']), 'title'))
    print(ui.color(tr('Raíz del escenario: ','Eszenatokiaren erroa: ')+str(w), 'muted'))
    if s['paso']>=len(a['pasos']):
        print(ui.highlight(loc(a['final'])))
        print(ui.color(tr('Actividad completada. MENU para volver.','Jarduera osatuta. MENU itzultzeko.'), 'success'))
        return
    print(ui.color(tr('Paso','Urratsa')+f" {s['paso']+1}/{len(a['pasos'])}", "title"))
    print(ui.highlight(loc(a['pasos'][s['paso']]['texto']).replace('{escenario}',str(w))))
    print('\n'+ui.highlight('PISTA · COMPROBAR · AYUDA · REINICIAR · MENU'))

def check_test(test,a,s,w,answer=input):
    kind=test['tipo']
    if kind not in ('respuesta','carpeta','contenido','ausente','vacio'):
        from retos import check as check_unit
        return check_unit(test,a,s,w,answer,loc,safe)
    if kind=='respuesta':
        value=answer(ui.color(loc(test['pregunta']), 'command')+' ').strip().casefold()
        acceptable=loc(test['respuestas'],s['idioma_escenario'])
        return value in [x.replace('{escenario}',str(w)).casefold() for x in acceptable]
    p=safe(w,test['ruta'])
    if p.is_symlink(): return False
    if kind=='carpeta': return p.is_dir()
    if kind=='ausente': return not p.exists()
    if kind=='vacio': return p.is_file() and p.stat().st_size==0
    if kind=='contenido':
        expected=loc(a['archivos'][test['origen']],s['idioma_escenario']).encode('utf-8')
        return p.is_file() and p.read_bytes()==expected
    return False

def check(aid):
    a,s,w=load(aid)
    if s['paso']>=len(a['pasos']): show(aid); return
    step=a['pasos'][s['paso']]
    for test in step['pruebas']:
        if not check_test(test,a,s,w):
            print(ui.color(loc(test.get('error',{'es':'Todavía no está resuelto. Revisa el objetivo o escribe PISTA.','eu':'Oraindik ez dago ebatzita. Berrikusi helburua edo idatzi PISTA.'})), 'error'))
            return
    s['paso']+=1
    s['sesion_paso']=os.environ.get('LA_SESSION_ID','')
    write(folder(aid)/'estado.json',s)
    show(aid, fresh=True, notice=tr('¡Correcto! Progreso guardado.','Zuzen! Aurrerapena gordeta.'))

def hint(aid):
    a,s,w=load(aid)
    if s['paso']>=len(a['pasos']): show(aid); return
    hints=loc(a['pasos'][s['paso']]['pistas'])
    key=str(s['paso']); n=min(s['pistas'].get(key,0),len(hints)-1)
    print(ui.color(f'PISTA {n+1}/{len(hints)}: ', 'hint')+ui.highlight(hints[n].replace('{escenario}',str(w))))
    s['pistas'][key]=n+1; write(folder(aid)/'estado.json',s)

def reset(aid):
    a,s,w=load(aid)
    print(tr('Se borrará el trabajo de ESTA actividad. Las demás se conservan.','Jarduera HONETAKO lana ezabatuko da. Besteak mantenduko dira.'))
    if input(tr('Escribe REINICIAR para confirmar: ','Idatzi REINICIAR berresteko: ')).strip()!='REINICIAR':
        print(tr('Cancelado.','Bertan behera.')); return
    # Validate replacement before deleting anything. Never follow a workspace symlink.
    replacement=next((x for x in available() if x['id']==aid),a)
    validate(replacement)
    if w.is_symlink(): raise ValueError('Escenario enlazado: reinicio rechazado.')
    if w.exists(): shutil.rmtree(w)
    (folder(aid)/'estado.json').unlink()
    for name in ('alias_guardados.sh','alias_comprobacion.txt','historial_comprobacion.txt'):
        (folder(aid)/name).unlink(missing_ok=True)
    start(replacement); show(aid, fresh=True)

def remember(aid, cwd):
    a,s,w=load(aid)
    try: rel=Path(cwd).resolve().relative_to(w.resolve())
    except ValueError: return
    if Path(cwd).is_dir():
        s['cwd']=str(rel); write(folder(aid)/'estado.json',s)

def cwd(aid):
    a,s,w=load(aid)
    p=w if s.get('cwd','.')=='.' else safe(w,s['cwd'])
    return p if p.is_dir() else w

def help_text():
    if lang()=='es':
        print(ui.highlight('''CÓMO SE JUEGA
Lee el objetivo, usa comandos reales de Linux y escribe COMPROBAR.
PISTA       Ayuda progresiva para el paso actual.
COMPROBAR   Verifica archivos o te pregunta lo que has descubierto.
AYUDA       Muestra estas instrucciones y el objetivo actual.
REINICIAR   Borra y reconstruye SOLO esta actividad, previa confirmación.
MENU        Vuelve al menú; conserva archivos y progreso.
ACTUALIZAR  Descarga actividades desde el repositorio configurado.
SALIR       Cierra el juego conservando el trabajo.

Las mayúsculas importan: los comandos del juego van en MAYÚSCULAS.
Los comandos Linux se escriben normalmente en minúsculas.
Estás en Bash real: cd, tuberías, redirecciones y scripts funcionan.
No necesitas sudo. Trabaja dentro de la carpeta del escenario.
El juego NO aísla la máquina: los comandos actúan con tus permisos.
Los pasos superados se guardan automáticamente; guarda tus scripts en el editor.
Ctrl+C cancela un comando. Ctrl+D vuelve al menú.\n'''))
    else:
        print(ui.highlight('''NOLA JOKATU
Irakurri helburua, erabili Linuxeko benetako komandoak eta idatzi COMPROBAR.
PISTA       Uneko urratserako laguntza mailakatua.
COMPROBAR   Fitxategiak egiaztatu edo aurkitutakoari buruz galdetu.
AYUDA       Argibide hauek eta uneko helburua erakutsi.
REINICIAR   Jarduera HAU bakarrik ezabatu eta berreraiki, berretsi ondoren.
MENU        Menura itzuli; fitxategiak eta aurrerapena mantendu.
ACTUALIZAR  Konfiguratutako biltegitik jarduerak deskargatu.
SALIR       Jokotik irten lana mantenduz.

Letra larriak garrantzitsuak dira: jokoaren komandoak LETRA LARRIZ.
Linuxeko komandoak normalean letra xehez idazten dira.
Benetako Bash erabiltzen ari zara: cd, hodiak, birbideratzeak eta scriptak dabiltza.
Ez duzu sudo behar. Lan egin eszenatokiaren karpetan.
Jokoak EZ du makina isolatzen: komandoek zure baimenekin jarduten dute.
Gainditutako urratsak automatikoki gordetzen dira; gorde scriptak editorean.
Ctrl+C: komandoa eten. Ctrl+D: menura itzuli.\n'''))

def fetch(url):
    if not url.startswith('https://raw.githubusercontent.com/'):
        raise ValueError('Solo URLs HTTPS de raw.githubusercontent.com')
    with urllib.request.urlopen(url,timeout=15) as r:
        if not r.geturl().startswith('https://raw.githubusercontent.com/'):
            raise ValueError('Redirección no permitida')
        data=r.read(2_000_001)
        if len(data)>2_000_000: raise ValueError('Archivo demasiado grande')
        return data

def update():
    cfg=read(ROOT/'config.json'); base=cfg.get('url_base','').rstrip('/')
    if not base:
        print(tr('Falta configurar url_base en config.json. Consulta README.md. Puedes seguir jugando sin conexión.','Konfiguratu url_base config.json fitxategian. Ikusi README.md. Konexiorik gabe jokatzen jarrai dezakezu.')); return
    try:
        manifest=json.loads(fetch(base+'/catalogo.json'))
        assert manifest['schema']==1
        pending=[]; ids=set()
        for entry in manifest['actividades']:
            name=entry['archivo']
            assert re.fullmatch(r'actividad_[0-9]{3,}\.json',name)
            raw=fetch(base+'/actividades/'+name)
            assert hashlib.sha256(raw).hexdigest()==entry['sha256'], 'SHA-256'
            a=validate(json.loads(raw))
            assert name==a['id']+'.json' and a['id'] not in ids
            ids.add(a['id'])
            dest=CATALOG/name
            if dest.exists() and read(dest)['version']>=a['version']: continue
            pending.append((dest,a))
        # Download and validate every candidate before publishing; states are snapshots.
        for dest,a in pending: write(dest,a)
        print(tr('Actividades incorporadas/actualizadas: ','Gehitutako/eguneratutako jarduerak: ')+str(len(pending)))
        print(tr('Las actividades iniciadas conservan su versión hasta REINICIAR.','Hasitako jarduerek beren bertsioa mantentzen dute REINICIAR egin arte.'))
    except (OSError,ValueError,KeyError,AssertionError,TypeError) as e:
        print(tr('No se pudo actualizar. Puedes seguir jugando. Detalle: ','Ezin izan da eguneratu. Jokatzen jarrai dezakezu. Xehetasuna: ')+str(e))

def main():
    action=sys.argv[1]; aid=os.environ.get('LA_ID')
    if action=='check': check(aid)
    elif action=='hint': hint(aid)
    elif action=='show': show(aid, fresh=True)
    elif action=='reset': reset(aid)
    elif action=='help': ui.clear(); help_text(); show(aid)
    elif action=='update': update()
    elif action=='remember': remember(aid,sys.argv[2])
    elif action=='path': print(cwd(aid))

if __name__=='__main__':
    try: main()
    except (KeyboardInterrupt,EOFError): print('\n'+tr('Cancelado.','Bertan behera.'))
    except (OSError,ValueError,KeyError,AssertionError) as e:
        print(tr('Error: ','Errorea: ')+str(e),file=sys.stderr); sys.exit(1)
