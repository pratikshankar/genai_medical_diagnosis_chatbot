# genai_medical_diagnosis_chatbot
I will build a rag based chatbot application to answer questions related to medical diagnosis and teatment.
# 🏥 Physiotherapy / Medical RAG Chatbot using Gemini 2.0 and Pinecone

---
![alt text](<Screenshot 2025-05-01 at 7.56.03 PM.png>)

## 🚀 Project Description

A professional **Retrieval-Augmented Generation (RAG)** chatbot designed to assist junior physiotherapists in diagnosing conditions and suggesting treatments.

Built with:
- **Google Gemini 2.0 Flash** as the LLM
- **NeuML/pubmedbert-base-embeddings** model for medical embeddings
- **Pinecone** for semantic search storage
- **Flask** for serving the chatbot

The chatbot retrieves relevant knowledge from physiotherapy textbooks and provides concise, context-aware answers.

---

## 💪 Tech Stack

- **Backend:** Flask
- **LLM:** Google Gemini-2.0-Flash-001 (via Generative AI API)
- **Embeddings:** Huggingface - pubmedbert-base-embeddings
- **Vector Database:** Pinecone
- **Frameworks:** LangChain for RAG implementation
- **Document Processing:** PyPDFLoader, RecursiveCharacterTextSplitter

---

## 📂 Data Sources

- "Therapeutic Modalities" by Kenneth Knight
- (Add more book names as you include)

These PDFs serve as the core knowledge base, including:
- Diagnosis protocols
- Treatment modalities
- Clinical case handling

---

## 📊 System Architecture

**Flow:**

1. **Load PDFs:** Extract text using `PyPDFLoader`
2. **Chunk Text:** Split into manageable 500-character segments with slight overlaps
3. **Generate Embeddings:** Using Huggingface's `pubmedbert-base-embeddings`
4. **Store Embeddings:** Push vectors into **Pinecone**
5. **User Query:** Entered via Flask app UI
6. **Retrieve Top Matches:** Pinecone returns most relevant document chunks
7. **Prompt Gemini:** Top chunks + user query fed into Gemini model
8. **Generate Answer:** Gemini formulates a context-aware, concise reply

(Diagram attached below! 📄)

---

## 🔥 Features

- Fast, accurate retrieval of medical knowledge
- Helps in diagnosis and treatment suggestions
- Handles complex physiotherapy queries
- Flask app provides simple UI for continuous conversation
- Scalable and modular RAG pipeline

---

## 📆 How to Run Locally

```bash
# 1. Clone the repository
$ git clone https://github.com/your-username/your-repo-name.git

# 2. Navigate to project folder
$ cd your-repo-name

# 3. Create and activate a virtual environment (optional but recommended)
$ python -m venv venv
$ source venv/bin/activate

# 4. Install dependencies
$ pip install -r requirements.txt

# 5. Set up environment variables
GEMINI_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
PINECONE_INDEX=your_index_name

# 6. Run the Flask app
$ python app.py
```

---

## 🔄 Future Improvements

- Add context memory for multi-turn conversations
- Fine-tune embedding chunk size and overlap
- Integrate feedback loop for continuous improvement
- Add role-based authentication for junior/senior physiotherapists
- Build full frontend using ReactJS or Streamlit

---

## 🤝 Contribution Guidelines

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📅 License

MIT License - see the LICENSE file for details.

---

## 📸 Architecture Diagram

*(Insert the updated diagram here)*

---

## 💚 Acknowledgments

- Google DeepMind Team for Gemini LLM
- Huggingface for PubMedBERT
- Pinecone team for vector database services
- LangChain open-source community

---

### ✨ Star this repo if you like it! 💫

---

