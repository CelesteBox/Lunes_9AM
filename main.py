# ==========================================
# IMPORTS
# ==========================================

import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI


# ==========================================
# CONFIGURACIÓN
# ==========================================

os.environ["GOOGLE_API_KEY"] = input("Pegá tu Google API Key: ")


# ==========================================
# CARGA DE DOCUMENTOS
# ==========================================

print("Cargando documentos...")

loader = PyPDFDirectoryLoader("data/raw")
documents = loader.load()

print(f"{len(documents)} documentos cargados.")


# ==========================================
# DIVISIÓN EN CHUNKS
# ==========================================

print("Dividiendo documentos...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"{len(chunks)} chunks creados.")


# ==========================================
# EMBEDDINGS
# ==========================================

print("Creando embeddings locales...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==========================================
# BASE VECTORIAL
# ==========================================

print("Construyendo índice FAISS...")

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)


# ==========================================
# RETRIEVER
# ==========================================

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)


# ==========================================
# MODELO LLM
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


# ==========================================
# ASISTENTE
# ==========================================

print("\n=========================================")
print("Asistente listo.")
print("Escribí 'salir' para terminar.")
print("=========================================\n")


while True:

    pregunta = input("Pregunta: ")

    if pregunta.lower() == "salir":
        break


    # --------------------------------------
    # Recuperar documentos relevantes
    # --------------------------------------

    docs = retriever.invoke(pregunta)


    # --------------------------------------
    # Construir contexto
    # --------------------------------------

    contexto = "\n\n".join(
        doc.page_content
        for doc in docs
    )


    # --------------------------------------
    # Prompt
    # --------------------------------------

    prompt = f"""
Sos el asistente Lunes 9 a.m.

Respondé únicamente utilizando la información del contexto.

Si la respuesta no aparece en el contexto, respondé:

"La información no está disponible en los documentos consultados."

CONTEXTO

{contexto}

PREGUNTA

{pregunta}
"""


    # --------------------------------------
    # Consulta al modelo
    # --------------------------------------

    respuesta = llm.invoke(prompt)


    # --------------------------------------
    # Mostrar respuesta
    # --------------------------------------

    print("\nRespuesta:\n")
    print(respuesta.content)
    print("\n" + "=" * 80 + "\n")
