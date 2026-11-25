# AGENTS.md

Contexto del proyecto para los agentes de IA. Léalo antes de cualquier cambio.

## Proyecto

Plataforma web lúdica de cursos para niños. Curso: Lógica y programación. Mecánica: Niveles.
Roles: docente y niño. El niño entra con código de clase y avatar, sin correo.

## Stack

- Python 3.11 o superior, FastAPI, plantillas Jinja2
- SQLModel con SQLite en desarrollo y PostgreSQL al publicar
- pytest con TestClient, Ruff
- GitHub Actions para el CI y Render para el despliegue

## Comandos

- Instalar: `pip install -r requirements-dev.txt`
- Ejecutar: `uvicorn app.main:app --reload`
- Pruebas: `pytest -v`
- Estilo: `ruff check .`

## Estructura

- `app/rutas/`: reciben la petición y llaman a los servicios; sin regla de negocio
- `app/servicios/`: regla de negocio, con pruebas propias
- `app/modelos/`: tablas de SQLModel
- `app/templates/` y `app/static/`: interfaz y PWA
- `tests/`: pruebas; `tests/aceptacion/`: criterios de la especificación

## Convenciones

- Nombres en español, claros y completos.
- Cambios pequeños, una tarea por rama y prueba antes del código.
- Al iniciar cada sesión, leer STATE.md.

## Qué no hacer

- No escribir claves ni contraseñas en el código: se leen de variables de entorno.
- No instalar dependencias sin verificar que existen en pypi.org.
- No modificar ni borrar pruebas para que pasen.
- No usar datos personales reales.
- No hacer commit ni push sin autorización explícita: por defecto los hace el desarrollador
  (en el Taller 8 el desarrollador autorizó ambos).

## Lecciones aprendidas

- Ejecutar pre-commit con .venv activo para que Ruff y pytest estén en PATH.
- OpenCode 1.x usa permission y bash en opencode.json, no el formato V2.
- Revisar `opencode.json` antes de un commit: si `git commit *` o `git push *` están en `deny`,
  pedir autorización en lugar de intentar el comando y recibir Permission denied.
- Crear `crear_tablas()` con `import app.modelos` antes de `SQLModel.metadata.create_all(motor)`;
  si no se registran los modelos, la metadata sale vacía y no se crea ninguna tabla.
- Ejecutar `ruff check .` apenas termina un archivo: Ruff exige el orden `JSON, Column, String`
  en las importaciones de SQLAlchemy y rechaza líneas de más de 100 caracteres; partir los textos
  largos en cadenas adyacentes entre paréntesis.
- Antes de probar la API en `127.0.0.1:8000`, comprobar `Get-NetTCPConnection -LocalPort 8000`:
  los procesos uvicorn huérfanos de otras sesiones pueden servir una versión antigua y devolver
  404. Detener todos los procesos `uvicorn app.main:app` y sus hijos antes de arrancar uno limpio.
- Los archivos PDF no siempre son legibles por el modelo: extraer el texto con `pypdf` a un
  archivo temporal fuera del repositorio antes de planear el trabajo.
- Antes de crear una rama con el árbol sucio, preservar los cambios pendientes en un stash y
  decidir la base de la rama con el desarrollador, para no mezclar talleres distintos.
Cada vez que el agente se equivoque, escriba aquí la regla que evita repetir el error.
