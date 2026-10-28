# Guía de prueba y soluciones — versiones 0.1–0.3

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


# Ampliación de la unidad — versión 0.3

Basada en «3.1- Intro de Linux en comandos.pdf» y «3.1.1- Actividades de Linux en comandos - copia.odt».
Se mantienen las cuatro primeras actividades y se añaden seis juegos más y un extra.

| Juego | Objetivo | Etapas | Tiempo orientativo |
|---|---|---|---|
| 5. La agenda perdida | date, formatos, cal, man cal, lunes | 5 | 20–30 min |
| 6. ¿Quién está al mando? | who, whoami y opciones de uname | 5 | 20–30 min |
| 7. La biblioteca del terminal | man, info, whereis, Tab, espacios, prompt y clear | 5 | 20–30 min |
| 8. Atajos para el turno | alias, secuencias con ; y unalias | 5 | 25–35 min |
| 9. El relevo del operador | history, history -c, passwd conceptual y exit | 4 | 15–25 min |
| 10. Operación IZAR | Repaso integrado y redirección > guiada | 12 | 45–70 min |
| Extra (11) | Definición → comando | 27 | 15–25 min |

Los tiempos son estimaciones didácticas, no límites del juego. El alumnado puede pedir pistas y repetir sin penalización.
Las tres primeras actividades siguen siendo tutoriales. El juego 4 conserva su misión de virus ficticio.

## Preparación del aula

En Ubuntu: `sudo apt update` y `sudo apt install python3 wget ncal man-db info`.
No se necesita sudo para jugar. No se debe lanzar el juego con root.
El motor muestra un aviso antes de abrir una actividad si falta cal, man o info.

## Cobertura y decisiones didácticas

- date: consulta y formato `+%d %m %A` en juegos 5 y 10.
- cal: tres meses, año completo, mes concreto, semana desde lunes en 5 y 10.
- who y who -a: sesiones registradas en 6 y 10; salida vacía permitida.
- whoami: identidad en 6, alias en 8 e informes en 10.
- man e info: consulta real registrada en 5, 7, 9 y 10.
- clear: juego 7 y alias; la interfaz también limpia etapas.
- whereis: binarios/manuales y consultas múltiples en 7 y 10.
- uname: -s, -n, -r, -v, -m, -p, -i, -o y -a en 6; aplicación en 10.
- alias y unalias: quien, meses, conectados, equipo en 8; turno y resumen en 10.
- passwd: manual e identificación, sin cambio de contraseña real, en 9, 10 y extra.
- history/history -c y exit: práctica en 9 y final 10.
- Prompt, Tab, espacios y flechas: explicación y práctica en 7 y 9.
- Sintaxis y argumentos: aparecen en todas las misiones; `;` se explica en alias.
- Ampliación final: `>` guarda resultados. No se exige un script, permisos ni administración ajena al temario.

## Qué comprueba realmente

Los archivos se comparan con los originales o con consultas de lectura de la máquina actual.
Los alias se inspeccionan en el Bash del alumno; se admiten espacios y comillas equivalentes y secuencias con ; o && indicadas en las pruebas.
Algunas consultas se verifican en el historial, con la orden completa y en una línea separada.
Esto prueba que la orden se escribió, no que el alumno entendió su salida ni que finalizó sin error.
No se registran pulsaciones: Tab y flechas se practican, pero no se certifican automáticamente.
La prueba de salida detecta una sesión nueva, no distingue exit de MENU o Ctrl+D.
Los JSON y los ficheros de progreso son accesibles: no es un sistema de evaluación antifraude.

## Particularidades de Ubuntu

- En el cal del paquete ncal, -m selecciona mes; para lunes se propone `ncal -b -M`.
  En util-linux cal puede usarse `cal -m`. Se explica la diferencia.
- `uname -p` y `uname -i` pueden mostrar unknown. No se fuerza un procesador concreto.
- Las respuestas de sistema se comparan con esa VM; no hay usuarios, hostnames ni versiones fijados.
- Las fechas se comparan con el reloj y el idioma de la VM. Si cambia el día entre consulta y comprobación, repite la consulta.
- Los calendarios del expediente usan febrero de 2028 para obtener un resultado estable: tiene 29 días.

