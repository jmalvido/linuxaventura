import contextlib
import io
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import motor as m
import retos

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.old=m.DATA
        m.DATA=Path(self.tmp.name)/'datos'; m.write(m.DATA/'preferencias.json',{'idioma':'es'})
    def tearDown(self):m.DATA=self.old;self.tmp.cleanup()
    def test_all_new_definitions_and_languages(self):
        for language in ('es','eu'):
            m.write(m.DATA/'preferencias.json',{'idioma':language})
            for a in m.available()[4:]:
                m.validate(a)
                self.assertTrue(a['titulo'][language])
                for step in a['pasos']:
                    self.assertTrue(step['texto'][language]);self.assertEqual(len(step['pistas'][language]),2)
            a=m.available()[-1]; _,s,w=m.start(a)
            for step in a['pasos']:
                t=step['pruebas'][0]
                self.assertTrue(m.check_test(t,a,s,w,lambda _:t['respuestas'][language][0]))
                self.assertFalse(m.check_test(t,a,s,w,lambda _:'incorrecto'))
    def test_alias_real_bash_quoting_and_mistakes(self):
        import subprocess
        a,s,w=m.start(m.available()[7])
        aliases=subprocess.check_output(['bash','-c',"alias quien='clear; whoami; date'; alias -p"],text=True)
        (w.parent/'alias_comprobacion.txt').write_text(aliases)
        t=a['pasos'][0]['pruebas'][0]
        self.assertTrue(m.check_test(t,a,s,w))
        (w.parent/'alias_comprobacion.txt').write_text("alias quien='clear; who; date'\n")
        self.assertFalse(m.check_test(t,a,s,w))
    def test_history_requires_command_not_echo_or_definition(self):
        a,s,w=m.start(m.available()[7]);t={'tipo':'ejecutado','comandos':['quien']}
        p=w.parent/'historial_comprobacion.txt'
        p.write_text(" 1 echo quien\n 2 alias quien='whoami'\n 3 COMPROBAR\n")
        self.assertFalse(m.check_test(t,a,s,w))
        p.write_text(' 1 quien\n 2 COMPROBAR\n')
        self.assertTrue(m.check_test(t,a,s,w))
        t={'tipo':'historial_limpio'}
        self.assertFalse(m.check_test(t,a,s,w))
        p.write_text(' 1 history\n 2 COMPROBAR\n')
        self.assertTrue(m.check_test(t,a,s,w))
    def test_reentry_needs_new_session(self):
        a,s,w=m.start(m.available()[8]);s['sesion_paso']='session-a'
        with patch.dict(os.environ,{'LA_SESSION_ID':'session-a'}):
            self.assertFalse(m.check_test({'tipo':'reentrada'},a,s,w))
        with patch.dict(os.environ,{'LA_SESSION_ID':'session-b'}):
            self.assertTrue(m.check_test({'tipo':'reentrada'},a,s,w))
    def test_final_dossier_and_tampering_both_languages(self):
        import subprocess
        # Calendar is stubbed only because this test host has no cal; system queries are real.
        original_query=retos.query
        def query(name):return 'CALENDARIO FEBRERO 2028' if name=='cal_fijo' else original_query(name)
        for language in ('es','eu'):
            shutil.rmtree(m.DATA);m.write(m.DATA/'preferencias.json',{'idioma':language})
            a,s,w=m.start(m.available()[9])
            subprocess.run(['bash','-c','''mkdir -p expediente/informes expediente/copias cuarentena
cp fuentes/aviso.txt expediente/copias/
cp fuentes/normas.txt expediente/protocolo.txt
whoami > expediente/informes/operador.txt
uname -n > expediente/informes/equipo.txt
uname -r > expediente/informes/nucleo.txt
uname -m > expediente/informes/arquitectura.txt
whereis date uname > expediente/informes/herramientas.txt
mv archivo/paquetes/resumen.txt cuarentena/incidencia.txt
touch expediente/listo.txt
'''],cwd=w,check=True)
            (w/'expediente/informes/reunion.txt').write_text(query('cal_fijo'))
            (w.parent/'alias_comprobacion.txt').write_text("alias resumen='uname -o; uname -n'\n")
            s['sesion_paso']='old'
            with patch.object(retos,'query',side_effect=query),patch.dict(os.environ,{'LA_SESSION_ID':'new'}):
                for t in a['pasos'][-1]['pruebas']:self.assertTrue(m.check_test(t,a,s,w),t)
                (w/'expediente/copias/aviso.txt').write_text('falso')
                copy_test=next(t for t in a['pasos'][-1]['pruebas'] if t.get('ruta')=='expediente/copias/aviso.txt')
                self.assertFalse(m.check_test(copy_test,a,s,w))
                (w/'expediente/listo.txt').write_text('no vacío')
                self.assertFalse(m.check_test({'tipo':'vacio','ruta':'expediente/listo.txt'},a,s,w))

if __name__=='__main__': unittest.main()
