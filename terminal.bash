# Bash real. No sustituye ni modifica ~/.bashrc.
COMPROBAR() { "$LA_PYTHON" "$LA_ROOT/motor.py" check; }
PISTA() { "$LA_PYTHON" "$LA_ROOT/motor.py" hint; }
AYUDA() { "$LA_PYTHON" "$LA_ROOT/motor.py" help; }
ACTUALIZAR() { "$LA_PYTHON" "$LA_ROOT/motor.py" update; }
MENU() { exit 0; }
SALIR() { exit 42; }
REINICIAR() {
    builtin cd "$LA_ROOT" || return
    "$LA_PYTHON" "$LA_ROOT/motor.py" reset
    local destino
    destino=$("$LA_PYTHON" "$LA_ROOT/motor.py" path) || return
    builtin cd "$destino"
}
_la_record() { "$LA_PYTHON" "$LA_ROOT/motor.py" remember "$PWD"; }
PROMPT_COMMAND=_la_record
trap '_la_record' EXIT
HISTFILE="$LA_HISTORY"
HISTSIZE=2000
HISTFILESIZE=4000
shopt -s histappend
PS1='[LinuxAventura \W] \$ '
unset BASH_ENV ENV
"$LA_PYTHON" "$LA_ROOT/motor.py" show