## Guardado y compatibilidad

Las actividades 1–4 conservan sus IDs y versiones: no se obliga a reiniciarlas.
Los alias se guardan por actividad y se restauran al volver. Los creados en otra terminal no cuentan.
Se utiliza un historial separado, que se guarda en cada prompt. history -c limpia el de la actividad.
REINICIAR borra escenario, progreso, alias e historial de la actividad actual.
No se modifica ~/.bashrc ni el historial habitual del usuario.

## Soluciones de las actividades nuevas

Las órdenes con rutas relativas se ejecutan desde la raíz del escenario, salvo indicación expresa.
Los valores pedidos de uname, whoami y date dependen de cada máquina: copiar su salida completa.

### La agenda perdida — Fecha y calendario

**Paso 1.** Lee LEEME.txt. Ejecuta date para consultar la fecha del sistema. Después prueba date +%Y-%m-%d. Al escribir COMPROBAR introduce la fecha con formato año-mes-día. No cambies el reloj.

```text
date
date +%Y-%m-%d
COMPROBAR
```

**Paso 2.** Necesitas ver el mes anterior, el actual y el siguiente. Consulta man cal y prueba cal -3. Sal del manual con q. Después COMPROBAR: se revisará la orden que has probado.

```text
man cal
cal -3
COMPROBAR
```

**Paso 3.** La reunión es en febrero de 2028. Muestra ese calendario y averigua cuántos días tiene. Usa mes y año como argumentos de cal. Después COMPROBAR.

```text
cal 2 2028
COMPROBAR → 29
```

**Paso 4.** Para organizar todo el curso, muestra el año actual completo con cal -y. Después muestra un calendario con semanas que empiecen en lunes. En Ubuntu con ncal: ncal -b -M. En cal de util-linux: cal -m. Consulta man cal para elegir la opción de tu versión. COMPROBAR.

```text
cal -y
ncal -b -M
COMPROBAR
```

**Paso 5.** Deja la fecha en una sola línea con día, mes y nombre del día de la semana. Las comillas permiten incluir espacios en el formato. Ejecuta la orden y escribe COMPROBAR para copiar el resultado.

```text
date "+%d %m %A"
COMPROBAR
```


### ¿Quién está al mando? — Usuarios y sistema

**Paso 1.** Lee LEEME.txt. Descubre tu nombre de usuario con whoami. Escribe COMPROBAR y responde con el resultado de tu máquina.

```text
whoami
COMPROBAR
```

**Paso 2.** Consulta who y who -a. Observa las sesiones registradas y la información adicional. Una salida vacía de who puede ser normal en una VM: no significa que no tengas usuario. COMPROBAR preguntará qué comando identifica al usuario que ejecuta una orden.

```text
who
who -a
COMPROBAR → whoami
```

**Paso 3.** La etiqueta debe distinguir núcleo y equipo. Consulta uname -s y uname -n. Escribe COMPROBAR y responde las dos preguntas.

```text
uname -s
uname -n
COMPROBAR
```

**Paso 4.** Consulta la versión del núcleo, su información de compilación y la arquitectura con uname -r, uname -v y uname -m. COMPROBAR pedirá la versión y la arquitectura.

```text
uname -r
uname -v
uname -m
COMPROBAR
```

**Paso 5.** Completa la identificación: prueba uname -p, uname -i, uname -o y uname -a. -p o -i pueden devolver unknown; no es un error del juego. COMPROBAR pedirá el sistema operativo mostrado por -o.

```text
uname -p
uname -i
uname -o
uname -a
COMPROBAR
```


### La biblioteca del terminal — Ayuda y localización

**Paso 1.** Lee LEEME.txt. Abre man whereis. Busca la opción que limita la búsqueda a los ejecutables y sal con q. COMPROBAR pedirá esa opción.

```text
man whereis
COMPROBAR → -b
```

**Paso 2.** Localiza date y uname con whereis. Después consulta whereis -b date para distinguir el ejecutable de su manual. COMPROBAR revisará las consultas.

```text
whereis date uname
whereis -b date
COMPROBAR
```

