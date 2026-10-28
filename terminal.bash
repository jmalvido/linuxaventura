# Bash real. No sustituye ni modifica ~/.bashrc.
COMPROBAR() {
    builtin alias -p > "$LA_ROOT/datos/$LA_ID/alias_comprobacion.txt"
    HISTTIMEFORMAT= builtin history > "$LA_ROOT/datos/$LA_ID/historial_comprobacion.txt"
    "$LA_PYTHON" "$LA_ROOT/motor.py" check
}
PISTA() { "$LA_PYTHON" "$LA_ROOT/motor.py" hint; }
AYUDA() { "$LA_PYTHON" "$LA_ROOT/motor.py" help; }
ACTUALIZAR() { "$LA_PYTHON" "$LA_ROOT/motor.py" update; }
MENU() { exit 0; }
SALIR() { exit 42; }
REINICIAR() {
    builtin cd "$LA_ROOT" || return
    "$LA_PYTHON" "$LA_ROOT/motor.py" reset
    if [[ ! -f "$LA_ROOT/datos/$LA_ID/alias_guardados.sh" ]]; then
        builtin unalias -a
        builtin history -c
    fi
    local destino
    destino=$("$LA_PYTHON" "$LA_ROOT/motor.py" path) || return
    builtin cd "$destino"
}
_la_record() {
    "$LA_PYTHON" "$LA_ROOT/motor.py" remember "$PWD"
    builtin alias -p > "$LA_ROOT/datos/$LA_ID/alias_guardados.sh"
    builtin history -w "$LA_HISTORY"
}
PROMPT_COMMAND=_la_record
trap '_la_record' EXIT
HISTFILE="$LA_HISTORY"
HISTCONTROL=
HISTIGNORE=
HISTTIMEFORMAT=
HISTSIZE=2000
HISTFILESIZE=4000
shopt -s histappend
# Solo recupera alias locales del alumno; no proceden de las actividades descargadas.
if [[ -f "$LA_ROOT/datos/$LA_ID/alias_guardados.sh" ]]; then
    builtin source "$LA_ROOT/datos/$LA_ID/alias_guardados.sh"
fi
if [[ -t 1 && ${TERM:-dumb} != dumb && ! ${NO_COLOR+x} ]]; then
    PS1='\[\e[1;36m\][LinuxAventura\[\e[0m\] \[\e[1;34m\]\W\[\e[0m\]\[\e[1;36m\]]\[\e[0m\] \[\e[1;32m\]\$\[\e[0m\] '
else
    PS1='[LinuxAventura \W] \$ '
fi
unset BASH_ENV ENV
"$LA_PYTHON" "$LA_ROOT/motor.py" show
