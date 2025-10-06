"""Quick launcher for web server"""
import sys
sys.path.insert(0, 'src')

from streamforge.web.api_server import app
import uvicorn

if __name__ == "__main__":
    print("🚀 Starting StreamForge-Pro Web Server...")
    print("📡 API: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