**Paso 3.** Prueba la otra ayuda del temario: info date. Desplázate por el documento y vuelve con q. Después abre man date para comparar. COMPROBAR pedirá el nombre del segundo sistema de ayuda, distinto de man.

```text
info date
man date
COMPROBAR → info
```

**Paso 4.** Dentro de documentos hay un nombre con espacios. Escribe cat documentos/Inf y pulsa Tab para completarlo; después Intro. También puedes usar comillas. Lee la clave y escribe COMPROBAR. Se comprueba la lectura, no la pulsación de Tab.

```text
cat "documentos/Informe de bienvenida.txt"
COMPROBAR → TABULADOR
```

**Paso 5.** Mira el final de tu prompt. En un prompt convencional, $ suele indicar usuario normal y # root. Limpia la pantalla con clear y escribe COMPROBAR: ¿qué símbolo suele identificar a root? No cambies de usuario.

```text
clear
COMPROBAR → #
```


### Atajos para el turno — Alias

**Paso 1.** Lee LEEME.txt. Crea un alias llamado quien que limpie la pantalla, muestre tu usuario y después la fecha. Para encadenar órdenes usa ; dentro de comillas. Ejemplo: alias nombre='orden1; orden2'. Ejecuta quien en otra línea y COMPROBAR.

```text
alias quien='clear; whoami; date'
quien
COMPROBAR
```

**Paso 2.** Crea meses: debe limpiar la pantalla, mostrar el mes anterior, el actual y el siguiente, y terminar mostrando tu usuario. Ejecútalo y comprueba.

```text
alias meses='clear; cal -3; whoami'
meses
COMPROBAR
```

**Paso 3.** Crea conectados: limpia la pantalla, muestra la fecha y luego las sesiones registradas. Ejecútalo aunque who no muestre ninguna sesión. COMPROBAR.

```text
alias conectados='clear; date; who'
conectados
COMPROBAR
```

**Paso 4.** Crea equipo para mostrar el sistema operativo y después el nombre del equipo. Ejecuta equipo y lista todos los alias con alias. Comprueba que siguen definidos los cuatro atajos.

```text
alias equipo='uname -o; uname -n'
equipo
alias
COMPROBAR
```

**Paso 5.** El turno termina: elimina meses y conectados con unalias. Conserva quien y equipo. Lista los alias y escribe COMPROBAR.

```text
unalias meses conectados
alias
COMPROBAR
```


### El relevo del operador — Historial y sesión

**Paso 1.** Lee LEEME.txt. Ejecuta date, whoami y uname -n. Usa la flecha arriba para recuperar una orden y ejecutarla otra vez. Muestra el historial con history. COMPROBAR verificará las consultas; las teclas no se registran.

```text
date
whoami
uname -n
history
COMPROBAR
```

**Paso 2.** Investiga la orden que cambia la contraseña del usuario actual consultando man passwd. No la ejecutes: basta con identificarla. COMPROBAR pedirá su nombre. Al introducir contraseñas en una terminal normalmente no aparecen caracteres.

```text
man passwd
COMPROBAR → passwd
```

**Paso 3.** Limpia la lista de comandos de ESTA actividad con history -c. Después ejecuta history y COMPROBAR, sin otras órdenes intermedias. Es normal que history y COMPROBAR aparezcan: son órdenes nuevas.

```text
history -c
history
COMPROBAR
```

**Paso 4.** Última prueba: escribe exit para salir de la terminal de la actividad. Volverás al menú del juego. Selecciona otra vez esta actividad y escribe COMPROBAR. Debes retomar este mismo paso; no uses REINICIAR.

```text
exit
MENU: 9
COMPROBAR
```


### Operación IZAR — Misión final de la unidad

**Paso 1.** MISIÓN FINAL. Habrá menos indicaciones y más objetivos que combinar. Lee LEEME.txt, explora el escenario y encuentra la clave oculta. No borres archivos por tu cuenta. COMPROBAR.

```text
cat LEEME.txt
ls -a archivo
cat archivo/.orden.txt
COMPROBAR → IZAR-2028
```

