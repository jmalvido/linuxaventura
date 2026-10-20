#!/usr/bin/env bash
set -e
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if ! command -v python3 >/dev/null; then
    echo 'Necesitas Python 3 / Python 3 behar duzu: sudo apt install python3'
    exit 1
fi
exec python3 menu.py
