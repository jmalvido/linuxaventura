# LinuxAventura 0.1 — primera versión para probar

Juego educativo para terminal REAL de Ubuntu. Python coordina las misiones;
Bash ejecuta los comandos del alumno. Castellano y euskera seleccionables.
No utiliza pip, servicios externos ni inteligencia artificial durante el juego.

## Prueba rápida en tu máquina virtual Ubuntu

Descomprime el paquete y coloca la carpeta `linuxaventura` en tu HOME.
No copies el juego en carpetas del sistema ni lo ejecutes como root.

```bash
cd ~/linuxaventura
bash jugar.sh
```

Requisitos: Linux, Bash y Python 3.8 o posterior. Si falta Python:

```bash
sudo apt update
sudo apt install python3
```

El juego no necesita sudo. Cada alumno usa su propia copia en su HOME.
La primera ejecución pregunta el idioma; después aparece un menú libre.
Introduce 1, 2, 3 o 4. Los nombres de archivos se mantienen iguales en ambos
idiomas para facilitar las instrucciones compartidas; su contenido se traduce.

## Cómo jugar

Lee el paso y trabaja con comandos reales. Escribe los comandos propios en MAYÚSCULAS:

| Comando | Resultado |
|---|---|
| COMPROBAR | Revisa el paso. Algunas pruebas preguntan lo que has leído. |
| PISTA | Primera orientación; al repetir, ayuda más concreta. |
| AYUDA | Explica el funcionamiento y vuelve a mostrar el objetivo. |
| REINICIAR | Pide escribir REINICIAR de nuevo y reconstruye solo esa actividad. |
| MENU | Vuelve al menú sin borrar trabajo. |
| ACTUALIZAR | Descarga nuevos archivos de actividades y nuevas versiones. |
| SALIR | Cierra el juego. |

En el menú: número de actividad, ACTUALIZAR, IDIOMA, AYUDA o SALIR.
IDIOMA cambia los textos del juego; los archivos de un escenario ya creado
conservan el idioma con el que se generaron para no sobrescribir el trabajo.
Para regenerarlos en otro idioma, cambia el idioma y usa REINICIAR.

Las pistas con rutas relativas parten de la raíz del escenario, salvo que el
paso indique otra ubicación. Si te pierdes, AYUDA muestra el objetivo;
la carpeta está en `~/linuxaventura/datos/actividad_00N/escenario`.

El progreso se guarda tras COMPROBAR y las pistas también se recuerdan.
Los archivos existen realmente en disco; guarda los cambios de tu editor.
La última carpeta dentro del escenario se recuerda al regresar al prompt y salir.
Ctrl+C cancela una orden; Ctrl+D o `exit` vuelven al menú desde Bash.

## Actividades incluidas

1. Bienvenido a Linux: pwd, ls, cat (4 pasos).
2. Bienvenido a Linux: cd, rutas, cd .., ls -a (4 pasos).
3. Bienvenido a Linux: mkdir, cp, mv, touch (5 pasos).
4. Encuentra el virus: investigación y repaso, sin comandos visibles salvo pistas (5 pasos).

Cada actividad es independiente. La cuarta utiliza solo textos inofensivos.
El motor comprueba resultados, no que se haya usado una secuencia concreta.
Las respuestas de lectura aceptan mayúsculas/minúsculas y espacios exteriores.
Los archivos y directorios reales sí respetan las reglas de Linux.
No es una plataforma de examen: quien inspeccione los JSON puede ver soluciones.

## Subir a un único repositorio GitHub

Esta entrega NO crea ni publica un repositorio. Elige un repositorio público
para que el alumnado pueda descargar sin autenticación. Sube el CONTENIDO de
`linuxaventura` a la raíz del repositorio, no la carpeta que lo contiene.
No subas `datos/`: incluye trabajo y progreso personales. `.gitignore` la excluye
si utilizas Git; si subes mediante la web, exclúyela manualmente.

