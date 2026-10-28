"""Comprobaciones de la unidad: datos reales, alias e historial de Bash."""
import os
from pathlib import Path
import pwd
import re
import shlex
import subprocess

# Solo se ejecutan estas consultas de lectura, nunca comandos procedentes del JSON.
QUERIES = {
    'usuario':['whoami'], 'nucleo':['uname','-s'], 'equipo':['uname','-n'],
    'version':['uname','-r'], 'compilacion':['uname','-v'], 'arquitectura':['uname','-m'],
    'procesador':['uname','-p'], 'plataforma':['uname','-i'], 'so':['uname','-o'],
    'sistema':['uname','-a'], 'fecha':['date','+%Y-%m-%d'],
    'fecha_detalle':['date','+%d %m %A'], 'cal_fijo':['cal','2','2028'],
    'cal_anual':['cal','2028'], 'ubicacion':['whereis','date','uname'],
}

def query(name):
    result=subprocess.run(QUERIES[name],capture_output=True,text=True,timeout=10)
    if result.returncode: raise ValueError('No se pudo consultar: '+' '.join(QUERIES[name]))
    return result.stdout.strip()

def tokens(text):
    lex=shlex.shlex(text,posix=True,punctuation_chars=';&|<>')
    lex.whitespace_split=True; lex.commenters=''
    return list(lex)

def history(w):
    p=w.parent/'historial_comprobacion.txt'
    if not p.exists(): return []
    return [re.sub(r'^\s*\d+\*?\s*','',line).strip() for line in p.read_text().splitlines() if line.strip()]

def aliases(w):
    p=w.parent/'alias_comprobacion.txt'
    out={}
    if not p.exists(): return out
    for line in p.read_text().splitlines():
        try: parts=shlex.split(line)
        except ValueError: continue
        if len(parts)==2 and parts[0]=='alias' and '=' in parts[1]:
            name,value=parts[1].split('=',1); out[name]=value
    return out

def matches_command(line, expected):
    # Se comprueba la orden escrita, no fragmentos dentro de echo o de un alias.
    try: return tokens(line)==tokens(expected)
    except ValueError: return False

def check(test,a,s,w,answer,loc,safe):
    kind=test['tipo']
    if kind=='respuesta_sistema':
        value=answer(loc(test['pregunta'])+' ').strip()
        return value==query(test['consulta'])
    if kind=='salida':
        p=safe(w,test['ruta'])
        return p.is_file() and not p.is_symlink() and p.read_text().strip()==query(test['consulta'])
    if kind=='alias':
        actual=aliases(w).get(test['nombre'])
        if actual is None: return False
        return any(matches_command(actual,x) for x in test['valores'])
    if kind=='sin_alias': return test['nombre'] not in aliases(w)
    if kind=='ejecutado':
        return any(matches_command(line,cmd) for line in history(w) for cmd in test['comandos'])
    if kind=='historial_limpio':
        lines=history(w)
        return bool(lines) and all(line in ('COMPROBAR','history','history -w') for line in lines)
    if kind=='reentrada':
        previous=s.get('sesion_paso')
        return bool(previous) and bool(os.environ.get('LA_SESSION_ID')) and previous!=os.environ['LA_SESSION_ID']
    return False
