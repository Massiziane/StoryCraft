from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings


# Create FastAPI app
app = FastAPI(
    title="StoryCraft API",
    description="API to generate stories",
    version="0.1.0",
    docs_url="/docs", 
    redoc_url="/redoc" 
    )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )   

if __name__ == "__main__":
    import uvicorn # webserver to serve FastAPI application
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
