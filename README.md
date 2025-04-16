
# 📚 Bookwise AI – Intelligent Book Management with LLaMA3

Bookwise AI is a FastAPI-based application designed for **intelligent book summarization, review management, and user interaction**. It utilizes a **locally hosted LLaMA3 model** via Ollama to generate insightful summaries and adopts a secure, scalable, and production-ready layered architecture.

---

## 🚀 Key Features

- 🔒 **JWT Authentication** for secure user management
- 🧠 **AI-Generated Summaries** powered by LLaMA3 (local Ollama server)
- 📝 **User Reviews and Ratings** with average rating computation
- 📘 **Book CRUD APIs** with auto-summarization
- ⚙️ **Asynchronous SQLAlchemy ORM** with PostgreSQL
- ✅ **Pytest-Based Unit Tests** for all major API endpoints
- 🧱 **SOLID Layered Structure** with clear separation of concerns

---

## 🏗️ Project Architecture

```
app/
├── api/               # API routes
├── ai/                # LLaMA3 interaction module
├── core/              # Security config & constants
├── database.py        # Async SQLAlchemy setup
├── models/            # SQLAlchemy models
├── repositories/      # DB operations
├── schemas/           # Pydantic schemas
├── services/          # Business logic layer
├── utils/             # LLaMA3 async HTTP client
└── main.py            # FastAPI app initialization
tests/                 # Full API test coverage using Pytest
```

---

## 🧪 Code Quality Highlights

The project **indirectly reflects adherence to best practices**:

- ✅ **Layered architecture** separates API, services, repositories, and utils
- ✅ **Pydantic models with validation**
- ✅ **Custom exception handling** in routes
- ✅ **Centralized DB session management**
- ✅ **Token-based security using OAuth2 + Bearer**
- ✅ **Clean async operations** using `AsyncSession` and `httpx`
- ✅ **Test automation** with structured unit tests in `tests/` folder
- ✅ **Swagger UI with Bearer token support**

---

## 🐳 Deployment Guide (Production Ready)

### 🧰 Prerequisites

- Docker & Docker Compose
- PostgreSQL database (locally or managed e.g., AWS RDS)
- Ollama server with LLaMA3 model loaded
- `.env` file or secrets manager for storing sensitive variables


---

### 🔐 Required Environment Variables

Create a `.env` file ( not using hardcoded values):

```
DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/bookwise
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OLLAMA_URL=http://host.docker.internal:11434/api/generate
```

You can then load them via `os.getenv()` or `python-dotenv`.

---

### ⚙️ Manual Deployment (non-Docker)

1. Set up PostgreSQL and Ollama server
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## ✅ Test Execution

```bash
pytest tests/
```

Pytest will execute all functional test cases for:

- Authentication (`test_auth.py`)
- Book operations (`test_books.py`)
- Review flow (`test_reviews.py`)

---
