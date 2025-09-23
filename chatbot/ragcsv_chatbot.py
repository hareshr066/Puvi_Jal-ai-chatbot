import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq   # Groq client

# ========= CONFIG =========
EXCEL_FILE = "chatbot.xlsx"   # <-- put your Excel file name here
GROQ_API_KEY = "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"   # <-- paste your Groq API key
# ==========================

# ===== STEP 1: Load Excel =====
df = pd.read_excel(EXCEL_FILE)
df['text'] = df.astype(str).agg(' '.join, axis=1)   # merge all columns into text
documents = df['text'].tolist()

# ===== STEP 2: Initialize ChromaDB =====
client = chromadb.PersistentClient(path="./chroma_db")

# Use sentence-transformers for embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_func(texts):
    return embedding_model.encode(texts).tolist()

collection = client.get_or_create_collection(
    name="excel_collection",
    embedding_function=None   # we’ll handle embeddings manually
)

# ===== STEP 3: Insert Data =====
if collection.count() == 0:
    embeddings = embed_func(documents)
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(documents))]
    )
    print("✅ Data inserted into ChromaDB")
else:
    print("ℹ️ Data already exists in ChromaDB")

# ===== STEP 4: Setup Groq Client =====
groq_client = Groq(api_key=GROQ_API_KEY)

# ===== STEP 5: Define RAG Chatbot =====
def rag_chatbot(query):
    # Embed query
    query_embedding = embed_func([query])

    # Retrieve from ChromaDB
    results = collection.query(query_embeddings=query_embedding, n_results=3)
    context = " ".join([doc for docs in results["documents"] for doc in docs])

    # Ask Groq with context
    prompt = f"""
    You are a helpful assistant.
    Use the following context to answer the question:
    Context: {context}
    Question: {query}
    """

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",   # you can switch to "llama3-70b-8192" if needed
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ===== STEP 6: Run a Sample Query =====
if __name__ == "__main__":
    while True:
        user_query = input("\nAsk a question (or type 'exit'): ")
        if user_query.lower() == "exit":
            break
        answer = rag_chatbot(user_query)
        print("🤖 Bot:", answer)
