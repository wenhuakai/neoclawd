from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.api import routes
from app.agents.orchestrator import AgentOrchestrator

# Initialize orchestrator
orchestrator = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global orchestrator
    orchestrator = AgentOrchestrator()
    await orchestrator.initialize()
    print("✓ Agents initialized")
    yield
    # Shutdown
    await orchestrator.cleanup()
    print("✓ Cleanup complete")

app = FastAPI(
    title="neoclawd",
    description="Ultra-light multi-agent system with free models",
    version="0.1.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(routes.router)

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "agents": orchestrator.get_status() if orchestrator else {}
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)