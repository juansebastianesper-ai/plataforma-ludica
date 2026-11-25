# STATE.md

Estado del proyecto. Léalo al iniciar cada sesión de trabajo y actualícelo al cerrarla.

## Estado actual

Repositorio publicado en GitHub y aplicación desplegada en https://plataforma-ludica.onrender.com.
En la rama `taller-8/actividades` están terminados el Taller 8: especificación con seis historias,
modelo de datos de cinco entidades, API CRUD de actividades con sus pruebas de aceptación y carga
inicial de 3 actividades y 15 preguntas de Lógica y programación. `python -m pytest -v` pasa 21
pruebas y `ruff check .` responde `All checks passed!`. La rama está publicada en
`origin/taller-8/actividades`; faltan el pull request, la fusión, la etiqueta `taller-8`, la
verificación en Render y el PDF de evidencias.

## Decisiones

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| 2026-11-05 | Desplegar la aplicación con el Blueprint de Render | Usar render.yaml para crear el servicio web gratuito |
| 2026-11-09 | Trabajar GET /api/version en la rama tarea/version | Revisar el cambio mediante un pull request antes de integrarlo |
| 2026-11-25 | Crear `taller-8/actividades` desde `tarea/version` y fusionar `origin/main` | Conservar `/api/version` y los anexos completos del encargo sin regresiones |
| 2026-11-25 | Guardar en `stash@{0}` los cambios previos sin confirmar | Evitar mezclar el trabajo pendiente del Taller 6 con el Taller 8 |
| 2026-11-25 | Copiar solo `respuestas-cliente-niveles.md` como `specs/respuestas-cliente.md` | La guía y LEEME.md indican copiar únicamente la mecánica asignada |
| 2026-11-25 | Autorizar al agente a hacer commit y push en este taller | El desarrollador lo confirmó al resolver el conflicto con AGENTS.md |
| 2026-11-25 | No instalar `gh` ni nuevas dependencias | Las evidencias de GitHub y Render las captura el desarrollador |

## Siguiente paso

Crear el pull request de `taller-8/actividades` a `main`, verificar el CI, fusionarlo, crear la
etiqueta `taller-8`, comprobar `/api/actividades` en Render y ensamblar
`entregas/EsperJuanSebastianTaller8.pdf` con las diez evidencias. Siguiente taller: entrada del
niño, pantalla de juego y regla de la mecánica de Niveles.