**Paso 2.** En la raíz del escenario crea expediente, con informes y copias dentro, y una carpeta cuarentena fuera de expediente. Copia aviso.txt a copias. Copia normas.txt a expediente y renombra esa copia como protocolo.txt. Conserva los originales. COMPROBAR.

```text
mkdir -p expediente/informes expediente/copias cuarentena
cp fuentes/aviso.txt expediente/copias/
cp fuentes/normas.txt expediente/
mv expediente/normas.txt expediente/protocolo.txt
COMPROBAR
```

**Paso 3.** Pequeña ampliación: > guarda la salida de una orden en un archivo; sustituye su contenido si ya existe. Ejemplo: whoami > expediente/informes/operador.txt. Crea ese informe y otro llamado equipo.txt con el nombre de la máquina. Lee ambos para revisarlos. COMPROBAR.

```text
whoami > expediente/informes/operador.txt
uname -n > expediente/informes/equipo.txt
cat expediente/informes/operador.txt
cat expediente/informes/equipo.txt
COMPROBAR
```

**Paso 4.** Guarda la versión del núcleo en expediente/informes/nucleo.txt y la arquitectura en expediente/informes/arquitectura.txt. Consulta además el nombre del núcleo, la información de compilación, procesador, plataforma, sistema operativo y el resumen completo con uname. Recuerda que unknown puede ser válido. COMPROBAR.

```text
uname -r > expediente/informes/nucleo.txt
uname -m > expediente/informes/arquitectura.txt
uname -s
uname -o
uname -a
uname -v
uname -p
uname -i
COMPROBAR
```

**Paso 5.** El expediente debe incluir febrero de 2028 en informes/reunion.txt. Guarda la salida de cal en ese archivo. Consulta también los tres meses alrededor del actual, el año actual completo y un calendario que empiece en lunes. COMPROBAR.

```text
cal 2 2028 > expediente/informes/reunion.txt
cal -3
cal -y
ncal -b -M
COMPROBAR
```

**Paso 6.** Localiza date y uname en una sola consulta y guarda el resultado en expediente/informes/herramientas.txt. Antes, consulta man whereis e info date para repasar las ayudas. COMPROBAR.

```text
man whereis
info date
whereis date uname > expediente/informes/herramientas.txt
COMPROBAR
```

**Paso 7.** Comprueba la fecha actual y preséntala en una sola línea con día, mes y nombre del día de la semana. Consulta también las sesiones y su información adicional. COMPROBAR pedirá la fecha formateada.

```text
date
date "+%d %m %A"
who
who -a
COMPROBAR
```

**Paso 8.** Crea y prueba dos atajos: turno limpia pantalla, muestra usuario y fecha; resumen muestra el sistema operativo y el nombre de equipo. Lista los alias. COMPROBAR.

```text
alias turno='clear; whoami; date'
alias resumen='uname -o; uname -n'
turno
resumen
alias
COMPROBAR
```

**Paso 9.** Investiga los paquetes usando el aviso. Mueve el archivo sospechoso a cuarentena/incidencia.txt. Conserva intactos los otros paquetes y las evidencias. Mover este texto es solo una simulación, no una desinfección real. COMPROBAR.

```text
cat fuentes/aviso.txt
cat archivo/paquetes/resumen.txt
mv archivo/paquetes/resumen.txt cuarentena/incidencia.txt
COMPROBAR
```

**Paso 10.** Revisa el historial con history. Elimina el alias turno y conserva resumen. Crea expediente/listo.txt vacío. COMPROBAR revisará todo el expediente y preguntará qué comando cambiaría tu contraseña. Identifícalo sin ejecutarlo.

```text
history
unalias turno
touch expediente/listo.txt
COMPROBAR → passwd
```

**Paso 11.** El expediente ya está revisado. Limpia ahora el historial de esta actividad, comprueba que solo quedan las órdenes nuevas y ejecuta COMPROBAR. Si pides una pista, vuelve a limpiarlo antes de comprobar.

```text
history -c
history
COMPROBAR
```

**Paso 12.** Entrega del turno: sal de esta terminal con exit. En el menú vuelve a seleccionar la misión 10 y escribe COMPROBAR. Verificaremos que el expediente sigue completo y el alias resumen se ha conservado. No reinicies la actividad.

