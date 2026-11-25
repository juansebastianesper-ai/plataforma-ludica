# Especificación

## Contexto

El cliente es una academia de robótica educativa que imparte talleres en colegios. Necesita una plataforma web para que los niños desarrollen pensamiento lógico antes de usar robots. Los temas del curso son secuencias, patrones y algoritmos sencillos. Hay dos roles: docente y niño. El niño entra con el código de la clase, su alias y un avatar, sin correo. Todos los datos son ficticios.

Las respuestas obligatorias del cliente están en `specs/respuestas-cliente.md`. Cuando una respuesta contradice un supuesto de `specs/dudas-encargo.md`, prevalece la respuesta del cliente.

## Historias de usuario

### H1. El docente gestiona las actividades del curso

Como docente, quiero crear, listar, consultar, actualizar y eliminar actividades con sus preguntas, para preparar los retos del curso.

**Criterios de aceptación**

- Dado que envío una actividad con 5 preguntas de 3 a 4 opciones y una sola respuesta correcta, cuando la creo, entonces la API responde 201 con el id de la actividad y el id de cada pregunta.
- Dado que existen actividades con orden 2 y 1, cuando las listo, entonces aparecen ordenadas por orden y cada una incluye sus preguntas.
- Dado que consulto una actividad existente, cuando pido su detalle, entonces respondo 200 con sus preguntas; si no existe, respondo 404.
- Dado que actualizo una actividad con otras 5 preguntas, cuando guardo, entonces respondo 200 y se reemplazan las preguntas anteriores, quedando exactamente 5.
- Dado que elimino una actividad, cuando confirmo, entonces respondo 204 y también desaparecen sus preguntas; si no existe, respondo 404.
- Dado que el título está vacío, hay menos de 5 preguntas, una pregunta tiene 2 o 5 opciones o la respuesta correcta no está entre las opciones, cuando envío los datos, entonces respondo 422 sin crear la actividad.

### H2. La plataforma inicia con contenido del curso

Como docente, quiero que la plataforma arranque con contenido inicial, para tener retos listos desde el primer acceso.

**Criterios de aceptación**

- Dado que la base de datos está vacía, cuando arranca la aplicación, entonces carga 1 clase de ejemplo con código de 6 caracteres, 3 niños ficticios y 3 actividades de 5 preguntas cada una, con una descripción por actividad.
- Dado que los datos iniciales ya fueron cargados, cuando se reinicia la aplicación, entonces siguen existiendo exactamente 1 clase, 3 niños y 3 actividades, sin duplicados.
- Dado que consulto una actividad inicial, cuando reviso sus 5 preguntas, entonces cada una tiene 3 o 4 opciones, una sola respuesta correcta y corresponde a secuencias, patrones o algoritmos sencillos de Lógica y programación.

### H3. El niño entra con el código de la clase, su alias y un avatar

Como niño, quiero entrar con el código de mi clase, mi alias y un avatar, para usar la plataforma sin correo.

**Criterios de aceptación**

- Dado que conozco el código de 6 caracteres de la clase de ejemplo, cuando lo escribo, entonces la plataforma encuentra esa clase.
- Dado que elijo uno de los 3 alias de niños de esa clase, cuando entro, entonces quedo asociado a esa clase sin escribir correo.
- Dado que elijo un avatar, cuando entro, entonces el valor guardado es uno de los seis oficiales: `colibri`, `tortuga`, `delfin`, `jaguar`, `buho` o `rana`.

### H4. El niño resuelve una actividad y sabe de inmediato si acertó

Como niño, quiero ver al momento si acerté, para aprender mientras respondo.

**Criterios de aceptación**

- Dado que una pregunta tiene 3 o 4 opciones y una sola respuesta correcta, cuando elijo una opción, entonces veo de inmediato si acerté.
- Dado que termino una actividad completa de 5 preguntas, cuando se cierra el intento, entonces se registra con los aciertos, el total 5, la duración en segundos y la fecha.
- Dado que no alcanzo el porcentaje necesario, cuando termino la actividad, entonces puedo intentarla de nuevo.

### H5. La plataforma aplica la regla de la mecánica

Como niño, quiero desbloquear niveles con mis aciertos, para avanzar por el camino de retos.

**Criterios de aceptación**

- Dado que comienzo el recorrido, cuando miro los niveles, entonces el nivel 1 (actividad con orden 1) está siempre abierto.
- Dado que obtengo 4 de 5 aciertos (80 %) en un intento del nivel anterior, cuando termino la actividad, entonces se abre el siguiente nivel.
- Dado que obtengo 3 de 5 aciertos (60 %) en el nivel anterior, cuando termino la actividad, entonces el siguiente nivel sigue cerrado y puedo repetir el anterior.
- Dado que el siguiente nivel ya fue abierto, cuando obtengo un porcentaje menor en un intento posterior, entonces el nivel abierto no se vuelve a cerrar.
- Dado que tengo varios intentos en un nivel, cuando el docente consulta mi progreso, entonces ve el mejor porcentaje obtenido en ese nivel.

### H6. El docente consulta el progreso de cada niño

Como docente, quiero ver el avance de cada niño, para acompañar su aprendizaje.

**Criterios de aceptación**

- Dado que los niños han terminado actividades, cuando consulto el progreso, entonces veo en qué nivel está cada niño y su mejor porcentaje en cada nivel.
- Dado que un niño tiene varios intentos, cuando consulto el tiempo de juego, entonces veo la suma de la duración de sus intentos.
- Dado que un niño repitió una actividad, cuando consulto las actividades completadas, entonces la cuento una sola vez, sin repetir.

## Requisitos funcionales

