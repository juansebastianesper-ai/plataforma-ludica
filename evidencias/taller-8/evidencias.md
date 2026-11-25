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

Pendiente: captura de pytest con 11 pruebas de `test_actividades.py` en rojo y 1 en verde, anterior a la API.

## 5. API de actividades

Pendiente: plan del agente con rutas completas y captura de pytest y Ruff en verde.

## 6. Prueba en /docs

Pendiente: captura de Swagger con POST `/api/actividades` y respuesta 201 de una actividad de Lógica y programación.

## 7. Contenido inicial

Pendiente: tabla de revisión de las 15 preguntas, pytest en verde y `/api/actividades` en local con 3 actividades.

## 8. Lecciones aprendidas

Pendiente: captura de la sección «Lecciones aprendidas» de `AGENTS.md` en GitHub, rama `taller-8/actividades`.

## 9. Integración y despliegue

Pendiente: PR fusionado con las tres preguntas y verificaciones en verde; `/api/actividades` en Render con la dirección visible.

## 10. Extras (opcional)

No se implementan extras; esta evidencia no corresponde.
