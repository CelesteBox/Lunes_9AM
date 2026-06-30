# Lunes 9 a.m.
### Gobernanza de Inteligencia Artificial para equipos que necesitan decisiones, no filosofía.
---

_Tienes un despliegue programado para el mediodía._
_Tu equipo está integrando un nuevo conjunto de datos, lanzando un chatbot o evaluando un LLM._
_No necesitas leer cinco documentos técnicos antes de la reunión._
_Necesitas saber **qué revisar, por qué es importante y qué documentación debe existir antes de lanzar**._




## ¿Qué problema resuelve?

Los equipos de desarrollo deben tomar decisiones relacionadas con gobernanza de IA durante el entrenamiento, evaluación y despliegue de modelos. Sin embargo, la información suele encontrarse dispersa entre normas, recomendaciones y documentación extensa.

_Lunes 9 a.m._ es un asistente RAG especializado en gobernanza de Inteligencia Artificial. Traduce marcos internacionales de gobernanza en **decisiones técnicas concretas** que puedan ser utilizadas por equipos de desarrollo durante el ciclo de vida de un sistema de IA.


## Objetivo

El proyecto busca reducir la distancia entre la teoría de la Gobernanza de IA y las decisiones cotidianas de ingeniería.

El asistente combina documentación oficial con una checklist práctica para responder preguntas reales que aparecen durante el desarrollo y despliegue de sistemas de IA. Cada respuesta busca ser útil para tomar una decisión concreta, explicando tanto la recomendación como el fundamento documental que la respalda.

No reemplaza auditorías, asesoramiento legal ni procesos formales de compliance.

Su propósito es facilitar **una primera capa de gobernanza responsable durante el desarrollo y despliegue de sistemas de IA**.


## Arquitectura lógica


```

                Usuario
                   │
                   ▼
        Pregunta en lenguaje natural
                   │
                   ▼
          Recuperación de conocimiento
            (PDFs + Checklist propio)
                   │
                   ▼
      Fragmentos relevantes del corpus
                   │
                   ▼
            Modelo de Lenguaje (LLM)
                   │
      ┌────────────┴────────────┐
      │                         │
Orientación práctica      Fundamentación
(Checklists)             (OECD/NIST/etc.)
      │                         │
      └────────────┬────────────┘
                   ▼
            Respuesta final

```


## Ejemplos de preguntas de usuarios

- _¿Qué debería revisar antes de desplegar un chatbot?_
- _¿Qué documentación debería existir para entrenar un modelo?_
- _Voy a entrenar un modelo con CVs. ¿Qué riesgos debería evaluar?_
- _¿Cómo recomienda NIST gestionar riesgos en IA?_
- _¿Qué mecanismos de supervisión humana recomiendan los organismos internacionales?_

A modo de ejemplo: 

Usuario 

> Tengo un deployment el lunes a las 9:00. No tengo tiempo para leer toda la documentación. ¿Qué debería revisar antes de lanzar el sistema?


Lunes 9 a.m. responde:
_- Verifica que la finalidad del sistema esté documentada._
_- Confirma que los datos utilizados sean apropiados y legalmente utilizables._
_- Asegura que exista supervisión humana._
_- Comprueba que el usuario sepa cuándo interactúa con IA._
_- Verifica mecanismos para reportar incidentes y un plan de rollback._
_- Documenta las decisiones relevantes y conserva registros para trazabilidad._
_Fundamentos: OECD AI Principles, NIST AI RMF, UNESCO Recommendation y EU AI Act._


## El conocimiento del agente

El corpus documental del asistente proviene de documentación oficial y material propio. Actualmente, incluye:

* OECD AI Principles
* NIST AI Risk Management Framework
* UNESCO Recommendation on the Ethics of AI
* EU AI Act (resumen oficial)
* AI Deployment Readiness Checklist (propio)



## El comportamiento del agente

* Recupera información mediante RAG.
* Responde basado en la información documental.
* Separa entre recomendaciones prácticas y fundamentos normativos.
* Evita generar recomendaciones sin respaldo documental.
* Transparenta las limitaciones del corpus.



## Tecnologías

- Python
- LangChain
- PyPDF
- Google Colab
- GitHub
- Oracle Cloud Infrastructure (OCI)


## Cómo ejecutar **PENDIENTE!**

```
git clone ...

pip install -r requirements.txt

python chatbot.py
```

---

## Deploy **PENDIENTE!** 

(captura o URL OCI) 

---

## Validación **PENDIENTE!**

```
El agente fue validado realizando consultas relacionadas con:

✓ chatbots

✓ datasets

✓ transparencia

✓ supervisión humana

✓ documentación requerida

En todos los casos las respuestas fueron obtenidas exclusivamente a partir del corpus documental.
```

## Limitaciones **PENDIENTE!**

```
Limitaciones actuales

• El agente sólo responde utilizando la documentación incluida en el corpus.

• No reemplaza asesoramiento jurídico.

• No interpreta legislación nacional.

• No realiza certificaciones de cumplimiento.

• Puede requerir ampliar el corpus para dominios específicos.
```


## Sobre el nombre

Existe una enorme distancia entre los marcos internacionales de Gobernanza de IA y las decisiones que los equipos técnicos deben tomar todos los días.

Mientras los principios suelen presentarse de forma abstracta, las decisiones siempre son concretas.

**Lunes 9 a.m.** busca cerrar esa brecha, ofreciendo orientación práctica respaldada por documentación oficial para que un equipo pueda tomar decisiones responsables antes de un despliegue.



## Origen y futuro del proyecto

Lunes 9 a.m. nació como un proyecto personal para explorar una pregunta sencilla: ¿cómo hacer que la gobernanza de IA resulte útil para quienes tienen que implementar sistemas y tomar decisiones bajo presión? La mejor recomendación ética es aquella que un equipo puede aplicar antes del próximo deployment.

Lunes 9 a.m. es un traductor de marcos internacionales de gobernanza en decisiones técnicas que un equipo puede aplicar antes del próximo despliegue. Comienza como la entrega del primer Challenge del Programa Oracle Next Education 2026 - Alura Latam, y continuará evolucionando como un proyecto abierto. Puede incorporar en próximas versiones: 

```
• nuevos dominios (salud, educación, sector público)
• plantillas automáticas de documentación
• generación de reportes de gobernanza
• integración con nuevas fuentes regulatorias
• soporte multilingüe
```



