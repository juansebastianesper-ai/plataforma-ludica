# Taller 8: especificación, modelo de datos y actividades

Curso: Lógica y programación. Mecánica: Niveles.

La sesión se inició con la instrucción global del Taller 8 aportada por el desarrollador. El prompt operativo de cada actividad se reproduce abajo tal como se ejecutó, adaptado desde `prompts-taller-8.md` al curso y la mecánica propios.

## Especificación

**Objetivo:** redactar `specs/spec.md` con las seis historias del MVP.

**Herramienta y modelo:** OpenCode con el modelo Big Pickle (`opencode/big-pickle`). No se usó Copilot.

**Prompt:**

```
## Rol
Actúa como analista de requisitos de software.

## Objetivo
Redactar en specs/spec.md la especificación del MVP de la plataforma, con la estructura que ya tiene ese archivo.

## Contexto
Lee AGENTS.md, specs/encargo.md, specs/ficha-mecanica.md, specs/dudas-encargo.md y specs/respuestas-cliente.md. Cuando una respuesta del cliente contradiga un supuesto de dudas-encargo.md, prevalece la respuesta del cliente.

## Restricciones
- Incluye exactamente estas seis historias de usuario:
  H1. El docente gestiona las actividades del curso.
  H2. La plataforma inicia con contenido del curso.
  H3. El niño entra con el código de la clase, su alias y un avatar.
  H4. El niño resuelve una actividad y sabe de inmediato si acertó.
  H5. La plataforma aplica la regla de la mecánica.
  H6. El docente consulta el progreso de cada niño.
- Cada historia tiene al menos dos criterios Dado/Cuando/Entonces, con los valores exactos de specs/respuestas-cliente.md.
- Todas las actividades son preguntas con 3 o 4 opciones y una respuesta correcta. Los demás tipos de actividad del encargo van en la sección Fuera de alcance.
- Las dudas que no responde el cliente van en Dudas abiertas, con el supuesto de dudas-encargo.md.
- No agregues funcionalidades que no estén en los documentos.
- En la tabla de Dudas abiertas, la columna Respuesta del cliente se renombra como Supuesto, porque esas dudas no tienen respuesta del cliente.
- Modifica solo specs/spec.md.

## Formato de salida
Antes de escribir, muestra la lista de historias con sus criterios resumidos en una línea cada uno y espera mi aprobación.

## Ejemplo
H5. Como niño, quiero desbloquear niveles con mis aciertos, para avanzar por el camino de retos.
- Dado que el niño acierta 4 de 5 preguntas, cuando termina la actividad, entonces se abre el siguiente nivel.
- Dado que el niño acierta 3 de 5, cuando termina la actividad, entonces el siguiente nivel sigue cerrado y puede repetir.

## Criterio de éxito
Las seis historias tienen al menos dos criterios cada una y ningún criterio usa términos vagos como rápido, fácil o adecuado.
```

**Resultado:** se presentó el borrador de H1–H6 con los criterios resumidos; el desarrollador lo aprobó antes de escribir. Se redactaron las seis historias con 6, 3, 3, 3, 5 y 3 criterios respectivamente. H5 usa 80 %, 4 de 5 y 3 de 5, y añade que un nivel abierto no se cierra y que el docente ve el mejor porcentaje. No hubo que corregir criterios tras la aprobación.

## Modelo de datos

**Objetivo:** crear los cinco modelos, `app/db.py` y el diagrama entidad-relación.

**Herramienta y modelo:** OpenCode con el modelo Big Pickle (`opencode/big-pickle`).

**Prompt:**

