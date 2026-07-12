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

```text
Lunes-9am/
│
├── data/
│   └── raw/
│       ├── UNESCO_Ethics_of_AI_ES.pdf
│       ├── OECD_AI_Principles_ES.pdf
│       ├── NIST_AI_RMF.pdf
│       └── EU_AI_Act_Resumen.pdf
│
├── docs/
│   ├── alcance_y_limitaciones.md
│   ├── arquitectura.md
│   ├── ejemplos_de_consultas.md
│   └── system_prompt.md
│
├── notebooks/
│   ├── Lunes9AM_RAG_v1_0-Colab.ipynb
│   └── Lunes9AM_RAG_v1_0-Demo.ipynb
|
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
```
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

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/af20529b-c4ec-43f3-a59c-a9fb9497762a" />


---

## Validación 

```
El agente fue validado realizando consultas relacionadas con:

✓ transparencia
✓ supervisión humana
✓ documentación requerida

En todos los casos las respuestas fueron obtenidas exclusivamente a partir del corpus documental. Por ejemplo: 

Pregunta: ¿Qué principios recomienda la OCDE para la gobernanza de la IA?
Respuesta: Los principios que la OCDE recomienda para la gobernanza de la inteligencia artificial, según el documento, son:
    *   Crecimiento inclusivo, desarrollo sostenible y bienestar.
    *   Responsabilidad.
**Riesgos relevantes.**
    *   **Para "Crecimiento inclusivo, desarrollo sostenible y bienestar":** El riesgo principal es que los sistemas de IA no contribuyan a estos objetivos o, peor aún, los socaven, por ejemplo, al exacerbar desigualdades o impactar negativamente el medio ambiente.
    *   **Para "Responsabilidad":** La falta de trazabilidad de los procesos y una gestión de riesgos inadecuada pueden llevar a la imposibilidad de identificar las causas de fallos o impactos negativos, dificultando la rendición de cuentas.
**Acciones recomendadas.**
    *   **Para "Crecimiento inclusivo, desarrollo sostenible y bienestar":**
        *   Integrar métricas de impacto social y ambiental en el diseño y evaluación de los sistemas de IA.
        *   Priorizar el desarrollo de IA que demuestre potencial para reducir desigualdades y promover la sostenibilidad.
    *   **Para "Responsabilidad":**
        *   Establecer y mantener registros detallados de la trazabilidad de los sistemas de IA, incluyendo datos de entrenamiento, algoritmos, decisiones de diseño y versiones.
        *   Implementar un marco sistemático de gestión de riesgos que cubra todo el ciclo de vida del sistema de IA, desde el diseño hasta el despliegue y la operación.
        *   Definir claramente los roles y responsabilidades para el desarrollo, despliegue y operación de los sistemas de IA.
**Documentación que debería existir.**
    *   Evaluaciones de impacto ético y social (incluyendo análisis de desigualdades y sostenibilidad).
    *   Registros de trazabilidad del sistema de IA (ej. logs de entrenamiento, versiones del modelo, decisiones de diseño).
    *   Planes de gestión de riesgos de IA.
    *   Políticas internas de gobernanza de IA que asignen responsabilidades específicas.
**Fundamento normativo.**
    Los principios se basan en los "Principios basados en valores" de los OECD AI Principles:
    *   "1.1 - Crecimiento inclusivo, desarrollo sostenible y bienestar (Inclusive growth, sustainable development and well-being): La IA debe contribuir al crecimiento y la prosperidad global, aumentando las capacidades humanas, reduciendo las desigualdades y protegiendo..."
    *   "1.5 - Responsabilidad (Accountability): Las organizaciones e individuos que desarrollan u operan sistemas de IA deben rendir cuentas de su funcionamiento, garantizando la trazabilidad de los procesos y aplicando una gestión sistemática de riesgos."
**Limitaciones.**
    El extracto proporcionado es un resumen de los Principios de la OCDE y solo detalla dos de los principios basados en valores (1.1 y 1.5). Es posible que la versión completa de los Principios de la OCDE incluya otros principios que no están presentes en este fragmento.

Pregunta: ¿Qué riesgos debería documentar un equipo antes de desplegar un sistema de Inteligencia Artificial?
Respuesta: Un equipo debería documentar los riesgos relacionados con:
- Información errónea, desinformación y discurso de odio, así como los daños causados por el uso indebido de los datos personales.
- Las repercusiones de los sistemas de IA en la cultura, especialmente de las aplicaciones de procesamiento del lenguaje natural (PLN), como la traducción automática y los asistentes de voz, en los matices del lenguaje y la expresión humanos.
- El impacto de los sistemas de IA en los derechos humanos, incluidos los derechos de los niños, y sus repercusiones.
- Reforzar o perpetuar aplicaciones y resultados discriminatorios o sesgados, para garantizar la equidad de dichos sistemas.
- La posibilidad de que los sistemas causen **daños indebidos o muestren comportamientos no deseados.

Pregunta: ¿Qué documentación debería existir antes de desplegar un sistema de Inteligencia Artificial de alto impacto?
Respuesta: Antes de desplegar un sistema de IA de alto impacto, debería existir la siguiente documentación y procesos:
- Evaluaciones del impacto ético de los sistemas de IA: Estas deben realizarse para anticipar las repercusiones, atenuar los riesgos, evitar las consecuencias perjudiciales, facilitar la participación de los ciudadanos y hacer frente a los desafíos sociales (Párrafo 53).
- Mecanismos de supervisión adecuados: La evaluación debe establecer la auditabilidad, la trazabilidad y la explicabilidad, que permitan evaluar los algoritmos, los datos y los procesos de concepción (Párrafo 53).
- Examen externo de los sistemas: La evaluación debe incluir un examen externo de los sistemas (Párrafo 53).
- Evaluaciones del impacto en la privacidad: Estas evaluaciones deben incluir consideraciones sociales y éticas de su utilización y un empleo innovador del enfoque de privacidad desde la etapa de concepción (Párrafo 34).
- Evaluaciones de los aspectos éticos de los sistemas de IA: Las obligaciones en materia de derechos humanos deberían formar parte de estas evaluaciones (Párrafo 52).

Pregunta: ¿Cuál es la fecha exacta en que Argentina aprobará una ley nacional de Inteligencia Artificial?
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



