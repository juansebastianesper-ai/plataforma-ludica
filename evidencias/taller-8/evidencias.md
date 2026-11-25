# Evidencias del Taller 8

**Taller:** Especificación, modelo de datos y actividades del curso.
**Repositorio:** https://github.com/juansebastianesper-ai/plataforma-ludica
**Aplicación publicada:** https://plataforma-ludica.onrender.com
**Curso:** Lógica y programación.
**Mecánica:** Niveles.
**Aprendiz:** Juan Sebastian Esper Martinez.

Documento de trabajo: cada captura se añade aquí en el momento indicado por la guía. Las capturas de GitHub y Render las aporta el desarrollador; las locales se capturan desde este entorno.

## 1. Datos iniciales

Pendiente: dirección del repositorio, dirección de Render, curso y mecánica visibles en el PDF final.

## 2. Especificación

Pendiente de captura del desarrollador: mensaje del agente con el borrador de las seis historias (criterios resumidos) y la sección H5 completa de `specs/spec.md`.

## 3. Modelo de datos

Pendiente de captura del desarrollador: plan del agente con rutas completas, terminal con el SQL generado junto a la clase `Pregunta`, y diagrama entidad-relación en GitHub con la rama `taller-8/actividades` visible.

SQL verificado localmente con `echo=True` (argumento retirado después):

```sql
CREATE TABLE pregunta (
	id INTEGER NOT NULL,
	enunciado VARCHAR NOT NULL,
	opciones JSON NOT NULL,
	respuesta_correcta VARCHAR NOT NULL,
	actividad_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(actividad_id) REFERENCES actividad (id)
)
```

Tablas creadas: `actividad`, `clase`, `intento`, `nino`, `pregunta`.

## 4. Pruebas en rojo

Pendiente de captura del desarrollador: ejecutar `python -m pytest -v` **antes de implementar la API** y capturar el resultado completo.

Resultado real obtenido en este momento: `11 failed, 8 passed` (19 pruebas). En `test_actividades.py`: 11 FAILED y 1 PASSED (`test_actividad_inexistente_responde_404`). Las 7 pruebas de `test_inicio.py` siguen en verde. Primer error representativo: `assert 404 == 200` en `test_lista_vacia_cuando_no_hay_actividades`, porque la ruta `/api/actividades` todavía no existe.

## 5. API de actividades

Pendiente de captura del desarrollador: mensaje del agente con el plan que incluya las rutas completas de los archivos, y terminal con `python -m pytest -v` y `ruff check .` en verde.

Rutas del plan aprobado: `app/esquemas.py`, `app/servicios/actividades.py`, `app/rutas/actividades.py` y `app/main.py`.

Resultado real: **19 pruebas pasadas** (12 de `test_actividades.py` y 7 de `test_inicio.py`) y `All checks passed!` de Ruff, al primer intento de corrección.

## 6. Prueba en /docs

Pendiente de captura del desarrollador: sección **Actividades** en `/docs` con cinco operaciones y captura de la respuesta **201** de `POST /api/actividades` para una actividad del curso propio.

Prueba manual local realizada con la actividad «Secuencias con el robot» (Lógica y programación): `POST` → **201**, id de actividad 1, ids de preguntas 1 a 5; `GET` → **200** con la actividad en la lista; un cuerpo con la respuesta correcta fuera de las opciones → **422**. El tag `Actividades` aparece en las cinco operaciones de `openapi.json`.

Incidencia resuelta: había procesos uvicorn huérfanos de sesiones anteriores en el puerto 8000 que servían una versión antigua (el primer POST devolvió 404). Se detuvieron todos los procesos `uvicorn app.main:app` y sus procesos hijos, se arrancó uno limpio y la prueba pasó. El servidor quedó detenido al terminar.

## 7. Contenido inicial

Pendiente: tabla de revisión de las 15 preguntas, pytest en verde y `/api/actividades` en local con 3 actividades.

## 8. Lecciones aprendidas

Pendiente: captura de la sección «Lecciones aprendidas» de `AGENTS.md` en GitHub, rama `taller-8/actividades`.

## 9. Integración y despliegue

Pendiente: PR fusionado con las tres preguntas y verificaciones en verde; `/api/actividades` en Render con la dirección visible.

## 10. Extras (opcional)

No se implementan extras; esta evidencia no corresponde.
