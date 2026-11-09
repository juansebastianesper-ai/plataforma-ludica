# STATE.md

Estado del proyecto. Léalo al iniciar cada sesión de trabajo y actualícelo al cerrarla.

## Estado actual

Repositorio publicado en GitHub con el CI en verde. La página de inicio, /salud y /docs funcionan
en https://plataforma-ludica.onrender.com. GET /api/version está implementado en la rama
tarea/version y devuelve la versión del proyecto. Las 7 pruebas, Ruff y los hooks locales pasan.

## Decisiones

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| 2026-11-05 | Desplegar la aplicación con el Blueprint de Render | Usar render.yaml para crear el servicio web gratuito |
| 2026-11-09 | Trabajar GET /api/version en la rama tarea/version | Revisar el cambio mediante un pull request antes de integrarlo |

## Siguiente paso

Revisar el diff, registrar y subir la rama tarea/version, crear el pull request y actualizar este estado después de integrarlo.
