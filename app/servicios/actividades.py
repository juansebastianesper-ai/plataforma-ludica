"""Regla de negocio de la gestión de actividades del curso."""

from sqlmodel import Session, select

from app.esquemas import ActividadCrear, ActividadRespuesta, PreguntaRespuesta
from app.modelos import Actividad, Pregunta


def _preguntas_de(sesion: Session, actividad_id: int) -> list[Pregunta]:
    return sesion.exec(
        select(Pregunta).where(Pregunta.actividad_id == actividad_id).order_by(Pregunta.id)
    ).all()


def _como_respuesta(actividad: Actividad, preguntas: list[Pregunta]) -> ActividadRespuesta:
    return ActividadRespuesta(
        id=actividad.id,
        titulo=actividad.titulo,
        descripcion=actividad.descripcion,
        orden=actividad.orden,
        preguntas=[
            PreguntaRespuesta(
                id=pregunta.id,
                enunciado=pregunta.enunciado,
                opciones=pregunta.opciones,
                respuesta_correcta=pregunta.respuesta_correcta,
            )
            for pregunta in preguntas
        ],
    )


def listar_actividades(sesion: Session) -> list[ActividadRespuesta]:
    """Devuelve las actividades ordenadas, cada una con sus preguntas."""
    actividades = sesion.exec(select(Actividad).order_by(Actividad.orden, Actividad.id)).all()
    return [
        _como_respuesta(actividad, _preguntas_de(sesion, actividad.id))
        for actividad in actividades
    ]


def crear_actividad(sesion: Session, datos: ActividadCrear) -> ActividadRespuesta:
    """Crea una actividad con sus preguntas y devuelve todos los identificadores."""
    actividad = Actividad(
        titulo=datos.titulo,
        descripcion=datos.descripcion,
        orden=datos.orden,
    )
    sesion.add(actividad)
    sesion.flush()
    for pregunta in datos.preguntas:
        sesion.add(
            Pregunta(
                enunciado=pregunta.enunciado,
                opciones=pregunta.opciones,
                respuesta_correcta=pregunta.respuesta_correcta,
                actividad_id=actividad.id,
            )
        )
    sesion.commit()
    sesion.refresh(actividad)
    return _como_respuesta(actividad, _preguntas_de(sesion, actividad.id))


def obtener_actividad(sesion: Session, actividad_id: int) -> ActividadRespuesta | None:
    """Devuelve una actividad por id, o None si no existe."""
    actividad = sesion.get(Actividad, actividad_id)
    if actividad is None:
        return None
    return _como_respuesta(actividad, _preguntas_de(sesion, actividad_id))


def actualizar_actividad(
    sesion: Session, actividad_id: int, datos: ActividadCrear
) -> ActividadRespuesta | None:
    """Reemplaza los datos y las preguntas de una actividad existente."""
    actividad = sesion.get(Actividad, actividad_id)
    if actividad is None:
        return None

    for pregunta in _preguntas_de(sesion, actividad_id):
        sesion.delete(pregunta)
    sesion.flush()

    actividad.titulo = datos.titulo
    actividad.descripcion = datos.descripcion
    actividad.orden = datos.orden
    sesion.flush()
    for pregunta in datos.preguntas:
        sesion.add(
            Pregunta(
                enunciado=pregunta.enunciado,
                opciones=pregunta.opciones,
                respuesta_correcta=pregunta.respuesta_correcta,
                actividad_id=actividad_id,
            )
        )
    sesion.commit()
    sesion.refresh(actividad)
    return _como_respuesta(actividad, _preguntas_de(sesion, actividad_id))


def eliminar_actividad(sesion: Session, actividad_id: int) -> bool:
    """Elimina la actividad y sus preguntas. Devuelve False si no existe."""
    actividad = sesion.get(Actividad, actividad_id)
    if actividad is None:
        return False

    for pregunta in _preguntas_de(sesion, actividad_id):
        sesion.delete(pregunta)
    sesion.flush()
    sesion.delete(actividad)
    sesion.commit()
    return True
