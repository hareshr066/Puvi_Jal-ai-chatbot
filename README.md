📚 PUVI-JAL AI CHATBOT with CSV/XLSX + ChromaDB + Groq

🚀 PROJECT OVERVIEW

This project is a Retrieval-Augmented Generation (RAG) Chatbot built using Python, ChromaDB, and Groq’s LLaMA models.
It allows you to query CSV/Excel datasets in natural language and get intelligent, context-aware answers.

Instead of relying only on the LLM’s knowledge, this chatbot uses your dataset as the source of truth.


🛠️ TECH STACK

Programming Language: Python 3.10+

Data Handling: pandas, openpyxl

Vector Database: ChromaDB

Embeddings: SentenceTransformers (all-MiniLM-L6-v2)

LLM: Groq API → LLaMA 3 family models

Default: llama-3.1-8b-instant (fast, cost-efficient)

Alternative: llama-3.1-70b-versatile (more powerful reasoning)

Environment: VS Code (local), extendable to Flask/Streamlit for UI


⚡ HOW IT WORKS

Data Ingestion → Load .csv or .xlsx file into pandas.

Embedding Generation → Convert rows into vector embeddings with SentenceTransformers.

Storage → Store embeddings in ChromaDB collection.

User Query → User enters a natural language question.

Retrieval → Query is embedded and matched against top relevant rows.

Augmentation → Retrieved data is passed into LLaMA prompt.

Answer Generation → Groq’s LLM generates context-grounded responses.


📂 PROJECT STRUCTURE

├── ragcsv_chatbot.py      # Main chatbot script  
├── data.xlsx              # Example dataset (replace with your file)  
├── requirements.txt       # Required Python dependencies  
├── README.md              # Project documentation  


🔧 SETUP & INSTALLATION

Clone the repo:

git clone (https://github.com/hareshr066/Puvi_Jal-ai-chatbot.git)


INSTALL DEPENDENCIES:

pip install -r requirements.txt


Set your Groq API key (replace with your actual key):

export GROQ_API_KEY="your_api_key_here"   # Linux/Mac
set GROQ_API_KEY=your_api_key_here        # Windows


RUN THE CHATBOT:

python ragcsv_chatbot.py

💡 EXAMPLE USAGE
Ask a question (or type 'exit'): Give rainfall in Assam  
🤖 Chatbot: The average rainfall in Assam is 2200 mm (based on dataset).  


🎯 FEATURES

✅ Query CSV/XLSX datasets in natural language
✅ Retrieval-Augmented Generation for accuracy
✅ Uses ChromaDB as vector store
✅ Powered by Groq LLaMA 3 models
✅ Extensible → can be deployed with Flask/Streamlit for UI


📌 FUTURE ENHANCEMENTS

Add a Streamlit web UI for a chat interface

Support for multiple datasets

Fine-tuned embeddings for domain-specific queries

Export chatbot responses as PDF/CSV reports


👨‍💻 CONTRIBUTORS

     NEURA CODERS
