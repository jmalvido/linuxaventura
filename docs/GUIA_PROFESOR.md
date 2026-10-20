# Guía de prueba y soluciones — versión 0.1

Primera prueba recomendada: completa la actividad 1 en castellano, sal con MENU,
entra en la 3, crea una carpeta y sal con SALIR. Vuelve a abrir para comprobar
que se mantienen paso y archivos. Prueba Euskera mediante IDIOMA en el menú.
La 4 funciona aunque no se hayan completado las anteriores.

## Actividad 1

- pwd → COMPROBAR: introducir la ruta completa real del escenario.
- ls → COMPROBAR: LEEME.txt.
- cat LEEME.txt → COMPROBAR: KAIXO.
- cat mensaje.txt → COMPROBAR: IZAR.

Las preguntas demuestran acceso a la información, no que se haya ejecutado
obligatoriamente un comando. No se vigila ni califica el historial.

## Actividad 2

Desde la raíz de su escenario:

```bash
cat LEEME.txt
cd centro
pwd
ls
cat entrada.txt
COMPROBAR
```

Respuesta: ALEX. Después:

```bash
cd archivo
cat nota.txt
COMPROBAR
```

Respuesta: NORTE. Después:

```bash
ls
ls -a
cat .pista.txt
COMPROBAR
```

Respuesta: LUNA. Después:

```bash
cd ..
pwd
ls
COMPROBAR
```

Respuesta: entrada.txt.

## Actividad 3

Todas las órdenes desde la raíz del escenario:

```bash
mkdir refugio
mkdir refugio/copias
COMPROBAR
cp documentos/mapa.txt refugio/copias/
COMPROBAR
mv refugio/copias/mapa.txt refugio/copias/plano.txt
COMPROBAR
mv refugio/copias/plano.txt refugio/plano.txt
COMPROBAR
touch refugio/listo.txt
cp documentos/normas.txt refugio/copias/
COMPROBAR
```

Se comprueba contenido, conservación de originales, desaparición de nombres
anteriores y que listo.txt esté vacío. Crear archivos falsos con los nombres
esperados no basta para superar las pruebas de contenido.

## Actividad 4

Desde la raíz del escenario:

```bash
cat LEEME.txt
cat informes/aviso.txt
COMPROBAR
```

Respuesta: IZAR-17.

```bash
ls -a almacen
cat almacen/.mantenimiento.txt
ls almacen/respaldos
cat almacen/respaldos/respaldo.txt
cat almacen/respaldos/actualizacion.txt
cat almacen/respaldos/antivirus.txt
COMPROBAR
```

Respuesta: actualizacion.txt. La marca correcta es SOMBRA-73.

```bash
mkdir evidencias
cp informes/aviso.txt evidencias/
COMPROBAR
mkdir cuarentena
mv almacen/respaldos/actualizacion.txt cuarentena/sospechoso.txt
COMPROBAR
touch evidencias/resuelto.txt
COMPROBAR
```

La última comprobación revisa la evidencia, el original, la cuarentena, la ausencia
del sospechoso en su ubicación inicial y la conservación de los otros respaldos.
No es una práctica de eliminación de malware real.

## Qué observar durante el piloto

- ¿Los mensajes de cada paso son suficientemente breves y claros?
- ¿Entienden la diferencia entre comandos Linux y comandos del juego?
- ¿Comprenden desde qué carpeta ejecutar las rutas relativas?
- ¿La segunda pista ayuda sin eliminar por completo el reto?
- ¿La misión 4 obliga a leer y razonar, o resulta demasiado directa?

No hay nota ni límite de intentos. Se guardan el paso actual y las pistas solicitadas.
Al distribuir a estudiantes puedes omitir esta guía; las definiciones JSON siguen
siendo accesibles, por lo que no debe utilizarse como examen protegido.
