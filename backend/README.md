Backend setup
=============

This backend uses a Mistral HTTP adapter for chat completions.

Environment
-----------
Create a `.env` file in the `backend` folder with:

MISTRAL_API_KEY=your_mistral_api_key_here

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
cd backend
uvicorn main:app --reload --port 8000
```
