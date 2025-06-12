# 🧠 AI Legal Assistant Chatbot

Live Demo 👉 [ai-lawyer-mu.vercel.app](https://ai-lawyer-mu.vercel.app/)

AI Legal Assistant is a smart legal chatbot that helps users query uploaded legal documents (PDF, DOCX) and receive context-aware answers powered by Gemini API. The project includes a fully functional frontend (React) and backend (FastAPI).

## 🚀 Features

- 🧾 Upload legal documents (PDF, DOCX)
- 🤖 Ask legal questions from the uploaded documents
- 🧠 Gemini API integration for context-aware legal responses
- 💡 Real-time chatbot UI
- 🌐 Fully deployed frontend on Vercel and backend on Render

## 🏗️ Tech Stack

### Frontend
- React
- Material UI
- Tailwind CSS
- Versal (deployment)

### Backend
- FastAPI
- PyMuPDF (for PDF parsing)
- python-docx (for DOCX parsing)
- Render (deployment)

### APIs
- Gemini API (Google's GenAI)

## 📁 Project Structure

```
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── ... (logic for parsing and API handling)
├── frontend
│   ├── src/
│   │   ├── Components/
│   │   ├── App.js
│   │   └── ...
│   └── public/
├── .render.yaml
└── README.md
```

## 🛡️ Environment Setup

### Backend

Install dependencies:
```bash
pip install -r requirements.txt
```

Run server:
```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

Add `.env` (should be kept private):
```env
GEMINI_API_KEY=your_key_here
```

### Frontend

Install dependencies:
```bash
npm install
```

Start app:
```bash
npm start
```

## ⚙️ Deployment Notes

- **Frontend**: Hosted on [Vercel](https://vercel.com/)
- **Backend**: Hosted on [Render](https://render.com/)
- API keys are managed securely via Render environment variables and not pushed in `.env` files in production.


## 📬 Contribution

Pull requests are welcome. Please open an issue first to discuss what you would like to change.

---
