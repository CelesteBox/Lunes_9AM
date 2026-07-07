# Lunes 9 a.m.
### Gobernanza de Inteligencia Artificial para equipos que necesitan decisiones, no filosofía.
---

_Tienes un despliegue programado para el mediodía._
_Tu equipo está integrando un nuevo conjunto de datos, lanzando un chatbot o evaluando un LLM._
_No necesitas leer cinco documentos técnicos antes de la reunión._
_Necesitas saber **qué revisar, por qué es importante y qué documentación debe existir antes de lanzar**._




## ¿Qué problema resuelve?

Los equipos de desarrollo deben tomar decisiones relacionadas con gobernanza de IA durante el entrenamiento, evaluación y despliegue de modelos. Sin embargo, la información suele encontrarse dispersa entre normas, recomendaciones y documentación extensa.

_Lunes 9 a.m._ es un asistente RAG especializado en gobernanza de Inteligencia Artificial. Recupera información de marcos internacionales y genera respuestas contextualizadas para apoyar decisiones técnicas.


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
            Gemini 2.5 Flash
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
- _¿Cómo recomienda NIST gestionar riesgos en IA?_
- _¿Qué mecanismos de supervisión humana recomiendan los organismos internacionales?_

A modo de ejemplo: 

Usuario 

> Tengo un deployment el lunes a las 9:00. No tengo tiempo para leer toda la documentación. ¿Qué debería revisar antes de lanzar el sistema?


Lunes 9 a.m. responde:
- _Verifica que la finalidad del sistema esté documentada._
- _Confirma que los datos utilizados sean apropiados y legalmente utilizables._
- _Asegura que exista supervisión humana._
- _Comprueba que el usuario sepa cuándo interactúa con IA._
- _Verifica mecanismos para reportar incidentes y un plan de rollback._
- _Documenta las decisiones relevantes y conserva registros para trazabilidad._
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

## Estructura del proyecto

Lunes-9AM/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│ └── raw/
│
└── notebooks/

rag_experiments.ipynb


## Dataset utilizado

El corpus actual incluye documentos oficiales sobre Gobernanza de IA:

• EU AI Overview (May 30, 2024)
• OECD AI Principles
• UNESCO Ethics of AI
• NIST AI Risk Management Framework
• NIST AI RMF Playbook 

Los documentos se cargan localmente mediante PyPDF y se indexan utilizando FAISS y Sentence Transformers.


## Tecnologías

- Python
- LangChain
- PyPDF
- Google Colab
- FAISS
- Sentence Transformers
- GitHub
- Oracle Cloud Infrastructure (OCI)


## Cómo ejecutar

```
git clone ...

cd lunes-9am

pip install -r requirements.txt

python main.py
```

---

## Deploy (en desarrollo)

(captura o URL OCI) 

---

## Validación 

```
El agente fue validado realizando consultas relacionadas con:

✓ transparencia
✓ supervisión humana
✓ documentación requerida

En todos los casos las respuestas fueron obtenidas exclusivamente a partir del corpus documental. Por ejemplo: 

Pregunta: ¿Cuál es el primer principio de la OCDE para una IA responsable?
Respuesta: El primer principio de la OCDE para una IA responsable es "Crecimiento inclusivo, desarrollo sostenible y bienestar (Inclusive growth, sustainable development and well-being)"

Pregunta: ¿Qué recomienda la UNESCO sobre supervisión humana?
Respuesta: La UNESCO recomienda que los "actores de la IA deben respetar la libertad, la dignidad, la privacidad y la justicia social. Esto incluye abordar la desinformación y **garantizar la supervisión humana para evitar el uso indebido.**"

Pregunta: ¿Qué hace a un sistema de IA robusto?
Respuesta: Según el contexto, los sistemas de IA deben ser "seguros durante todo su ciclo de vida". Además, para ser robustos, "deben existir mecanismos para anular, reparar o retirar sistemas que causen daños indebidos o muestren comportamientos no deseados."

Pregunta: ¿Quién es Lionel Messi?
Respuesta: La información no está disponible en los documentos consultados.

```


## Limitaciones actuales

```

• El agente sólo responde utilizando la documentación incluida en el corpus.

• Puede requerir ampliar el corpus a la inclusión de normativa nacional específica y/o relacionada.

• Puede requerir ampliar el corpus para dominios específicos.

• No reemplaza asesoramiento jurídico.

• No realiza certificaciones de cumplimiento.

```


## Sobre el nombre

Existe una enorme distancia entre los marcos internacionales de Gobernanza de IA y las decisiones que los equipos técnicos deben tomar todos los días.

Mientras los principios suelen presentarse de forma abstracta, las decisiones siempre son concretas.

**Lunes 9 a.m.** busca cerrar esa brecha, ofreciendo orientación práctica respaldada por documentación oficial para que un equipo pueda tomar decisiones responsables antes de un despliegue.



## Origen y futuro del proyecto

La gobernanza de IA no comienza cuando aparece un regulador. Comienza cuando un equipo técnico decide qué sistema va a poner en producción el lunes a las 9 de la mañana.

Lunes 9 a.m. comienza como la entrega del primer Challenge del Programa Oracle Next Education - Alura Latam 2026, y continuará evolucionando como un proyecto abierto. Puede incorporar en próximas versiones: 

```
• Nuevos dominios (salud, educación, sector público)
• Plantillas automáticas de documentación
• Generación de reportes de gobernanza
• Integración con nuevas fuentes regulatorias
• Soporte multilingüe
```



