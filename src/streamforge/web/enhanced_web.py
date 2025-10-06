"""Enhanced Web Interface with API"""
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio
import uuid

app = FastAPI(title="StreamForge-Pro", version="1.0.0")

# In-memory storage
downloads = {}

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>StreamForge-Pro</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Segoe UI', Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
            .container { max-width: 1200px; margin: 0 auto; }
            .header { text-align: center; color: white; padding: 40px 0; }
            .header h1 { font-size: 48px; margin-bottom: 10px; }
            .card { background: white; border-radius: 15px; padding: 30px; margin: 20px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
            input, select { width: 100%; padding: 15px; margin: 10px 0; border: 2px solid #ddd; border-radius: 8px; font-size: 16px; }
            button { width: 100%; padding: 15px; background: #667eea; color: white; border: none; border-radius: 8px; font-size: 18px; cursor: pointer; margin: 10px 0; }
            button:hover { background: #5568d3; }
            .progress { width: 100%; height: 30px; background: #f0f0f0; border-radius: 15px; overflow: hidden; margin: 10px 0; }
            .progress-bar { height: 100%; background: linear-gradient(90deg, #667eea, #764ba2); transition: width 0.3s; text-align: center; color: white; line-height: 30px; }
            .downloads { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
            .download-item { background: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #667eea; }
            .status { display: inline-block; padding: 5px 10px; border-radius: 5px; font-size: 12px; font-weight: bold; }
            .status.completed { background: #d4edda; color: #155724; }
            .status.downloading { background: #fff3cd; color: #856404; }
            .status.failed { background: #f8d7da; color: #721c24; }
            .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0; }
            .feature { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎬 StreamForge-Pro</h1>
                <p>Advanced Multi-Platform Media Downloader</p>
            </div>
            
            <div class="card">
                <h2>📥 Download Video</h2>
                <input type="text" id="url" placeholder="Enter video URL (YouTube, Instagram, Twitter, etc.)">
                <select id="quality">
                    <option value="best">Best Quality</option>
                    <option value="1080p">1080p</option>
                    <option value="720p">720p</option>
                    <option value="480p">480p</option>
                    <option value="audio">Audio Only (MP3)</option>
                </select>
                <button onclick="startDownload()">🚀 Start Download</button>
                
                <div id="progress-container" style="display:none;">
                    <div class="progress">
                        <div class="progress-bar" id="progress-bar">0%</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2>📊 Active Downloads</h2>
                <div id="downloads" class="downloads"></div>
            </div>
            
            <div class="card">
                <h2>✨ Features</h2>
                <div class="features">
                    <div class="feature">
                        <h3>🌐 1000+ Sites</h3>
                        <p>YouTube, Instagram, Twitter, TikTok, and more</p>
                    </div>
                    <div class="feature">
                        <h3>🎯 Quality Selection</h3>
                        <p>Choose from 4K to audio-only</p>
                    </div>
                    <div class="feature">
                        <h3>⚡ Fast Downloads</h3>
                        <p>Concurrent downloads with queue</p>
                    </div>
                    <div class="feature">
                        <h3>🔄 Format Conversion</h3>
                        <p>Convert to MP4, AVI, MKV, MP3</p>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            let ws = null;
            
            function connectWebSocket() {
                ws = new WebSocket('ws://localhost:8000/ws');
                ws.onmessage = (event) => {
                    const data = JSON.parse(event.data);
                    updateDownloads(data);
                };
            }
            
            async function startDownload() {
                const url = document.getElementById('url').value;
                const quality = document.getElementById('quality').value;
                
                if (!url) {
                    alert('Please enter a URL');
                    return;
                }
                
                document.getElementById('progress-container').style.display = 'block';
                
                const response = await fetch('/api/download', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({url, quality})
                });
                
                const result = await response.json();
                alert(result.message);
                loadDownloads();
            }
            
            async function loadDownloads() {
                const response = await fetch('/api/downloads');
                const downloads = await response.json();
                
                const container = document.getElementById('downloads');
                container.innerHTML = downloads.map(d => `
                    <div class="download-item">
                        <strong>${d.title || d.url}</strong>
                        <br>
                        <span class="status ${d.status}">${d.status}</span>
                        <br>
                        Quality: ${d.quality}
                    </div>
                `).join('');
            }
            
            // Load downloads on page load
            loadDownloads();
            setInterval(loadDownloads, 5000);
        </script>
    </body>
    </html>
    """

@app.post("/api/download")
async def create_download(data: dict):
    download_id = str(uuid.uuid4())[:8]
    downloads[download_id] = {
        'id': download_id,
        'url': data['url'],
        'quality': data['quality'],
        'status': 'queued',
        'progress': 0
    }
    return {'message': f'Download started: {download_id}', 'id': download_id}

@app.get("/api/downloads")
async def get_downloads():
    return list(downloads.values())

@app.get("/api/status")
async def status():
    return {
        'status': 'running',
        'version': '1.0.0',
        'total_downloads': len(downloads)
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_json(list(downloads.values()))
        await asyncio.sleep(2)

if __name__ == "__main__":
    import uvicorn
    print("\n🌐 Starting StreamForge-Pro Web Server...")
    print("📍 URL: http://localhost:8000")
    print("Press Ctrl+C to stop\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