Antes de subir, edita `config.json`:

```json
{
  "url_base": "https://raw.githubusercontent.com/USUARIO/REPOSITORIO/main"
}
```

Sustituye USUARIO, REPOSITORIO y, si procede, la rama `main`.
La URL debe apuntar a la carpeta que contiene catalogo.json.
Ejecuta:

```bash
python3 publicar_catalogo.py
```

Sube motor.py, menu.py, jugar.sh, terminal.bash, config.json, catalogo.json,
actividades/, publicar_catalogo.py, README.md y los demás documentos deseados.
Los tests y la guía de profesor son opcionales para la distribución a estudiantes.

### Primera descarga con wget

Cuando esté publicado, sustituye los marcadores en estas órdenes:

```bash
cd ~
wget -O linuxaventura-main.tar.gz https://github.com/USUARIO/REPOSITORIO/archive/refs/heads/main.tar.gz
tar -xzf linuxaventura-main.tar.gz
mv REPOSITORIO-main linuxaventura
bash ~/linuxaventura/jugar.sh
```

Hazlo en una instalación nueva, donde NO exista `~/linuxaventura`.
Para una instalación existente utiliza ACTUALIZAR; no extraigas encima de ella.
También puedes descargar cualquier archivo individual usando su URL Raw:

```bash
wget -O ~/linuxaventura/actividades/actividad_005.json https://raw.githubusercontent.com/USUARIO/REPOSITORIO/main/actividades/actividad_005.json
```

Este último ejemplo solo funcionará cuando crees y publiques la actividad 005.

## ACTUALIZAR: alcance de esta versión

Lee catalogo.json desde la URL configurada, descarga los JSON y verifica sus
SHA-256 y estructura antes de incorporarlos. La conexión usa HTTPS.
No descarga ni ejecuta código Python/Bash remoto. Solo actualiza actividades;
las ampliaciones del MOTOR se distribuirán en otra versión del programa.
Una actividad nueva o no empezada usa la última definición disponible.
Cada actividad iniciada conserva una copia de su definición, incluso completada;
REINICIAR adopta la versión nueva y reconstruye su escenario previa confirmación.
Si no hay Internet o el repositorio aún no está configurado, se puede seguir jugando.
El hash detecta descargas incoherentes; no autentica a un autor distinto del repositorio.

## Añadir actividades

Consulta docs/CREAR_ACTIVIDADES.md. Un JSON por actividad; el menú no se edita.
Al modificar una actividad publicada aumenta `version`, regenera catalogo.json
con publicar_catalogo.py y sube ambos archivos.

## Datos, límites y recuperación

- `actividades/`: definiciones descargables.
- `datos/actividad_00N/actividad.json`: versión fijada al iniciar.
- `datos/actividad_00N/estado.json`: paso, pistas, idioma inicial y última carpeta.
- `datos/actividad_00N/escenario/`: archivos reales del alumno.
- `datos/actividad_00N/historial`: historial de comandos de esa actividad.
- `datos/preferencias.json`: idioma del menú.

Haz copia de `datos/` si quieres conservar el trabajo antes de una prueba importante.
REINICIAR borra solo el escenario y el avance de la actividad actual, no las demás.
El historial se conserva. El menú evita dos sesiones simultáneas en la misma copia.
No se modifica ~/.bashrc, ni se instalan comandos globales.
Esto NO es un contenedor de seguridad: un comando fuera del escenario puede afectar
a otros archivos del usuario. Para el aula se ha diseñado para una VM individual.
Los mensajes de los comandos Linux usan el idioma del sistema operativo.
Windows nativo todavía no está implementado; esta entrega se prueba en Ubuntu/Linux.
La estructura de actividades puede reutilizarse en una futura adaptación.

## Pruebas del motor

```bash
python3 -m unittest discover -s tests -v
```

Las pruebas usan directorios temporales, no el progreso de tu instalación.
