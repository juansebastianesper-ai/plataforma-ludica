"""Conexión con la base de datos y sesiones por petición."""

import os
from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

URL_BASE_DATOS = os.getenv("DATABASE_URL", "sqlite:///./plataforma.db")

ARGUMENTOS_SQLITE = (
    {"check_same_thread": False} if URL_BASE_DATOS.startswith("sqlite") else {}
)

motor = create_engine(URL_BASE_DATOS, connect_args=ARGUMENTOS_SQLITE)


def crear_tablas() -> None:
    """Crea las tablas del modelo si todavía no existen."""
    import app.modelos  # noqa: F401  Se necesita para registrar las tablas.
    SQLModel.metadata.create_all(motor)


def obtener_sesion() -> Generator[Session, None, None]:
    """Entrega una sesión por petición y la cierra al terminar."""
    with Session(motor) as sesion:
        yield sesion
