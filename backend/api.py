from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

app = FastAPI(
    title="FREDRICK AI API",
    description="Fiduciary Risk Evaluation, Due-diligence Reporting & Integrated Compliance Knowledge",
    version="1.0.0"
)

# API Key authentication
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: str = Depends(api_key_header)):
    """Verify API key from request headers"""
    expected_key = os.getenv("FREDRICK_API_KEY")
    if not expected_key:
        raise HTTPException(status_code=500, detail="API key not configured")
    if api_key != expected_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

# Initialize Groq client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# Request/Response Models
class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    model: str

class RiskAnalysisRequest(BaseModel):
    business_data: str
    risk_areas: Optional[list[str]] = None

class ComplianceCheckRequest(BaseModel):
    document: str
    compliance_framework: str

class DueDiligenceRequest(BaseModel):
    company_info: str
    focus_areas: Optional[list[str]] = None

# Helper function to call Groq
def call_groq(system_prompt: str, user_message: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Call Groq API with system and user prompts"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")

# API Endpoints
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "FREDRICK AI",
        "version": "1.0.0"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    api_key: str = Depends(verify_api_key)
):
    """General chat endpoint for business intelligence queries"""
    system_prompt = """You are FREDRICK, the Executive AI CTO for Southern Shade LLC. 
    You provide strategic business intelligence, compliance oversight, and risk analysis. 
    Your responses are professional, analytical, and actionable."""
    
    user_message = request.message
    if request.context:
        user_message = f"Context: {request.context}\n\nQuery: {request.message}"
    
    response = call_groq(system_prompt, user_message)
    
    return ChatResponse(
        response=response,
        model="llama-3.3-70b-versatile"
    )

@app.post("/risk-analysis")
async def risk_analysis(
    request: RiskAnalysisRequest,
    api_key: str = Depends(verify_api_key)
):
    """Perform fiduciary risk evaluation"""
    system_prompt = """You are FREDRICK's risk analysis module. Evaluate business risks 
    across financial, operational, legal, and strategic dimensions. Provide a structured 
    risk assessment with severity levels and mitigation strategies."""
    
    user_message = f"Business Data:\n{request.business_data}\n\n"
    if request.risk_areas:
        user_message += f"Focus on these risk areas: {', '.join(request.risk_areas)}\n\n"
    user_message += "Provide comprehensive risk analysis."
    
    response = call_groq(system_prompt, user_message)
    
    return {"analysis": response, "model": "llama-3.3-70b-versatile"}

@app.post("/compliance-check")
async def compliance_check(
    request: ComplianceCheckRequest,
    api_key: str = Depends(verify_api_key)
):
    """Check document for compliance with specified framework"""
    system_prompt = f"""You are FREDRICK's compliance module. Review documents for 
    compliance with {request.compliance_framework}. Identify gaps, violations, and 
    provide recommendations for achieving full compliance."""
    
    user_message = f"Document to review:\n{request.document}\n\nProvide compliance analysis."
    
    response = call_groq(system_prompt, user_message)
    
    return {"compliance_report": response, "framework": request.compliance_framework}

@app.post("/due-diligence")
async def due_diligence(
    request: DueDiligenceRequest,
    api_key: str = Depends(verify_api_key)
):
    """Perform due diligence analysis on company information"""
    system_prompt = """You are FREDRICK's due diligence module. Conduct thorough 
    due diligence analysis covering financial health, legal standing, operational 
    efficiency, market position, and strategic viability. Flag red flags and provide 
    actionable insights."""
    
    user_message = f"Company Information:\n{request.company_info}\n\n"
    if request.focus_areas:
        user_message += f"Focus areas: {', '.join(request.focus_areas)}\n\n"
    user_message += "Provide comprehensive due diligence report."
    
    response = call_groq(system_prompt, user_message)
    
    return {"due_diligence_report": response, "model": "llama-3.3-70b-versatile"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
