# Taller 8: especificación, modelo de datos y actividades

Curso: Lógica y programación. Mecánica: Niveles.

La sesión se inició con la instrucción global del Taller 8 aportada por el desarrollador. El prompt operativo de cada actividad se reproduce abajo tal como se ejecutó, adaptado desde `prompts-taller-8.md` al curso y la mecánica propios.

## Especificación

**Objetivo:** redactar `specs/spec.md` con las seis historias del MVP.

**Herramienta y modelo:** OpenCode con el modelo Big Pickle (`opencode/big-pickle`). No se usó Copilot.

**Prompt:**

```
## Rol
Actúa como analista de requisitos de software.

## Objetivo
Redactar en specs/spec.md la especificación del MVP de la plataforma, con la estructura que ya tiene ese archivo.

## Contexto
Lee AGENTS.md, specs/encargo.md, specs/ficha-mecanica.md, specs/dudas-encargo.md y specs/respuestas-cliente.md. Cuando una respuesta del cliente contradiga un supuesto de dudas-encargo.md, prevalece la respuesta del cliente.

## Restricciones
- Incluye exactamente estas seis historias de usuario:
  H1. El docente gestiona las actividades del curso.
  H2. La plataforma inicia con contenido del curso.
  H3. El niño entra con el código de la clase, su alias y un avatar.
  H4. El niño resuelve una actividad y sabe de inmediato si acertó.
  H5. La plataforma aplica la regla de la mecánica.
  H6. El docente consulta el progreso de cada niño.
- Cada historia tiene al menos dos criterios Dado/Cuando/Entonces, con los valores exactos de specs/respuestas-cliente.md.
- Todas las actividades son preguntas con 3 o 4 opciones y una respuesta correcta. Los demás tipos de actividad del encargo van en la sección Fuera de alcance.
- Las dudas que no responde el cliente van en Dudas abiertas, con el supuesto de dudas-encargo.md.
- No agregues funcionalidades que no estén en los documentos.
- En la tabla de Dudas abiertas, la columna Respuesta del cliente se renombra como Supuesto, porque esas dudas no tienen respuesta del cliente.
- Modifica solo specs/spec.md.

## Formato de salida
Antes de escribir, muestra la lista de historias con sus criterios resumidos en una línea cada uno y espera mi aprobación.

## Ejemplo
H5. Como niño, quiero desbloquear niveles con mis aciertos, para avanzar por el camino de retos.
- Dado que el niño acierta 4 de 5 preguntas, cuando termina la actividad, entonces se abre el siguiente nivel.
- Dado que el niño acierta 3 de 5, cuando termina la actividad, entonces el siguiente nivel sigue cerrado y puede repetir.

## Criterio de éxito
Las seis historias tienen al menos dos criterios cada una y ningún criterio usa términos vagos como rápido, fácil o adecuado.
```

**Resultado:** se presentó el borrador de H1–H6 con los criterios resumidos; el desarrollador lo aprobó antes de escribir. Se redactaron las seis historias con 4, 3, 3, 3, 5 y 3 criterios respectivamente. H5 usa 80 %, 4 de 5 y 3 de 5, y añade que un nivel abierto no se cierra y que el docente ve el mejor porcentaje. No hubo que corregir criterios tras la aprobación.
