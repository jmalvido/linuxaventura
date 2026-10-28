# LinuxAventura

LinuxAventura es un juego para aprender comandos de Linux resolviendo pequeñas misiones en una terminal real. Leerás mensajes, explorarás carpetas, buscarás pistas y organizarás archivos para avanzar.

Puedes jugar en **castellano o euskera**. Cada actividad es independiente y puedes elegirla desde el menú:

1. **Bienvenido a Linux: tus primeros pasos.** Aprende `pwd`, `ls` y `cat`.
2. **Bienvenido a Linux: explora las carpetas.** Practica `cd`, las rutas y `ls -a`.
3. **Bienvenido a Linux: organiza tus archivos.** Utiliza `mkdir`, `cp`, `mv` y `touch`.
4. **Encuentra el virus.** Resuelve una investigación aplicando lo aprendido. El virus es un archivo de texto inofensivo.

5. **La agenda perdida.** Fecha y calendario.
6. **¿Quién está al mando?** Usuarios e información del sistema.
7. **La biblioteca del terminal.** Manuales, localización de comandos y nombres con espacios.
8. **Atajos para el turno.** Crear, probar y eliminar alias.
9. **El relevo del operador.** Historial, contraseñas y salida de la sesión.
10. **Operación IZAR.** Misión final de 12 etapas que combina toda la unidad.
11. **EXTRA: Adivina el comando.** 27 definiciones para responder con el comando correspondiente.

Son **10 juegos y un extra**. Se irán añadiendo nuevas actividades durante el curso.

## Cómo descargar y jugar en una máquina virtual

Utiliza una **máquina virtual con Ubuntu**. Abre la terminal dentro de Ubuntu y realiza estos pasos con tu usuario habitual. Esta versión no se ejecuta directamente en PowerShell de Windows.

### 1. Prepara Ubuntu

Instala Python 3, wget y las herramientas de calendario y ayuda:

```bash
sudo apt update
sudo apt install python3 wget ncal man-db info
```

### 2. Descarga el juego

Para la primera instalación, copia y ejecuta estas órdenes en la terminal:

```bash
cd ~
wget -O actualizar_linuxaventura.sh https://raw.githubusercontent.com/jmalvido/linuxaventura/main/actualizar_linuxaventura.sh
bash ~/actualizar_linuxaventura.sh
```

El juego quedará en la carpeta `linuxaventura` de tu HOME. El script sirve también para actualizar una instalación existente y conserva el trabajo.

Cuando haya una nueva versión del juego, ciérralo y ejecuta:

```bash
bash ~/actualizar_linuxaventura.sh
```

`ACTUALIZAR`, dentro del juego, descarga solo actividades. Para instalar esta ampliación de la unidad necesitas actualizar el juego completo con el script.

### 3. Empieza a jugar

```bash
cd ~/linuxaventura
bash jugar.sh
```

Elige el idioma y después el número de la actividad. Puedes empezar por cualquiera, aunque se recomienda hacer primero los tres tutoriales.

**Para jugar otro día**, solo necesitas abrir una terminal y ejecutar:

```bash
bash ~/linuxaventura/jugar.sh
```

## Instrucciones del juego

1. Lee la explicación del paso actual.
2. Utiliza los comandos de Linux para resolver la tarea.
3. Escribe `COMPROBAR` cuando creas que has terminado.
4. Si la solución es correcta, pasarás al siguiente paso. Si falta algo, podrás corregirlo y volver a intentarlo.
5. Si te atascas, escribe `PISTA`.

Los comandos propios del juego se escriben **en MAYÚSCULAS**, tanto en castellano como en euskera:

| Comando | Qué hace |
|---|---|
| `COMPROBAR` | Comprueba la tarea o te pregunta la información que has encontrado. |
| `PISTA` | Ofrece una orientación. Si la pides otra vez, recibirás una ayuda más concreta. |
| `AYUDA` | Muestra cómo se juega y recuerda el objetivo actual. |
| `REINICIAR` | Empieza de nuevo la actividad actual. Pide confirmación antes de borrar el trabajo de esa actividad. |
| `MENU` | Vuelve al menú para elegir otra actividad, conservando el trabajo. |
| `ACTUALIZAR` | Descarga las nuevas actividades disponibles desde GitHub. Necesita conexión a Internet. |
| `SALIR` | Cierra el juego conservando el trabajo. |

En el menú puedes escribir `IDIOMA` para cambiar entre castellano y euskera. Los archivos de una actividad ya iniciada conservan su idioma original; para regenerarlos en el nuevo idioma debes usar `REINICIAR`.

### Guardado y continuación

El progreso se guarda automáticamente al superar cada paso. Los archivos, carpetas y alias que crees también se conservan por actividad. Si utilizas un editor, recuerda guardar los cambios en él.

En el menú verás si cada actividad está **sin empezar**, **en curso** o **completada**. Puedes continuar otro día o repetir una actividad con `REINICIAR`.

Las actualizaciones conservan tu trabajo. Si cambia una actividad que ya habías iniciado, seguirás con su versión anterior hasta que decidas reiniciarla. Una vez descargadas, las actividades se pueden jugar sin conexión.

### Consejos para empezar

- Pulsa **Intro** después de cada comando.
- No escribas el símbolo `$` que pueda aparecer al principio de la línea de la terminal.
- Los comandos de Linux, como `ls` o `mkdir`, se escriben normalmente en minúsculas.
- Los nombres de archivos distinguen mayúsculas y minúsculas.
- Usa `pwd` para saber dónde estás y `ls` para ver qué hay en esa carpeta.
- Trabaja dentro del escenario de la actividad y no uses `sudo` para jugar. La terminal es real y tus órdenes pueden afectar a otros archivos si sales del escenario.

### En las actividades nuevas

- Ejecuta cada orden en una línea separada; escribe COMPROBAR después.
- Algunas pruebas comprueban la orden escrita en el historial; otras revisan archivos, alias o respuestas.
- Los alias e historial de cada actividad están separados de los de tu terminal habitual.
- REINICIAR limpia también los alias y el historial de esa actividad.
- Al salir de man o info, pulsa q para volver al juego.
- En el extra, escribe primero COMPROBAR y responde con el comando como texto: no tienes que ejecutarlo.
- La misión final introduce `>` para guardar la salida de una orden en un archivo, con una explicación y pistas.
- No se pide cambiar contraseñas reales: passwd se trabaja mediante consulta e identificación.
