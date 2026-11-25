# Respuestas del cliente: Niveles

Estas respuestas son obligatorias y prevalecen sobre los supuestos de specs/dudas-encargo.md.

## Para todas las mecánicas

- **Actividad:** grupo de preguntas del curso, con un mínimo de 5. Cada pregunta tiene un enunciado, de 3 a 4 opciones y una sola respuesta correcta.
- **Intento:** registro que se crea cuando un niño termina una actividad completa. Guarda los aciertos, el total de preguntas, la duración en segundos y la fecha.
- **Porcentaje de aciertos:** aciertos dividido por el total de preguntas, multiplicado por 100.
- **Contenido inicial:** al iniciar, la aplicación carga una clase de ejemplo, 3 actividades de 5 preguntas del curso y 3 niños ficticios, solo si la base de datos está vacía.
- **Entrada del niño:** el niño escribe el código de la clase, elige su alias en la lista de niños de esa clase y elige uno de los 6 avatares.
- **Métricas del docente:** el tiempo de juego es la suma de la duración de los intentos; las actividades completadas se cuentan sin repetir.

## Avatares

Los 6 avatares se identifican con estos valores, que se guardan en el campo avatar: colibri, tortuga, delfin, jaguar, buho y rana.

## Regla de la mecánica Niveles

- Cada actividad es un nivel, según su campo orden. El nivel 1 está siempre abierto.
- El siguiente nivel se abre cuando el niño obtiene 80 % o más en un intento del nivel anterior: 4 de 5 aciertos lo abren; 3 de 5, no.
- Un nivel abierto no se vuelve a cerrar, aunque un intento posterior tenga un porcentaje menor.
- El docente ve, para cada niño, el mejor porcentaje obtenido en cada nivel.
