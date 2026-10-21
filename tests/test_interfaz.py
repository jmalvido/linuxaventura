import contextlib
import io
import os
import sys
from pathlib import Path
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import interfaz as ui

class ScreenTests(unittest.TestCase):
    def test_redirected_output_is_plain(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            ui.clear()
            print(ui.highlight('Ejecuta COMPROBAR y ls'))
        self.assertNotIn('\033',out.getvalue())
    def test_terminal_clear_and_color(self):
        with patch.object(ui,'terminal',return_value=True), patch.dict(os.environ,{'TERM':'xterm','LA_CLEAR':'1'},clear=True), contextlib.redirect_stdout(io.StringIO()) as out:
            ui.clear()
            print(ui.highlight('COMPROBAR\n  ls -a'))
        value=out.getvalue()
        self.assertTrue(value.startswith('\033[2J\033[H'))
        self.assertIn('\033[1;33mCOMPROBAR\033[0m', value)
        self.assertNotIn('\033[3J',value)
    def test_optional_plain_mode(self):
        with patch.object(ui,'terminal',return_value=True), patch.dict(os.environ,{'NO_COLOR':'1','LA_CLEAR':'0'}), contextlib.redirect_stdout(io.StringIO()) as out:
            ui.clear(); print(ui.highlight('PISTA'))
        self.assertEqual(out.getvalue(),'PISTA\n')