| Código | Requisito | Historia |
| --- | --- | --- |
| RF1 | Listar actividades ordenadas por `orden`, con sus preguntas | H1 |
| RF2 | Crear actividad con preguntas y devolver sus ids | H1 |
| RF3 | Consultar, actualizar y eliminar actividad por id | H1 |
| RF4 | Validar título, mínimo 5 preguntas, 3 o 4 opciones y respuesta correcta incluida | H1 |
| RF5 | Cargar 1 clase, 3 niños y 3 actividades de 5 preguntas solo si la base está vacía | H2 |
| RF6 | Entrada del niño con código de clase, alias y uno de los 6 avatares, sin correo | H3 |
| RF7 | Mostrar acierto inmediato y registrar intento con aciertos, total, duración y fecha | H4 |
| RF8 | Abrir el siguiente nivel con 80 % o más (4 de 5); 3 de 5 no lo abre | H5 |
| RF9 | No cerrar un nivel abierto y conservar el mejor porcentaje | H5 |
| RF10 | Consultar nivel, mejor porcentaje, tiempo de juego y actividades completadas sin repetir | H6 |

## Requisitos no funcionales

| Código | Requisito | Cómo se verifica |
| --- | --- | --- |
| RNF1 | Arquitectura por rutas, servicios y modelos | Revisión del diff y pruebas de aceptación |
| RNF2 | Sin dependencias nuevas; SQLModel ya está en `requirements.txt` | `git diff requirements.txt` sin cambios |
| RNF3 | Secretos y URL de base de datos fuera del código | `DATABASE_URL` leída de entorno con valor por defecto SQLite |
| RNF4 | Pruebas oficiales sin modificación | Comparación por hash con el paquete del taller 8 |
| RNF5 | Estilo y pruebas en verde | `ruff check .` y `python -m pytest -v` |

## Casos límite

- Actividad con menos de 5 preguntas, título vacío, pregunta con 2 o 5 opciones, o respuesta correcta fuera de las opciones: respuesta 422.
- Actividad inexistente en GET, PUT o DELETE: respuesta 404.
- PUT reemplaza las preguntas anteriores; DELETE elimina actividad y preguntas.
- Reinicio de la aplicación con datos ya cargados: no duplica clase, niños ni actividades.
- Umbral de Niveles: 4 de 5 aciertos abre el nivel siguiente; 3 de 5 no; un nivel abierto no se cierra con un intento posterior peor.
- Varios intentos en un nivel: se conserva y muestra el mejor porcentaje.

## Fuera de alcance

- Cuadrícula visual con personaje que avanza y gira, metas y animaciones.
- Instrucciones visuales de avanzar, girar y repetir, y escritura de código tipo Scratch.
- Actividades de completar patrones dibujados o de ordenar pasos arrastrando elementos.
- Modelos de robot concretos y sus instrucciones, autenticación del docente y administración de códigos de clase, pantallas de juego, rachas, estrellas, misiones, insignias y memoria de parejas.

El MVP solo incluye actividades formadas por preguntas con 3 o 4 opciones y una sola respuesta correcta.

## Criterios de terminado

- [ ] `specs/spec.md` tiene las seis historias con al menos dos criterios Dado/Cuando/Entonces cada una.
- [ ] H5 usa los valores exactos de Niveles: 80 %, 4 de 5 y 3 de 5.
- [ ] `specs/respuestas-cliente.md` contiene solo las respuestas de Niveles, los avatares y las reglas comunes.
- [ ] Las pruebas oficiales de `tests/aceptacion` pasan sin haber sido modificadas.
- [ ] La API CRUD respeta 201, 200, 204, 404 y 422.
- [ ] La carga inicial crea 3 actividades y 15 preguntas del curso propio, sin duplicados.

## Dudas abiertas

| Duda | Supuesto |
| --- | --- |
| ¿Qué dimensiones tiene la cuadrícula, cuál es la posición y orientación inicial del personaje y qué elementos puede haber en ella? | Pendiente de decisión del estudiante |
| ¿Qué acciones concretas realizan «girar» y «repetir», y cómo se indica el sentido o la cantidad de repeticiones? | Pendiente de decisión del estudiante |
| ¿Qué criterio determina que una solución de secuencia, patrón u ordenamiento sea correcta cuando pueda haber más de una respuesta posible? | Pendiente de decisión del estudiante |
| ¿Secuencias, patrones y algoritmos son las únicas categorías de actividades previstas o los tres ejemplos son ilustrativos? | Pendiente de decisión del estudiante |
| ¿Qué información y reglas puede configurar el docente al crear un reto nuevo? | Pendiente de decisión del estudiante |
| ¿Cuántos niveles tiene el recorrido y cómo se distribuyen las actividades entre niveles? | Pendiente de decisión del estudiante |
| ¿Cómo se calcula y redondea el 80 % cuando un nivel tiene una cantidad de preguntas distinta de diez? | Pendiente de decisión del estudiante |
| ¿Existe un límite de reintentos? | Pendiente de decisión del estudiante |
| Si un niño no alcanza el porcentaje, ¿puede acceder a otro nivel disponible o debe repetir hasta desbloquear el siguiente? | Pendiente de decisión del estudiante |
| ¿Qué acciones incrementan el contador de intentos que ve el docente? | Pendiente de decisión del estudiante |
| ¿Cómo se mide que los niños usan «menos instrucciones» y entre qué niveles o periodos se compara esa cantidad? | Pendiente de decisión del estudiante |
| ¿Con qué modelo de robot y conjunto de instrucciones deben corresponder los retos de la plataforma? | Pendiente de decisión del estudiante |
| ¿Qué requisitos concretos de lectura, interacción o accesibilidad debe cumplir la interfaz para el rango de 6 a 12 años? | Pendiente de decisión del estudiante |
| ¿Cómo autentica el docente y crea o administra los códigos de clase? | Pendiente de decisión del estudiante |
