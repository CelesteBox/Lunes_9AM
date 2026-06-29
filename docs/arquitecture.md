# Arquitectura

Lunes 9 a.m. implementa un asistente RAG (Retrieval-Augmented Generation) especializado en gobernanza de Inteligencia Artificial.

## Flujo general

Usuario --> 

↓

Pregunta en lenguaje natural

↓

Recuperación de información del corpus documental

↓

Selección de los fragmentos más relevantes

↓

Modelo de Lenguaje (LLM)

↓

Respuesta fundamentada

## Corpus documental

El conocimiento proviene de documentación oficial:

- OECD AI Principles
- NIST AI Risk Management Framework
- UNESCO Recommendation on the Ethics of AI
- EU AI Act (resumen oficial)
- AI Deployment Readiness Checklist (documento propio)

## Principios de diseño

- Las respuestas deben estar respaldadas por documentación.
- El agente diferencia recomendaciones prácticas de fundamentos normativos.
- Si la documentación no permite responder una consulta, el sistema declara esa limitación en lugar de generar información inventada.
