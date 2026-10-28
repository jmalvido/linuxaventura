"""Presentación compartida; no modifica actividades ni progreso."""
import os
import re
import sys

COLORS = {'title':'1;36', 'command':'1;33', 'success':'1;32', 'error':'1;31', 'hint':'1;35', 'muted':'36'}

def terminal():
    return sys.stdout.isatty() and os.environ.get('TERM','') not in ('','dumb')

def color(text, role='command'):
    if not terminal() or 'NO_COLOR' in os.environ:
        return str(text)
    return '\033['+COLORS[role]+'m'+str(text)+'\033[0m'

def clear():
    # Clear visible screen only, preserving terminal scrollback.
    if terminal() and os.environ.get('LA_CLEAR','1') != '0':
        print('\033[2J\033[H', end='', flush=True)

def highlight(text):
    words=r'\b(?:PISTA|COMPROBAR|AYUDA|REINICIAR|MENU|ACTUALIZAR|SALIR|IDIOMA|pwd|ls|cat|cd|mkdir|cp|mv|touch|date|cal|ncal|who|whoami|man|info|clear|whereis|alias|unalias|uname|passwd|history|exit)\b'
    lines=[]
    for line in str(text).split('\n'):
        if line.startswith('  ') and line.strip():
            lines.append(color(line,'command'))
        else:
            lines.append(re.sub(words,lambda m:color(m.group(),'command'),line))
    return '\n'.join(lines)

def pause(message):
    input(message)
