"""
Real Estate Lead Bot - FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="Real Estate Lead Bot API - Lead capture, qualification, and management",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "service": settings.APP_NAME, "environment": settings.APP_ENV}


@app.get("/")
async def root():
    return {
        "message": "Real Estate Lead Bot API",
        "docs": "/docs",
        "health": "/health",
        "version": "0.1.0",
    }


# TODO: Include routers
# from app.api import chat, leads, followups
# app.include_router(chat.router, prefix=settings.API_V1_PREFIX)
# app.include_router(leads.router, prefix=settings.API_V1_PREFIX)
# app.include_router(followups.router, prefix=settings.API_V1_PREFIX)
