from langchain_groq import ChatGroq
import os

# ---------------- LLM ----------------
def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )

# ---------------- PROMPT ----------------
def build_prompt(context, query):
    return f"""
You are a helpful AI assistant that answers using the provided context.

Rules:
- Use the context as the main source
- If context is partially relevant, infer a simple correct answer
- Only say you don't know if NOTHING is relevant

Context:
{context}

Question:
{query}

Answer:
"""