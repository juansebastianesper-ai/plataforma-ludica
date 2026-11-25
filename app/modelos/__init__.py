"""Modelos de tabla del MVP con SQLModel.

Los nombres de clases y campos siguen el contrato del taller 8. Los nombres no
llevan tildes ni ñ, por eso la entidad se llama ``Nino``.
"""

from datetime import datetime

from sqlalchemy import JSON, Column, String
from sqlmodel import Field, SQLModel


class Clase(SQLModel, table=True):
    """Grupo de niños que comparten un código de acceso de seis caracteres."""

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    codigo: str = Field(sa_column=Column(String(6), unique=True, nullable=False))


class Nino(SQLModel, table=True):
    """Niño ficticio que pertenece a una clase."""

    id: int | None = Field(default=None, primary_key=True)
    alias: str
    avatar: str
    clase_id: int = Field(foreign_key="clase.id", index=True)


class Actividad(SQLModel, table=True):
    """Nivel del curso: grupo de preguntas con un orden determinado."""

    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str = Field(default="")
    orden: int


class Pregunta(SQLModel, table=True):
    """Pregunta de una actividad, con opciones guardadas como JSON."""

    id: int | None = Field(default=None, primary_key=True)
    enunciado: str
    opciones: list[str] = Field(sa_column=Column(JSON, nullable=False))
    respuesta_correcta: str
    actividad_id: int = Field(foreign_key="actividad.id", index=True)


class Intento(SQLModel, table=True):
    """Registro de una actividad completa realizada por un niño."""

    id: int | None = Field(default=None, primary_key=True)
    nino_id: int = Field(foreign_key="nino.id", index=True)
    actividad_id: int = Field(foreign_key="actividad.id", index=True)
    aciertos: int
    total: int
    duracion_segundos: int
    fecha: datetime = Field(default_factory=datetime.now)
