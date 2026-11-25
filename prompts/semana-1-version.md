## Objetivo

Agregar el endpoint GET /api/version y una prueba automatizada que confirme que devuelve la versión del proyecto.

## Herramienta y modelo

Copilot SDK en VS Code; el modelo no se indicó en esta sesión.

## Prompt

El usuario pidió: "analiza el taller 5 de agentsstate, y ayudame a realizarlo". Después de revisar la guía, se propuso modificar únicamente `app/rutas/api.py` y `tests/test_inicio.py`; el usuario aprobó ese plan.

## Resultado

Se agregó GET /api/version, usando `proyecto.VERSION`, y una prueba para validar el código 200 y el valor devuelto. Las 7 pruebas y Ruff pasan. Los cambios siguen en la rama `tarea/version`; commit, push y pull request quedan a cargo del desarrollador.
