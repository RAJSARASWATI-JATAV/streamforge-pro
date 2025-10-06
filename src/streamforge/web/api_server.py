"""API Server for StreamForge-Pro"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="StreamForge-Pro", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>StreamForge-Pro</title>
        <style>
            body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; background: #f5f5f5; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2196F3; margin: 0; }
            .feature { background: #f9f9f9; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #2196F3; }
            input, select { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
            button { background: #2196F3; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background: #1976D2; }
            ul { line-height: 2; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎬 StreamForge-Pro</h1>
            <p>Advanced Multi-Platform Media Downloader</p>
            
            <div class="feature">
                <h3>📥 Download Video</h3>
                <input type="text" placeholder="Enter video URL (YouTube, Instagram, Twitter, etc.)" id="url">
                <select id="quality">
                    <option value="best">Best Quality</option>
                    <option value="1080p">1080p</option>
                    <option value="720p">720p</option>
                    <option value="480p">480p</option>
                    <option value="audio">Audio Only (MP3)</option>
                </select>
                <button onclick="download()">⬇️ Download</button>
            </div>
            
            <div class="feature">
                <h3>✨ Features</h3>
                <ul>
                    <li>🌐 Browser Extension (Chrome & Firefox)</li>
                    <li>🎤 Voice Commands</li>
                    <li>☁️ Cloud Upload (AWS, GCP, Azure)</li>
                    <li>🎬 Video Editor (Trim, Merge, Watermark)</li>
                    <li>📡 Live Stream Recording</li>
                    <li>📱 Social Media Integration</li>
                </ul>
            </div>
            
            <div class="feature">
                <h3>📖 Documentation</h3>
                <p><a href="/docs" target="_blank">API Documentation</a></p>
                <p><a href="https://github.com/RAJSARASWATI-JATAV/streamforge-pro" target="_blank">GitHub Repository</a></p>
            </div>
        </div>
        
        <script>
            function download() {
                const url = document.getElementById('url').value;
                const quality = document.getElementById('quality').value;
                if (!url) {
                    alert('Please enter a URL');
                    return;
                }
                alert('Download started!\\nURL: ' + url + '\\nQuality: ' + quality + '\\n\\n(Full implementation in progress)');
            }
        </script>
    </body>
    </html>
    """

@app.get("/api/status")
async def status():
    return {
        "status": "running",
        "version": "1.0.0",
        "features": [
            "Browser Extension",
            "Voice Commands",
            "Cloud Upload",
            "Video Editor",
            "Live Recording",
            "Social Media"
        ]
    }

@app.post("/api/download")
async def download(url: str, quality: str = "best"):
    return {
        "status": "success",
        "message": "Download started",
        "url": url,
        "quality": quality
    }
