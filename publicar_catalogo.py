#!/usr/bin/env python3
"""Ejecutar tras añadir/modificar JSON y antes de subir a GitHub."""
import hashlib
import motor as m
entries=[]
for p in sorted(m.CATALOG.glob('*.json')):
    a=m.validate(m.read(p))
    if p.name!=a['id']+'.json': raise ValueError('El nombre debe coincidir con el ID: '+p.name)
    entries.append({'archivo':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
if len({e['archivo'] for e in entries})!=len(entries): raise ValueError('ID repetido')
m.write(m.ROOT/'catalogo.json',{'schema':1,'actividades':entries})
print('Catálogo generado:',len(entries))
