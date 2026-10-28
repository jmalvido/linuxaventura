"""Prueba de integración con un Bash interactivo y un pseudoterminal real."""
import os
from pathlib import Path
import pty
import select
import shutil
import signal
import sys
import tempfile
import time
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import motor as m

class TerminalTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.old=(m.ROOT,m.DATA,m.CATALOG)
        root=Path(self.tmp.name)/'juego';root.mkdir()
        for f in self.old[0].glob('*.py'):shutil.copy2(f,root/f.name)
        shutil.copy2(self.old[0]/'terminal.bash',root/'terminal.bash')
        shutil.copytree(self.old[2],root/'actividades')
        m.ROOT=root;m.DATA=root/'datos';m.CATALOG=root/'actividades'
        m.write(m.DATA/'preferencias.json',{'idioma':'es'})
        self.pid=None;self.fd=None
    def tearDown(self):
        self.stop()
        m.ROOT,m.DATA,m.CATALOG=self.old;self.tmp.cleanup()
    def stop(self):
        if self.pid:
            try:os.kill(self.pid,signal.SIGTERM)
            except ProcessLookupError:pass
            os.waitpid(self.pid,0);os.close(self.fd);self.pid=None
    def read_prompt(self):
        buf=b''; deadline=time.monotonic()+8
        while time.monotonic()<deadline:
            r,_,_=select.select([self.fd],[],[],0.2)
            if r:
                try:chunk=os.read(self.fd,65536)
                except OSError:break
                buf+=chunk
                if buf.endswith(b'] # ') or buf.endswith(b'] $ '):return buf.decode(errors='replace')
        self.fail('No llegó el prompt: '+buf.decode(errors='replace'))
    def open(self,aid,sid):
        a=next(a for a in m.available() if a['id']==aid);m.start(a)
        env=os.environ.copy();env.update(LA_ROOT=str(m.ROOT),LA_ID=aid,LA_SESSION_ID=sid,LA_PYTHON=sys.executable,LA_HISTORY=str(m.folder(aid)/'historial'),NO_COLOR='1',LA_CLEAR='0',TERM='xterm')
        self.pid,self.fd=pty.fork()
        if self.pid==0:
            os.chdir(m.cwd(aid))
            os.execve('/bin/bash',['bash','--noprofile','--rcfile',str(m.ROOT/'terminal.bash'),'-i'],env)
        self.read_prompt()
    def command(self,cmd):
        os.write(self.fd,(cmd+'\n').encode());return self.read_prompt()
    def leave(self):
        os.write(self.fd,b'exit\n');os.waitpid(self.pid,0);os.close(self.fd);self.pid=None
    def test_alias_check_and_resume(self):
        aid='actividad_008';self.open(aid,'one')
        self.command("alias quien='clear; whoami; date'")
        self.command('quien')
        text=self.command('COMPROBAR')
        self.assertIn('¡Correcto!',text)
        self.assertEqual(m.load(aid)[1]['paso'],1)
        self.leave();self.open(aid,'two')
        self.assertIn('clear; whoami; date',self.command('alias quien'))
        self.leave()
    def test_clear_history_and_real_reentry(self):
        aid='actividad_009';a=next(a for a in m.available() if a['id']==aid);m.start(a)
        s=m.load(aid)[1];s['paso']=2;m.write(m.folder(aid)/'estado.json',s)
        self.open(aid,'first');self.command('whoami');self.command('history -c');self.command('history')
        self.assertIn('¡Correcto!',self.command('COMPROBAR'))
        self.assertEqual(m.load(aid)[1]['paso'],3)
        self.assertNotIn('¡Correcto!',self.command('COMPROBAR'))
        self.leave();self.open(aid,'second')
        self.assertIn('¡Correcto!',self.command('COMPROBAR'))
        self.assertEqual(m.load(aid)[1]['paso'],4)
        self.leave()

if __name__=='__main__':unittest.main()
