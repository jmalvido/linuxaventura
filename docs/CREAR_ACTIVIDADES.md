# Crear actividades sin editar el menú

1. Copia un JSON de actividades/ y ponle un nuevo nombre, por ejemplo actividad_005.json.
2. Cambia id a actividad_005; conserva schema: 1 y empieza con version: 1.
3. Escribe titulo, final y todos los textos en es y eu.
4. Define carpetas vacías en carpetas y archivos de texto iniciales en archivos.
5. Define pasos. Cada paso tiene texto, pistas (listas es/eu) y pruebas.
6. Ejecuta python3 publicar_catalogo.py: valida y actualiza el índice de descarga.
7. Publica el JSON y catalogo.json. El alumnado ejecuta ACTUALIZAR.

## Tipos de comprobación disponibles

| tipo | Campos | Condición |
|---|---|---|
| respuesta | pregunta (es/eu), respuestas (listas es/eu) | Respuesta escrita aceptada. |
| carpeta | ruta | Existe como directorio. |
| vacio | ruta | Archivo de cero bytes. |
| ausente | ruta | Ya no existe en esa ubicación. |
| contenido | ruta, origen | Su contenido coincide exactamente con el archivo inicial indicado. |

En contenido, origen es una clave de archivos de la misma actividad. No se compara
con una copia del alumno que pueda haber modificado. Las pruebas de un paso deben
cumplirse todas. El campo opcional error (es/eu) proporciona ayuda al fallar.
Las rutas son relativas al escenario. No se permiten rutas absolutas ni .. en los
archivos de definición. {escenario} se sustituye por la ruta real en instrucciones,
pistas y respuestas aceptadas. No hay código ejecutable dentro de los JSON.

Ejemplo de paso:

```json
{
  "texto": {"es": "Crea la carpeta taller y escribe COMPROBAR.", "eu": "Sortu taller karpeta eta idatzi COMPROBAR."},
  "pistas": {
    "es": ["Necesitas crear un directorio.", "Ejecuta mkdir taller desde la raíz del escenario."],
    "eu": ["Direktorio bat sortu behar duzu.", "Exekutatu mkdir taller eszenatokiaren errotik."]
  },
  "pruebas": [{"tipo": "carpeta", "ruta": "taller"}]
}
```

Las actividades empezadas usan la definición guardada en datos, no la descargada.
Para probar tus cambios en una actividad existente usa REINICIAR (borra su trabajo).
Aumenta version cada vez que publiques cambios; ACTUALIZAR no sustituye una versión
por otra con número igual o menor. No cambies el ID de una actividad existente.

Límite de la versión 0.1: estas pruebas cubren navegación y operaciones de archivos.
Permisos, usuarios, procesos, servicios y ejecución/evaluación de scripts necesitarán
nuevos tipos de comprobación en el motor. Los alumnos YA pueden escribir y ejecutar
scripts en la terminal real; su evaluación automática se ampliará cuando la diseñemos.


## Motor 0.3: comprobaciones de la unidad

Las actividades 005–011 llevan `motor_minimo: 3`. Se mantiene schema: 1.

- respuesta_sistema: pregunta es/eu y consulta (clave fija de retos.QUERIES).
- salida: ruta del archivo y consulta cuya salida debe contener.
- alias: nombre y lista valores con secuencias de comandos admitidas.
- sin_alias: nombre que no debe estar definido.
- ejecutado: lista comandos; alguno debe aparecer como orden completa en el historial.
- historial_limpio: admite únicamente history, history -w y COMPROBAR tras limpiar.
- reentrada: requiere una sesión distinta de aquella donde se superó el paso anterior.
- requisitos: lista opcional de ejecutables que el menú comprueba antes de entrar.

retos.py solo ejecuta consultas de lectura de una lista fija. Los JSON no se ejecutan como código.
Las pruebas basadas en historial son para práctica guiada; el historial puede manipularse.
