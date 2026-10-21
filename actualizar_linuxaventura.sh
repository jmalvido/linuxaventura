#!/usr/bin/env bash
# Instala o actualiza LinuxAventura en el HOME del usuario actual.
set -euo pipefail
if [[ ${EUID} -eq 0 ]]; then
    echo 'Ejecuta este script con tu usuario habitual, sin sudo.' >&2
    exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
    echo 'Falta Python 3. Instálalo y vuelve a ejecutar este script:' >&2
    echo 'sudo apt update && sudo apt install python3' >&2
    exit 1
fi
python3 - <<'PY'
import datetime
import fcntl
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

URL = 'https://github.com/jmalvido/linuxaventura/archive/refs/heads/main.tar.gz'

def install(home):
    home = Path(home)
    target = home / 'linuxaventura'
    if target.is_symlink() or (target.exists() and not target.is_dir()):
        raise RuntimeError('~/linuxaventura debe ser una carpeta normal, no un enlace ni un archivo.')
    if target.exists() and not (target/'jugar.sh').is_file():
        raise RuntimeError('Ya existe ~/linuxaventura pero no parece una instalación del juego. No se ha modificado.')
    lock_path = home / '.linuxaventura-instalacion.lock'
    if lock_path.is_symlink(): raise RuntimeError('El archivo de bloqueo no puede ser un enlace.')
    with lock_path.open('a+') as install_lock:
        try: fcntl.flock(install_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: raise RuntimeError('Ya hay otra instalación o actualización en curso.')
        game_lock = None
        try:
            if target.exists():
                data = target/'datos'
                if data.is_symlink(): raise RuntimeError('datos no puede ser un enlace. No se ha modificado la instalación.')
                data.mkdir(exist_ok=True)
                if (data/'sesion.lock').is_symlink(): raise RuntimeError('Bloqueo de sesión no válido.')
                game_lock = (data/'sesion.lock').open('a+')
                try: fcntl.flock(game_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError: raise RuntimeError('Cierra el juego con SALIR antes de actualizar.')
            print('Descargando la última versión de jmalvido/linuxaventura (main)…', flush=True)
            with tempfile.TemporaryDirectory(prefix='.linuxaventura-descarga-', dir=home) as tmp:
                tmp = Path(tmp)
                archive = tmp/'juego.tar.gz'
                with urllib.request.urlopen(URL, timeout=30) as response, archive.open('wb') as out:
                    total = 0
                    while True:
                        chunk = response.read(1024*1024)
                        if not chunk: break
                        total += len(chunk)
                        if total > 100*1024*1024: raise RuntimeError('Descarga demasiado grande.')
                        out.write(chunk)
                stage = tmp/'linuxaventura'
                stage.mkdir()
                print('Descomprimiendo y comprobando los archivos…', flush=True)
                with tarfile.open(archive, 'r:gz') as tar:
                    size = 0
                    members = tar.getmembers()
                    if len(members) > 20000: raise RuntimeError('Demasiados archivos en el paquete.')
                    for member in members:
                        p = PurePosixPath(member.name)
                        if p.is_absolute() or '..' in p.parts or not p.parts or p.parts[0] != 'linuxaventura-main':
                            raise RuntimeError('El paquete contiene una ruta inesperada.')
                        parts = p.parts[1:]
                        if not parts: continue
                        if parts[0] in ('datos', '.git', '__pycache__'): continue
                        if '__pycache__' in parts or member.name.endswith('.pyc'): continue
                        if not (member.isfile() or member.isdir()):
                            raise RuntimeError('El paquete contiene un enlace o archivo especial no admitido.')
                        dest = stage.joinpath(*parts)
                        if member.isdir(): dest.mkdir(parents=True, exist_ok=True); continue
                        size += member.size
                        if size > 300*1024*1024: raise RuntimeError('Paquete descomprimido demasiado grande.')
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        with tar.extractfile(member) as source, dest.open('wb') as out:
                            shutil.copyfileobj(source, out)
                        dest.chmod(0o755 if member.mode & 0o111 else 0o644)
                required = ('jugar.sh','menu.py','motor.py','terminal.bash','config.json','catalogo.json')
                for name in required:
                    if not (stage/name).is_file(): raise RuntimeError('Falta un archivo del juego: '+name)
                if not (stage/'actividades').is_dir(): raise RuntimeError('Falta la carpeta actividades.')
                # Comprueba sintaxis sin importar ni ejecutar el código descargado.
                for file in stage.glob('*.py'):
                    compile(file.read_bytes(), str(file), 'exec')
                subprocess.run(['bash','-n',str(stage/'jugar.sh')],check=True)
                subprocess.run(['bash','-n',str(stage/'terminal.bash')],check=True)
                if (target/'datos').exists():
                    print('Conservando el progreso y los archivos del alumno…', flush=True)
                    shutil.copytree(target/'datos', stage/'datos', symlinks=True)
                backup = None
                if target.exists():
                    backups = home/'.linuxaventura-copias'
                    if backups.is_symlink(): raise RuntimeError('La carpeta de copias no puede ser un enlace.')
                    backups.mkdir(exist_ok=True)
                    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
                    backup = backups/('linuxaventura-'+stamp)
                    target.rename(backup)
                try:
                    stage.rename(target)
                except BaseException:
                    if backup is not None: backup.rename(target)
                    raise
                print('\n¡LinuxAventura está listo!')
                if backup is not None:
                    print('Copia de la instalación anterior:', backup)
                print('Para jugar:')
                print('bash ~/linuxaventura/jugar.sh')
        finally:
            if game_lock is not None: game_lock.close()

if __name__ == '__main__':
    try:
        install(Path.home())
    except KeyboardInterrupt:
        print('\nOperación cancelada.', file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print('\nNo se ha completado la instalación:', exc, file=sys.stderr)
        print('Corrige el problema y vuelve a ejecutar el script.', file=sys.stderr)
        sys.exit(1)
PY