```
## Rol
Actúa como desarrollador backend con experiencia en FastAPI y SQLModel.

## Objetivo
Crear el modelo de datos del MVP y la conexión con la base de datos:
1. En app/modelos/__init__.py, los modelos de tabla Clase, Nino, Actividad, Pregunta e Intento, con los campos del contrato.
2. En app/db.py, la variable motor, la función crear_tablas() y la dependencia obtener_sesion(), que entrega una sesión por petición.
3. En app/main.py, un ciclo de vida (lifespan) que llame a crear_tablas() al iniciar la aplicación.
4. En specs/plan.md, el diagrama entidad-relación en Mermaid, dentro de la sección Modelo de datos.

## Contexto
Lee AGENTS.md, specs/spec.md, specs/plan.md y app/main.py.
Contrato de datos:
- Clase: id, nombre, codigo (texto de 6 caracteres, único).
- Nino: id, alias, avatar, clase_id (clave foránea a Clase).
- Actividad: id, titulo, descripcion (texto opcional, vacío por defecto), orden (entero).
- Pregunta: id, enunciado, opciones (lista de textos), respuesta_correcta, actividad_id (clave foránea a Actividad).
- Intento: id, nino_id, actividad_id, aciertos, total, duracion_segundos, fecha (fecha y hora).

## Restricciones
- Usa exactamente los nombres de clases y campos del contrato.
- Guarda opciones en una columna JSON.
- La URL de la base de datos se lee de la variable de entorno DATABASE_URL, con el valor por defecto sqlite:///./plataforma.db.
- No agregues dependencias: sqlmodel ya está en requirements.txt.
- No crees endpoints ni modifiques las pruebas.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos y espera mi aprobación.

## Ejemplo
Pregunta(enunciado="¿Qué instrucción mueve al robot hacia delante?", opciones=["Avanzar", "Girar", "Repetir"], respuesta_correcta="Avanzar", actividad_id=1)

## Criterio de éxito
python -m pytest -v pasa todas las pruebas existentes, ruff check . no reporta errores y el comando python -c "import app.main" termina sin errores. No dejes ningún servidor en ejecución. Si después de 3 intentos no se cumple, detente y explica el problema.
```

**Resultado:** se crearon las cinco tablas con `opciones JSON`, `codigo` único de seis caracteres y las cuatro claves foráneas. `crear_tablas()` importa los modelos antes de `create_all`, por lo que aparecen las cinco sentencias `CREATE TABLE`. Se corrigió el orden de importación de `sqlalchemy` para Ruff (I001). El argumento `echo=True` se usó solo para verificar el SQL y se retiró después.

## API de actividades

**Objetivo:** implementar el CRUD de actividades hasta que pasen las pruebas de aceptación.

**Herramienta y modelo:** OpenCode con el modelo Big Pickle (`opencode/big-pickle`).

**Prompt:**

```
## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Pydantic y SQLModel.

## Objetivo
Implementar el CRUD completo de actividades en app/esquemas.py, app/servicios/actividades.py, app/rutas/actividades.py y app/main.py, hasta que pasen las pruebas de aceptación.

## Contexto
Lee AGENTS.md, specs/spec.md, app/db.py, app/modelos/__init__.py, app/main.py y tests/aceptacion/test_actividades.py. El contrato exige:
- GET /api/actividades devuelve la lista ordenada por orden, con sus preguntas.
- POST /api/actividades responde 201 con el id de la actividad y de cada pregunta.
- GET, PUT y DELETE /api/actividades/{actividad_id} responden 200, 200 y 204; 404 si no existe.
- PUT reemplaza las preguntas anteriores; DELETE elimina actividad y preguntas.
- Validaciones: título no vacío, mínimo 5 preguntas, de 3 a 4 opciones por pregunta y respuesta correcta incluida en las opciones. Cualquier fallo responde 422.
- La ruta se registra con el tag Actividades.

## Restricciones
- La lógica de negocio va en app/servicios/actividades.py; las rutas solo reciben la petición y llaman al servicio.
- El cuerpo se valida con esquemas de Pydantic, no con modelos de tabla.
- La sesión se declara con Annotated[Session, Depends(obtener_sesion)].
- No modifiques ningún archivo de tests ni agregues dependencias.
- No dejes servidores en ejecución al terminar.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos y espera mi aprobación.

## Ejemplo
@router.post("/api/actividades", response_model=ActividadRespuesta, status_code=201)
def crear_actividad(datos: ActividadCrear, sesion: Annotated[Session, Depends(obtener_sesion)]):
    return servicio_actividades.crear_actividad(sesion, datos)

## Criterio de éxito
python -m pytest -v pasa las 19 pruebas y ruff check . responde All checks passed!. Si después de 3 intentos no se cumple, detente y explica el problema.
```

