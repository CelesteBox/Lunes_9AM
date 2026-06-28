# Lunes 9 a.m.

### Gobernanza de Inteligencia Artificial para equipos que necesitan decisiones, no filosofía.


> Tienes un despliegue programado para el mediodía.
> Tu equipo está integrando un nuevo conjunto de datos, lanzando un chatbot o evaluando un LLM.
> No necesitas leer cinco documentos técnicos antes de la reunión.
> Necesitas saber **qué revisar, por qué es importante y qué documentación debe existir antes de lanzar**.



_Lunes 9 a.m._ es tu asistente RAG especializado en gobernanza de Inteligencia Artificial. Su objetivo es traducir marcos internacionales de gobernanza en decisiones técnicas concretas que puedan ser utilizadas por equipos de desarrollo durante el ciclo de vida de un sistema de IA.


### ¿Qué problema resuelve?

Los equipos de desarrollo deben tomar decisiones relacionadas con gobernanza de IA durante el entrenamiento, evaluación y despliegue de modelos. Sin embargo, la información suele encontrarse dispersa entre normas, recomendaciones y documentación extensa.

Lunes 9 a.m. reúne ese conocimiento y lo traduce en orientación práctica respaldada por documentación oficial.


### Objetivo

El proyecto busca reducir la distancia entre la teoría de la Gobernanza de IA y las decisiones cotidianas de ingeniería.

El asistente combina documentación oficial con una checklist práctica para responder preguntas reales que aparecen durante el desarrollo y despliegue de sistemas de IA. Cada respuesta busca ser útil para tomar una decisión concreta, explicando tanto la recomendación como el fundamento documental que la respalda.

No reemplaza auditorías, asesoramiento legal ni procesos formales de compliance.

Su propósito es facilitar **una primera capa de gobernanza responsable durante el desarrollo y despliegue de sistemas de IA**.


### Arquitectura lógica:


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


# Ejemplos de preguntas de usuarios

- _¿Qué debería revisar antes de desplegar un chatbot?_
- _¿Qué documentación debería existir para entrenar un modelo?_
- _¿Cómo recomienda NIST gestionar riesgos en IA?_
- _¿Qué principios de la OECD se relacionan con transparencia?_
- _¿Qué mecanismos de supervisión humana recomiendan los organismos internacionales?_

A modo de ejemplo: 
Usuario > Voy a desplegar un chatbot interno para RRHH.

# El agente responde: Riesgos principales, documentación recomendada, supervisión humana y referencias del corpus documental (como OECD y NIST). xxxxxxxxxxxxxxxxxxxxxxxxx

Usuario > ¿Qué debería revisar antes de entrenar un modelo con CVs?

Respuesta... xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# El conocimiento del agente

El corpus documental del asistente proviene de documentación oficial y material propio. Actualmente, incluye:

* OECD AI Principles
* NIST AI Risk Management Framework
* UNESCO Recommendation on the Ethics of AI
* EU AI Act (resumen oficial)
* AI Deployment Readiness Checklist (propio)



# El comportamiento del agente

* Recupera información mediante RAG.
* Responde basado en la información documental.
* Separa entre recomendaciones prácticas y fundamentos normativos.
* Evita generar recomendaciones sin respaldo documental.
* Transparenta las limitaciones del corpus.



# Tecnologías

- Python
- LangChain
- PyPDF
- Google Colab
- GitHub
- Oracle Cloud Infrastructure (OCI)


# 6 Cómo ejecutar. Esto HOY no está. Y Alura lo pide. Algo tan simple como

```
git clone ...

pip install -r requirements.txt

python chatbot.py
```

Después lo actualizamos.
---

# 7 Deploy. Acá irá

captura o URL OCI

---

# 8 Validación

Esto casi nadie lo pone. Y justamente por eso te diferencia. Algo sencillo. 

```
El agente fue validado realizando consultas relacionadas con:

✓ chatbots

✓ datasets

✓ transparencia

✓ supervisión humana

✓ documentación requerida

En todos los casos las respuestas fueron obtenidas exclusivamente a partir del corpus documental.
```

Eso es exactamente una validación.

---
# 9 Limitaciones. Esto me parece MUY importante. Porque además coincide con tu filosofía. Algo así.

```
Limitaciones actuales

• El agente sólo responde utilizando la documentación incluida en el corpus.

• No reemplaza asesoramiento jurídico.

• No interpreta legislación nacional.

• No realiza certificaciones de cumplimiento.

• Puede requerir ampliar el corpus para dominios específicos.
```

Eso transmite honestidad.






# Sobre el nombre

Existe una enorme distancia entre los marcos internacionales de Gobernanza de IA y las decisiones que los equipos técnicos deben tomar todos los días.

Mientras los principios suelen presentarse de forma abstracta, las decisiones siempre son concretas.

**Lunes 9 a.m.** busca cerrar esa brecha, ofreciendo orientación práctica respaldada por documentación oficial para que un equipo pueda tomar decisiones responsables antes de un despliegue.



# Sobre el proyecto

Lunes 9 a.m. nació como un proyecto personal para explorar una pregunta sencilla: ¿cómo hacer que la gobernanza de IA resulte útil para quienes tienen que implementar sistemas y tomar decisiones bajo presión? La mejor recomendación ética es aquella que un equipo puede aplicar antes del próximo deployment.

Lunes 9 a.m. es un traductor de marcos internacionales de gobernanza en decisiones técnicas que un equipo puede aplicar antes del próximo despliegue. Comienza como la entrega del primer Challenge del Programa Oracle Next Education 2026 - Alura Latam, y continuará evolucionando como un proyecto abierto. Puede incorporar en próximas versiones: 

```
• nuevos dominios (salud, educación, sector público)
• plantillas automáticas de documentación
• generación de reportes de gobernanza
• integración con nuevas fuentes regulatorias
• soporte multilingüe
```



