import contextlib
import copy
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import motor as m

class GameTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.old=(m.ROOT,m.DATA,m.CATALOG)
        m.ROOT=Path(self.temp.name); m.DATA=m.ROOT/'datos'; m.CATALOG=m.ROOT/'actividades'
        shutil.copytree(self.old[2],m.CATALOG)
        m.write(m.ROOT/'config.json',{'url_base':'https://raw.githubusercontent.com/test/repo/main'})
        m.write(m.DATA/'preferencias.json',{'idioma':'es'})
    def tearDown(self):
        m.ROOT,m.DATA,m.CATALOG=self.old
        self.temp.cleanup()
    def do(self,aid,commands):
        a,s,w=m.load(aid)
        subprocess.run(['/bin/bash','-c',commands],cwd=w,check=True)
    def pass_step(self,aid,response=None):
        before=m.load(aid)[1]['paso']
        with patch('builtins.input',return_value=response),contextlib.redirect_stdout(io.StringIO()):
            # check_test takes input at definition time; inject explicitly.
            real=m.check_test
            with patch.object(m,'check_test',side_effect=lambda t,a,s,w:real(t,a,s,w,answer=lambda _:response)):
                m.check(aid)
        self.assertEqual(m.load(aid)[1]['paso'],before+1)
    def test_complete_all_four_in_both_languages(self):
        for language in ('es','eu'):
            shutil.rmtree(m.DATA)
            m.write(m.DATA/'preferencias.json',{'idioma':language})
            for a in m.available(): m.start(a)
            aid='actividad_001'
            for response in (str(m.load(aid)[2]),'LEEME.txt','KAIXO','IZAR'): self.pass_step(aid,response)
            aid='actividad_002'
            for response in ('ALEX','NORTE','LUNA','entrada.txt'): self.pass_step(aid,response)
            aid='actividad_003'
            for cmd in ('mkdir -p refugio/copias','cp documentos/mapa.txt refugio/copias/','mv refugio/copias/mapa.txt refugio/copias/plano.txt','mv refugio/copias/plano.txt refugio/plano.txt','touch refugio/listo.txt; cp documentos/normas.txt refugio/copias/'):
                self.do(aid,cmd); self.pass_step(aid)
            aid='actividad_004'
            self.pass_step(aid,'IZAR-17'); self.pass_step(aid,'actualizacion.txt')
            for cmd in ('mkdir evidencias; cp informes/aviso.txt evidencias/','mkdir cuarentena; mv almacen/respaldos/actualizacion.txt cuarentena/sospechoso.txt','touch evidencias/resuelto.txt'):
                self.do(aid,cmd); self.pass_step(aid)
    def test_wrong_answers_and_contents_do_not_advance(self):
        a=m.available()[0]; m.start(a)
        with patch.object(m,'check_test',return_value=False),contextlib.redirect_stdout(io.StringIO()):m.check(a['id'])
        self.assertEqual(m.load(a['id'])[1]['paso'],0)
        a=m.available()[2]; m.start(a); aid=a['id']
        self.do(aid,'mkdir -p refugio/copias'); self.pass_step(aid)
        self.do(aid,'touch refugio/copias/mapa.txt')
        with contextlib.redirect_stdout(io.StringIO()):m.check(aid)
        self.assertEqual(m.load(aid)[1]['paso'],1)
    def test_resume_language_and_restart_isolation(self):
        a,b=m.available()[2:4]; m.start(a); m.start(b)
        self.do(a['id'],'mkdir -p refugio/copias'); self.pass_step(a['id'])
        self.do(b['id'],'touch personal.txt')
        m.remember(a['id'],str(m.load(a['id'])[2]/'refugio'))
        self.assertEqual(m.cwd(a['id']).name,'refugio')
        m.write(m.DATA/'preferencias.json',{'idioma':'eu'})
        self.assertEqual(m.start(a)[1]['idioma_escenario'],'es')
        with patch('builtins.input',return_value='no'),contextlib.redirect_stdout(io.StringIO()):m.reset(a['id'])
        self.assertEqual(m.load(a['id'])[1]['paso'],1)
        with patch('builtins.input',return_value='REINICIAR'),contextlib.redirect_stdout(io.StringIO()):m.reset(a['id'])
        self.assertEqual(m.load(a['id'])[1]['paso'],0)
        self.assertEqual(m.load(a['id'])[1]['idioma_escenario'],'eu')
        self.assertTrue((m.load(b['id'])[2]/'personal.txt').exists())
    def test_update_pins_existing_and_adds_new(self):
        a=m.available()[0]; m.start(a)
        changed=copy.deepcopy(a); changed['version']=2
        new=copy.deepcopy(a); new['id']='actividad_005'
        payloads={}
        entries=[]
        for x in (changed,new):
            name=x['id']+'.json'; raw=json.dumps(x).encode()
            payloads['actividades/'+name]=raw
            entries.append({'archivo':name,'sha256':hashlib.sha256(raw).hexdigest()})
        payloads['catalogo.json']=json.dumps({'schema':1,'actividades':entries}).encode()
        with patch.object(m,'fetch',side_effect=lambda url:payloads[url.split('/main/')[1]]),contextlib.redirect_stdout(io.StringIO()):m.update()
        self.assertEqual(m.load(a['id'])[0]['version'],1)
        self.assertEqual(m.read(m.CATALOG/'actividad_001.json')['version'],2)
        self.assertEqual(len(m.available()),5)
        with patch('builtins.input',return_value='REINICIAR'),contextlib.redirect_stdout(io.StringIO()):m.reset(a['id'])
        self.assertEqual(m.load(a['id'])[0]['version'],2)
    def test_failed_download_and_path_escape(self):
        before=(m.CATALOG/'actividad_001.json').read_bytes()
        with patch.object(m,'fetch',side_effect=OSError('offline')),contextlib.redirect_stdout(io.StringIO()):m.update()
        self.assertEqual((m.CATALOG/'actividad_001.json').read_bytes(),before)
        with self.assertRaises(ValueError):m.safe(m.DATA,'../escape')
        m.DATA.mkdir(exist_ok=True)
        (m.DATA/'link').symlink_to('/tmp',target_is_directory=True)
        with self.assertRaises(ValueError):m.safe(m.DATA,'link/escape')

if __name__=='__main__':unittest.main()
