"""Esquemas de Pydantic que validan el cuerpo de la API de actividades."""

from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints, field_validator, model_validator

Titulo = Annotated[str, StringConstraints(min_length=1, strip_whitespace=True)]


class PreguntaCrear(BaseModel):
    """Pregunta recibida al crear o actualizar una actividad."""

    enunciado: str = Field(min_length=1)
    opciones: list[str] = Field(min_length=3, max_length=4)
    respuesta_correcta: str = Field(min_length=1)

    @field_validator("enunciado", "respuesta_correcta", mode="after")
    @classmethod
    def texto_no_vacio(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("El texto no puede estar vacío")
        return valor.strip()

    @field_validator("opciones", mode="after")
    @classmethod
    def opciones_no_vacias(cls, valores: list[str]) -> list[str]:
        if any(not opcion.strip() for opcion in valores):
            raise ValueError("Las opciones no pueden estar vacías")
        return [opcion.strip() for opcion in valores]

    @model_validator(mode="after")
    def respuesta_entre_opciones(self):
        if self.respuesta_correcta not in self.opciones:
            raise ValueError("La respuesta correcta debe estar entre las opciones")
        return self


class ActividadCrear(BaseModel):
    """Actividad recibida al crear o actualizar."""

    titulo: Titulo
    descripcion: str = ""
    orden: int
    preguntas: list[PreguntaCrear] = Field(min_length=5)


class PreguntaRespuesta(BaseModel):
    """Pregunta devuelta por la API, con su identificador."""

    id: int
    enunciado: str
    opciones: list[str]
    respuesta_correcta: str


class ActividadRespuesta(BaseModel):
    """Actividad devuelta por la API, con sus preguntas."""

    id: int
    titulo: str
    descripcion: str
    orden: int
    preguntas: list[PreguntaRespuesta]
