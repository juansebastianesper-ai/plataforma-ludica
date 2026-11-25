# Plan técnico

## Arquitectura

Capas: rutas, servicios, modelos y plantillas.

## Modelo de datos

```mermaid
erDiagram
    CLASE {
        int id PK
        str nombre
        str codigo
    }
    NINO {
        int id PK
        str alias
        str avatar
        int clase_id FK
    }
    ACTIVIDAD {
        int id PK
        str titulo
        str descripcion
        int orden
    }
    PREGUNTA {
        int id PK
        str enunciado
        str opciones
        str respuesta_correcta
        int actividad_id FK
    }
    INTENTO {
        int id PK
        int nino_id FK
        int actividad_id FK
        int aciertos
        int total
        int duracion_segundos
        datetime fecha
    }
    CLASE ||--o{ NINO : tiene
    ACTIVIDAD ||--o{ PREGUNTA : contiene
    NINO ||--o{ INTENTO : realiza
    ACTIVIDAD ||--o{ INTENTO : recibe
```

## Contrato de API

| Método | Ruta | Descripción | Respuesta |
| --- | --- | --- | --- |
| GET | /salud | Estado del servicio | 200 |

## Decisiones

Cada decisión importante se registra como ADR en `specs/adr/`.
