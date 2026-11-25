"""Endpoints del CRUD de actividades del curso."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session

from app.db import obtener_sesion
from app.esquemas import ActividadCrear, ActividadRespuesta
from app.servicios import actividades as servicio_actividades

router = APIRouter(tags=["Actividades"])


@router.get("/api/actividades", response_model=list[ActividadRespuesta])
def listar_actividades(
    sesion: Annotated[Session, Depends(obtener_sesion)],
) -> list[ActividadRespuesta]:
    return servicio_actividades.listar_actividades(sesion)


@router.post(
    "/api/actividades",
    response_model=ActividadRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_actividad(
    datos: ActividadCrear,
    sesion: Annotated[Session, Depends(obtener_sesion)],
) -> ActividadRespuesta:
    return servicio_actividades.crear_actividad(sesion, datos)


@router.get("/api/actividades/{actividad_id}", response_model=ActividadRespuesta)
def obtener_actividad(
    actividad_id: int,
    sesion: Annotated[Session, Depends(obtener_sesion)],
) -> ActividadRespuesta:
    actividad = servicio_actividades.obtener_actividad(sesion, actividad_id)
    if actividad is None:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return actividad


@router.put("/api/actividades/{actividad_id}", response_model=ActividadRespuesta)
def actualizar_actividad(
    actividad_id: int,
    datos: ActividadCrear,
    sesion: Annotated[Session, Depends(obtener_sesion)],
) -> ActividadRespuesta:
    actividad = servicio_actividades.actualizar_actividad(sesion, actividad_id, datos)
    if actividad is None:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return actividad


@router.delete("/api/actividades/{actividad_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_actividad(
    actividad_id: int,
    sesion: Annotated[Session, Depends(obtener_sesion)],
) -> Response:
    if not servicio_actividades.eliminar_actividad(sesion, actividad_id):
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