**Resultado:** se implementó el CRUD con validaciones Pydantic y servicio separado. Todas las pruebas pasaron al primer intento, sin correcciones de código. Hubo un problema ajeno al código: varios servidores uvicorn huérfanos de sesiones anteriores atendían el puerto 8000 con una versión antigua, por lo que el primer POST manual devolvió 404. Se detuvieron esos procesos, se inició un servidor limpio y el POST devolvió 201 con los ids esperados; además, un cuerpo inválido devolvió 422. Lección para AGENTS.md: detener y verificar los procesos uvicorn antes de una prueba manual en el puerto 8000.

## Contenido inicial

**Objetivo:** cargar 3 actividades de 5 preguntas del curso propio.

**Herramienta y modelo:** OpenCode con el modelo Big Pickle (`opencode/big-pickle`).

**Prompt:**

```
## Rol
Actúa como desarrollador backend y diseñador de contenidos educativos para niños de 6 a 10 años.

## Objetivo
Crear en app/datos_iniciales.py la función cargar_datos_iniciales(sesion), que cargue el contenido inicial de Lógica y programación, y llamarla en el ciclo de vida de app/main.py después de crear_tablas().

## Contexto
Lee AGENTS.md, specs/encargo.md, specs/respuestas-cliente.md, app/modelos/__init__.py, app/main.py y tests/aceptacion/test_datos_iniciales.py.

## Restricciones
- Carga una clase con un código de 6 caracteres, 3 niños con alias de animales y avatares de la lista de specs/respuestas-cliente.md, y 3 actividades de 5 preguntas cada una, con su descripción.
- Las preguntas siguen los temas y ejemplos de specs/encargo.md: secuencias, patrones y algoritmos sencillos, sin escribir código. Tienen 3 o 4 opciones y una sola respuesta correcta.
- Solo carga los datos si la base de datos no tiene ninguna clase, para que al ejecutarla dos veces no se duplique nada.
- Todos los datos son ficticios y los alias no son nombres de personas.
- No modifiques ningún archivo de la carpeta tests.

## Formato de salida
Antes de escribir código, muestra los títulos de las 3 actividades y sus 15 preguntas con sus opciones y la respuesta correcta, y espera mi aprobación.

## Ejemplo
Actividad 1: «Secuencias para llegar a la meta». Pregunta: «¿Qué instrucción mueve al robot una casilla hacia delante?». Opciones: Avanzar, Girar, Repetir. Respuesta correcta: Avanzar.

## Criterio de éxito
python -m pytest -v pasa todas las pruebas, incluidas las de tests/aceptacion/test_datos_iniciales.py, y ruff check . no reporta errores. Si después de 3 intentos no se cumple, detente y explica el problema.
```

**Resultado:** se propusieron las actividades «Secuencias para llegar a la meta», «Patrones que se repiten» y «Algoritmos sencillos paso a paso», con 15 preguntas de 3 opciones cada una. El desarrollador revisó una por una las respuestas correctas y el lenguaje, y aprobó el contenido sin correcciones. La primera ejecución de Ruff detectó 9 líneas largas en `app/datos_iniciales.py`; se partieron los textos en cadenas adyacentes y la segunda ejecución pasó. Las 21 pruebas pasaron. La verificación local mostró 3 actividades y 15 preguntas tras borrar la base y también después de reiniciar el servidor.
