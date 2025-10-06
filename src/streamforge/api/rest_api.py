"""
RESTful API Server for StreamForge-Pro
Created by RAJSARASWATI JATAV
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="StreamForge-Pro API",
    description="RESTful API for video downloading",
    version="2.2.0",
    contact={"name": "RAJSARASWATI JATAV", "email": "rajsaraswatijatav@outlook.com"}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DownloadRequest(BaseModel):
    url: str
    quality: Optional[str] = "best"
    audio_only: Optional[bool] = False

class DownloadResponse(BaseModel):
    status: str
    message: str
    file_path: Optional[str] = None

@app.get("/")
async def root():
    return {
        "name": "StreamForge-Pro API",
        "version": "2.2.0",
        "author": "RAJSARASWATI JATAV",
        "endpoints": ["/download", "/status", "/platforms", "/health"]
    }

@app.post("/download", response_model=DownloadResponse)
async def download_video(request: DownloadRequest):
    """Download video from URL"""
    try:
        from streamforge.core.simple_downloader import SimpleDownloader
        downloader = SimpleDownloader()
        result = downloader.download(request.url, quality=request.quality, audio_only=request.audio_only)
        return DownloadResponse(status="success", message="Download completed", file_path=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/platforms")
async def get_platforms():
    """Get list of supported platforms"""
    return {
        "platforms": ["YouTube", "Instagram", "TikTok", "Twitter", "Facebook", "Twitch", "Vimeo"],
        "total": "1000+"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "StreamForge-Pro API"}

def start_api_server(host: str = "0.0.0.0", port: int = 8000):
    """Start the API server"""
    print(f"🚀 StreamForge-Pro API Server")
    print(f"📍 Created by: RAJSARASWATI JATAV")
    print(f"🌐 Server: http://{host}:{port}")
    print(f"📖 Docs: http://{host}:{port}/docs")
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    start_api_server()
