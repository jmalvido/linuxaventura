# LinuxAventura

LinuxAventura es un juego para aprender comandos de Linux resolviendo pequeñas misiones en una terminal real. Leerás mensajes, explorarás carpetas, buscarás pistas y organizarás archivos para avanzar.

Puedes jugar en **castellano o euskera**. Cada actividad es independiente y puedes elegirla desde el menú:

1. **Bienvenido a Linux: tus primeros pasos.** Aprende `pwd`, `ls` y `cat`.
2. **Bienvenido a Linux: explora las carpetas.** Practica `cd`, las rutas y `ls -a`.
3. **Bienvenido a Linux: organiza tus archivos.** Utiliza `mkdir`, `cp`, `mv` y `touch`.
4. **Encuentra el virus.** Resuelve una investigación aplicando lo aprendido. El virus es un archivo de texto inofensivo.

Se irán añadiendo nuevas actividades durante el curso.

## Cómo descargar y jugar en una máquina virtual

Utiliza una **máquina virtual con Ubuntu**. Abre la terminal dentro de Ubuntu y realiza estos pasos con tu usuario habitual. Esta versión no se ejecuta directamente en PowerShell de Windows.

### 1. Prepara Ubuntu

Instala Python 3 y wget si todavía no los tienes:

```bash
sudo apt update
sudo apt install python3 wget
```

### 2. Descarga el juego

Para la primera instalación, copia y ejecuta estas órdenes en la terminal:

```bash
cd ~
wget -O linuxaventura.tar.gz https://github.com/jmalvido/linuxaventura/archive/refs/heads/main.tar.gz
tar -xzf linuxaventura.tar.gz
mv linuxaventura-main linuxaventura
```

El juego quedará en la carpeta `linuxaventura` de tu HOME. Si ya tienes esa carpeta, no repitas la instalación: abre el juego y usa `ACTUALIZAR` para descargar nuevas actividades.

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

El progreso se guarda automáticamente al superar cada paso. Los archivos y carpetas que crees también se conservan. Si utilizas un editor, recuerda guardar los cambios en él.

En el menú verás si cada actividad está **sin empezar**, **en curso** o **completada**. Puedes continuar otro día o repetir una actividad con `REINICIAR`.

Las actualizaciones conservan tu trabajo. Si cambia una actividad que ya habías iniciado, seguirás con su versión anterior hasta que decidas reiniciarla. Una vez descargadas, las actividades se pueden jugar sin conexión.

### Consejos para empezar

- Pulsa **Intro** después de cada comando.
- No escribas el símbolo `$` que pueda aparecer al principio de la línea de la terminal.
- Los comandos de Linux, como `ls` o `mkdir`, se escriben normalmente en minúsculas.
- Los nombres de archivos distinguen mayúsculas y minúsculas.
- Usa `pwd` para saber dónde estás y `ls` para ver qué hay en esa carpeta.
- Trabaja dentro del escenario de la actividad y no uses `sudo` para jugar. La terminal es real y tus órdenes pueden afectar a otros archivos si sales del escenario.
