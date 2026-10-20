#!/usr/bin/env python3
"""Menú independiente; descubre las actividades sin una lista fija."""
import os
import subprocess
import sys
import fcntl
import motor as m

def choose_language():
    while True:
        v=input('1. Castellano  /  2. Euskera > ').strip()
        if v in ('1','2'):
            cfg=m.settings(); cfg['idioma']='es' if v=='1' else 'eu'
            m.write(m.DATA/'preferencias.json',cfg); return

def main():
    if sys.platform!='linux':
        print('Esta versión necesita Linux con Bash. Windows nativo: versión futura.'); return
    m.DATA.mkdir(exist_ok=True)
    with (m.DATA/'sesion.lock').open('w') as lock:
        try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:
            print('Ya hay una sesión abierta / Saio bat irekita dago.'); return
        if not (m.DATA/'preferencias.json').exists(): choose_language()
        while True:
            acts=m.available()
            print('\nLINUXAVENTURA · 0.1\n')
            for i,a in enumerate(acts,1):
                d=m.folder(a['id'])
                status=m.tr('Sin empezar','Hasi gabe')
                if (d/'estado.json').exists():
                    saved,s,w=m.load(a['id'])
                    status=m.tr('Completada','Osatuta') if s['paso']>=len(saved['pasos']) else m.tr('En curso','Abian')+f" ({s['paso']}/{len(saved['pasos'])})"
                print(f"{i}. {m.loc(a['titulo'])} [{status}]")
            print('\nACTUALIZAR · IDIOMA · AYUDA · SALIR')
            choice=input(m.tr('Elige una actividad: ','Aukeratu jarduera: ')).strip()
            if choice=='SALIR': return
            if choice=='IDIOMA': choose_language(); continue
            if choice=='ACTUALIZAR': m.update(); continue
            if choice=='AYUDA': m.help_text(); continue
            if not choice.isdigit() or not 1<=int(choice)<=len(acts):
                print(m.tr('Elige un número o un comando del menú.','Aukeratu zenbaki bat edo menuko komando bat.')); continue
            a=acts[int(choice)-1]; m.start(a)
            env=os.environ.copy()
            env.update(LA_ROOT=str(m.ROOT),LA_ID=a['id'],LA_PYTHON=sys.executable,LA_HISTORY=str(m.folder(a['id'])/'historial'))
            env.pop('BASH_ENV',None); env.pop('ENV',None)
            result=subprocess.run(['/bin/bash','--noprofile','--rcfile',str(m.ROOT/'terminal.bash'),'-i'],cwd=m.cwd(a['id']),env=env)
            if result.returncode==42: return

if __name__=='__main__':
    try: main()
    except (KeyboardInterrupt,EOFError): print('\nAgur / Hasta pronto.')
    except (OSError,ValueError,KeyError) as e:
        print('Error / Errorea:',e); sys.exit(1)
