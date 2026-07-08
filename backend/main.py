import os
import json
import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Portfolio Brain")

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key) if groq_api_key else None

# Initialize Gemini client
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_client = genai.Client(api_key=gemini_api_key) if gemini_api_key else None
gemini_model_name = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")

class ChatMessageModel(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    query: str
    history: list[ChatMessageModel] = []

class ChatResponse(BaseModel):
    intent: str
    ai_text: str
    provider: str

# Base prompt layout
BASE_SYSTEM_PROMPT = """You are Shubham Patil's AI Portfolio Assistant. Your job is to answer questions about Shubham based on the provided Knowledge Base and determine what UI component the frontend should render.

Knowledge Base:
======================
{knowledge_base}
======================

Your response MUST be valid JSON matching this schema exactly:
{
  "intent": "me" | "projects" | "resume" | "skills" | "contact" | "general",
  "ai_text": "Your natural, conversational response speaking as Shubham's assistant."
}

Rules:
- If the user asks "Tell me about yourself", "Who are you?", or asks for a general introduction, set intent to "me".
  CRITICAL FOR "me" INTENT: The frontend will automatically display a visual profile card with Shubham's summary and key skills. DO NOT repeat the information shown on the card. Instead, briefly welcome the user and ask what they would like to know more about.
  Example `ai_text`:
  "You've got a quick overview of my background above! Feel free to ask about my Full-Stack development experience, MERN projects, backend architecture, AI integrations, or career journey."

- If the user explicitly asks to view, show, browse, or list your projects or portfolio, set intent to "projects".

- If the user asks a detailed or follow-up question about a specific project (for example: "How does MediFlow work?", "Explain the AI Recipe Blog architecture.", "How did you integrate Gemini API?"), set intent to "general" so only the text response is rendered without showing the projects section again.

- If the user asks about your experience, internship, career, professional journey, resume, or previous work, set intent to "resume".
  CRITICAL FOR "resume" INTENT: The frontend will automatically display the professional experience timeline. DO NOT repeat every company, date, or responsibility. Instead, provide a short overview and invite the user to ask about any specific role.
  Example `ai_text`:
  "I've displayed my professional experience above, including my Full-Stack Developer internship and the technologies I've worked with. Let me know if you'd like to learn more about a specific role or project."

- If the user asks about your technical skills, programming languages, frameworks, databases, tools, or technologies, set intent to "skills".

- If the user wants to contact you, hire you, collaborate, or asks for your email or LinkedIn, set intent to "contact".
  CRITICAL FOR "contact" INTENT:
  You MUST set the `ai_text` to EXACTLY:
  "You can reach me through the contact information above! Whether it's a job opportunity, collaboration, or just a tech discussion, I'd be happy to connect. What's on your mind?"

- For all other questions—including technical discussions, software engineering concepts, project implementation details, backend architecture, React, Node.js, Express.js, MongoDB, authentication, REST APIs, AI integrations, OCR, Gemini API, career goals, or learning journey—set intent to "general".

- Keep `ai_text` friendly, professional, and conversational.

Response Length Rules:
- For greetings or whenever dynamic cards are displayed (intents: "me", "projects", "resume", "skills", "contact"), keep responses concise (1–3 sentences).

- CRITICAL EXCEPTION FOR TECHNICAL QUESTIONS:
  If the user asks about project architecture, implementation details, backend design, authentication, database structure, AI integration, OCR, React, Node.js, Express.js, MongoDB, REST APIs, JWT, deployment, or software engineering decisions, provide a detailed and well-structured response (1–3 paragraphs with bullet points where appropriate). Explain your reasoning like an experienced Full-Stack Developer speaking to a recruiter or engineering manager.

- Base all answers only on the provided Knowledge Base. If the information isn't available, politely say you don't have that information instead of making assumptions.

- Do not invent projects, companies, technologies, achievements, certifications, or work experience.

- Do not mention personal social media accounts unless explicitly requested.

- Always use proper English grammar and punctuation.

- CRITICAL Punctuation Rule:
Always write English contractions correctly using apostrophes:
"I'm", "I've", "don't", "it's", "you're", "we've", "they're".
Never write:
"Im", "Ive", "dont", "its" (unless possessive), "youre", "weve", or "theyre".
"""

def get_system_prompt() -> str:
    try:
        kb_path = os.path.join(os.path.dirname(__file__), "knowledge_base.md")
        with open(kb_path, "r", encoding="utf-8") as f:
            kb_content = f.read()
        return BASE_SYSTEM_PROMPT.replace("{knowledge_base}", kb_content)
    except Exception as e:
        print(f"Error loading knowledge base: {e}")
        return BASE_SYSTEM_PROMPT.replace("{knowledge_base}", "Knowledge base file not found.")

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not client and not gemini_client:
        raise HTTPException(status_code=500, detail="Neither Groq nor Gemini API clients are configured on the server.")
        
    system_prompt = get_system_prompt()
    response_content = None
    provider = "groq"
    
    # Try Groq first
    if client:
        try:
            messages = [{"role": "system", "content": system_prompt}]
            
            # Append conversation history
            for msg in request.history:
                role = "user" if msg.role == "user" else "assistant"
                messages.append({"role": role, "content": msg.content})
                
            # Append latest user query
            messages.append({"role": "user", "content": request.query})
            
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile", # Active Groq model for JSON
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=400
            )
            response_content = completion.choices[0].message.content
        except Exception as e:
            print(f"[Warning] Groq completion failed: {e}. Attempting fallback to Gemini...")
            response_content = None
            
    # Fallback to Gemini if Groq failed or is not configured
    if response_content is None:
        if not gemini_client:
            raise HTTPException(status_code=500, detail="Groq API failed and Gemini API client is not configured.")
            
        try:
            provider = "gemini"
            
            # Format prompt & history for Gemini
            gemini_prompt = f"{system_prompt}\n\n"
            for msg in request.history:
                role_label = "user" if msg.role == "user" else "assistant"
                gemini_prompt += f"{role_label}: {msg.content}\n"
            gemini_prompt += f"user: {request.query}\n"
            gemini_prompt += "Response (in JSON schema):"
            
            # Call Gemini using the new SDK
            completion = gemini_client.models.generate_content(
                model=gemini_model_name,
                contents=gemini_prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            response_content = completion.text
        except Exception as gemini_err:
            print(f"[Error] Gemini fallback also failed: {gemini_err}")
            raise HTTPException(
                status_code=500, 
                detail=f"Both primary (Groq) and fallback (Gemini) API calls failed. Gemini Error: {gemini_err}"
            )
            
    try:
        data = json.loads(response_content)
        ai_text = data.get("ai_text", "I'm not quite sure how to answer that.")
        
        # Post-process to restore missing apostrophes in common contractions
        ai_text = re.sub(r"\b[Ii]ve\b", "I've", ai_text)
        ai_text = re.sub(r"\b[Ii]m\b", "I'm", ai_text)
        ai_text = re.sub(r"\b[Dd]ont\b", "don't", ai_text)
        ai_text = re.sub(r"\b[Cc]ant\b", "can't", ai_text)
        ai_text = re.sub(r"\b[Yy]oure\b", "you're", ai_text)
        ai_text = re.sub(r"\b[Ww]eve\b", "we've", ai_text)
        ai_text = re.sub(r"\b[Tt]heyre\b", "they're", ai_text)
        
        return ChatResponse(
            intent=data.get("intent", "general"),
            ai_text=ai_text,
            provider=provider
        )
    except Exception as parse_err:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to parse model JSON. Raw content: {response_content}. Error: {parse_err}"
        )

@app.get("/")
async def root():
    return {"message": "Hello from the AI Portfolio Backend!"}