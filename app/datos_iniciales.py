"""Contenido ficticio del curso cargado al iniciar la aplicación."""

from sqlmodel import Session, select

from app.modelos import Actividad, Clase, Nino, Pregunta

CODIGO_CLASE = "ROBOT7"

NINOS = [
    {"alias": "Lobo", "avatar": "jaguar"},
    {"alias": "Osa", "avatar": "buho"},
    {"alias": "Zorro", "avatar": "rana"},
]

ACTIVIDADES = [
    {
        "titulo": "Secuencias para llegar a la meta",
        "descripcion": (
            "Observa el orden de las instrucciones y elige la que continúa cada secuencia "
            "para que el robot llegue a la meta."
        ),
        "orden": 1,
        "preguntas": [
            {
                "enunciado": "¿Qué instrucción mueve al robot una casilla hacia delante?",
                "opciones": ["Avanzar", "Girar", "Repetir"],
                "respuesta_correcta": "Avanzar",
            },
            {
                "enunciado": (
                    "El robot mira hacia arriba y debe mirar hacia la derecha. "
                    "¿Qué instrucción usa?"
                ),
                "opciones": ["Girar", "Avanzar", "Esperar"],
                "respuesta_correcta": "Girar",
            },
            {
                "enunciado": (
                    "La secuencia es avanzar, avanzar, girar, avanzar, avanzar. "
                    "¿Qué sigue?"
                ),
                "opciones": ["Avanzar", "Girar", "Repetir"],
                "respuesta_correcta": "Girar",
            },
            {
                "enunciado": "¿Qué palabra usamos para hacer una instrucción tres veces?",
                "opciones": ["Repetir", "Avanzar", "Dibujar"],
                "respuesta_correcta": "Repetir",
            },
            {
                "enunciado": (
                    "En la secuencia círculo, cuadrado, círculo, cuadrado, "
                    "¿qué figura sigue?"
                ),
                "opciones": ["Círculo", "Cuadrado", "Estrella"],
                "respuesta_correcta": "Círculo",
            },
        ],
    },
    {
        "titulo": "Patrones que se repiten",
        "descripcion": (
            "Completa patrones de colores, formas y acciones igual que un robot "
            "que aprende a observar."
        ),
        "orden": 2,
        "preguntas": [
            {
                "enunciado": "El patrón es rojo, azul, rojo, azul, rojo. ¿Qué color sigue?",
                "opciones": ["Azul", "Rojo", "Verde"],
                "respuesta_correcta": "Azul",
            },
            {
                "enunciado": (
                    "El patrón es triángulo, cuadrado, triángulo, cuadrado. "
                    "¿Qué forma sigue?"
                ),
                "opciones": ["Triángulo", "Cuadrado", "Círculo"],
                "respuesta_correcta": "Triángulo",
            },
            {
                "enunciado": "El robot aplaude, pisa, aplaude, pisa. ¿Qué acción sigue?",
                "opciones": ["Aplaudir", "Pisar", "Saltar"],
                "respuesta_correcta": "Aplaudir",
            },
            {
                "enunciado": "En el patrón grande, pequeño, grande, pequeño, ¿qué tamaño sigue?",
                "opciones": ["Grande", "Pequeño", "Mediano"],
                "respuesta_correcta": "Grande",
            },
            {
                "enunciado": "¿Por qué una secuencia se llama un patrón?",
                "opciones": [
                    "Porque sus partes se repiten en el mismo orden",
                    "Porque cambia sin regla",
                    "Porque todas sus partes son distintas",
                ],
                "respuesta_correcta": "Porque sus partes se repiten en el mismo orden",
            },
        ],
    },
    {
        "titulo": "Algoritmos sencillos paso a paso",
        "descripcion": (
            "Ordena pasos sencillos para que el robot llegue desde su punto "
            "de partida hasta la meta."
        ),
        "orden": 3,
        "preguntas": [
            {
                "enunciado": "¿Qué es un algoritmo?",
                "opciones": [
                    "Una lista de pasos ordenados",
                    "Un dibujo sin pasos",
                    "Un robot que piensa solo",
                ],
                "respuesta_correcta": "Una lista de pasos ordenados",
            },
            {
                "enunciado": "Si la meta está a la derecha del robot, ¿qué hace primero?",
                "opciones": ["Girar a la derecha", "Avanzar hacia la pared", "Repetir tres veces"],
                "respuesta_correcta": "Girar a la derecha",
            },
            {
                "enunciado": (
                    "El robot debe tomar un bloque que tiene delante. "
                    "¿Qué instrucción va primero?"
                ),
                "opciones": ["Avanzar hasta el bloque", "Girar dos veces", "Repetir sin moverse"],
                "respuesta_correcta": "Avanzar hasta el bloque",
            },
            {
                "enunciado": (
                    "Los pasos son avanzar, girar, avanzar. "
                    "¿Cómo podemos usar menos instrucciones?"
                ),
                "opciones": [
                    "Quitar un paso que no necesita",
                    "Agregar más giros",
                    "Cambiar el color del robot",
                ],
                "respuesta_correcta": "Quitar un paso que no necesita",
            },
            {
                "enunciado": (
                    "Después de seguir todos los pasos, el robot llegó a la meta. "
                    "¿Qué debe pasar al terminar?"
                ),
                "opciones": [
                    "El algoritmo termina en la meta",
                    "El robot sigue avanzando",
                    "El algoritmo empieza de nuevo",
                ],
                "respuesta_correcta": "El algoritmo termina en la meta",
            },
        ],
    },
]


def cargar_datos_iniciales(sesion: Session) -> None:
    """Carga la clase, los niños y las actividades si la base está vacía."""
    if sesion.exec(select(Clase)).first() is not None:
        return

    clase = Clase(nombre="Robot Club", codigo=CODIGO_CLASE)
    sesion.add(clase)
    sesion.flush()

    for nino in NINOS:
        sesion.add(Nino(**nino, clase_id=clase.id))

    for actividad in ACTIVIDADES:
        fila = Actividad(
            titulo=actividad["titulo"],
            descripcion=actividad["descripcion"],
            orden=actividad["orden"],
        )
        sesion.add(fila)
        sesion.flush()
        for pregunta in actividad["preguntas"]:
            sesion.add(Pregunta(**pregunta, actividad_id=fila.id))

    sesion.commit()