```text
exit
MENU: 10
COMPROBAR
```


### EXTRA — Adivina el comando (27 definiciones)

**Paso 1.** DEFINICIÓN 1/27
Muestra la ruta completa de la carpeta actual.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
pwd
```

**Paso 2.** DEFINICIÓN 2/27
Lista los archivos y carpetas.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
ls
```

**Paso 3.** DEFINICIÓN 3/27
Lista también los nombres que empiezan por punto.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
ls -a
```

**Paso 4.** DEFINICIÓN 4/27
Cambia de directorio. Escribe solo el nombre del comando.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
cd
```

**Paso 5.** DEFINICIÓN 5/27
Sube a la carpeta superior.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
cd ..
```

**Paso 6.** DEFINICIÓN 6/27
Muestra el contenido de un archivo de texto.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
cat
```

**Paso 7.** DEFINICIÓN 7/27
Crea directorios.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
mkdir
```

**Paso 8.** DEFINICIÓN 8/27
Copia archivos conservando el original.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
cp
```

**Paso 9.** DEFINICIÓN 9/27
Mueve o renombra archivos.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
mv
```

**Paso 10.** DEFINICIÓN 10/27
Crea un archivo vacío si no existe; si existe, actualiza sus marcas de tiempo.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
touch
```

**Paso 11.** DEFINICIÓN 11/27
Muestra la fecha y la hora actuales.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
date
```

**Paso 12.** DEFINICIÓN 12/27
Muestra un calendario.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
cal
```

**Paso 13.** DEFINICIÓN 13/27
Muestra el mes anterior, el actual y el siguiente.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
cal -3
```

**Paso 14.** DEFINICIÓN 14/27
Muestra las sesiones de usuarios registradas en el sistema.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
who
```

**Paso 15.** DEFINICIÓN 15/27
Muestra el nombre del usuario efectivo actual.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
whoami
```

**Paso 16.** DEFINICIÓN 16/27
Abre páginas del manual de un comando.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
man
```

**Paso 17.** DEFINICIÓN 17/27
Consulta documentación en el sistema de ayuda Info.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
info
```

**Paso 18.** DEFINICIÓN 18/27
Limpia la pantalla de la terminal.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
clear
```

**Paso 19.** DEFINICIÓN 19/27
Localiza binarios, fuentes y páginas de manual de un comando.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
whereis
```

**Paso 20.** DEFINICIÓN 20/27
Define o muestra atajos de comandos.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
alias
```

**Paso 21.** DEFINICIÓN 21/27
Elimina un alias.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
unalias
```

**Paso 22.** DEFINICIÓN 22/27
Muestra información del sistema y del núcleo.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
uname
```

**Paso 23.** DEFINICIÓN 23/27
Muestra el nombre del equipo con una opción de uname.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
uname -n
```

**Paso 24.** DEFINICIÓN 24/27
Cambia la contraseña del usuario actual. Aquí solo debes escribir su nombre como respuesta.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
passwd
```

**Paso 25.** DEFINICIÓN 25/27
Muestra la lista de órdenes del historial de Bash.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
history
```

**Paso 26.** DEFINICIÓN 26/27
Vacía la lista del historial de la sesión.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
history -c
```

**Paso 27.** DEFINICIÓN 27/27
Sale del intérprete de órdenes actual.
Escribe COMPROBAR y, cuando aparezca la pregunta, introduce el comando como texto. No necesitas ejecutarlo.

```text
exit
```


## Verificación realizada

Se mantienen las pruebas de las cuatro actividades iniciales. Se añaden pruebas de respuestas,
alias reales de Bash, historial, salida y reentrada, y conservación/comprobación del expediente
final en castellano y euskera. Dos pruebas usan un pseudoterminal interactivo real.
El entorno de desarrollo no dispone de cal: su salida se simula únicamente en la prueba del
expediente. La visualización del calendario y las páginas interactivas de man/info deben
revisarse en la VM Ubuntu del aula; las opciones de calendario se han contrastado con su manual.

Referencias técnicas:
- https://manpages.ubuntu.com/manpages/noble/man1/cal.1.html
- https://www.gnu.org/software/bash/manual/html_node/Aliases.html
- https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html
