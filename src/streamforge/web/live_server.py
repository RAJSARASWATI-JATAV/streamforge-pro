"""
Live Server with WebSocket for StreamForge-Pro
Created by RAJSARASWATI JATAV
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
from typing import List

app = FastAPI(title="StreamForge-Pro Live Server")

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>StreamForge-Pro Live</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Courier New', monospace; background: #0a0a0a; color: #00ff41; }
        .header { background: #1a1a1a; padding: 20px; border-bottom: 2px solid #00ff41; }
        .title { font-size: 24px; font-weight: bold; }
        .subtitle { color: #888; margin-top: 5px; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .download-box { background: #1a1a1a; padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #00ff41; }
        input { width: 100%; padding: 15px; background: #0a0a0a; border: 2px solid #00ff41; color: #fff; font-size: 16px; border-radius: 5px; }
        button { width: 100%; padding: 15px; background: #00ff41; color: #0a0a0a; border: none; font-size: 18px; font-weight: bold; cursor: pointer; border-radius: 5px; margin-top: 10px; }
        button:hover { background: #00cc33; }
        .status { background: #1a1a1a; padding: 15px; border-radius: 5px; margin-top: 20px; border-left: 4px solid #00ff41; }
        .log { background: #0a0a0a; padding: 10px; margin: 5px 0; border-radius: 3px; font-size: 14px; }
        .success { border-left-color: #00ff41; }
        .error { border-left-color: #ff0041; color: #ff0041; }
        .info { border-left-color: #00ccff; color: #00ccff; }
    </style>
</head>
<body>
    <div class="header">
        <div class="container">
            <div class="title">🎬 StreamForge-Pro Live Server</div>
            <div class="subtitle">Created by RAJSARASWATI JATAV | Real-time Downloads</div>
        </div>
    </div>
    <div class="container">
        <div class="download-box">
            <h2>📥 Download Video</h2>
            <input type="text" id="url" placeholder="Paste video URL here...">
            <button onclick="download()">Download Now</button>
        </div>
        <div class="status">
            <h3>📊 Live Status</h3>
            <div id="logs"></div>
        </div>
    </div>
    <script>
        const ws = new WebSocket("ws://localhost:8080/ws");
        
        ws.onmessage = function(event) {
            const logs = document.getElementById('logs');
            const log = document.createElement('div');
            log.className = 'log info';
            log.textContent = event.data;
            logs.insertBefore(log, logs.firstChild);
        };
        
        function download() {
            const url = document.getElementById('url').value;
            if (!url) {
                alert('Enter URL');
                return;
            }
            ws.send(JSON.stringify({action: 'download', url: url}));
            addLog('Downloading: ' + url, 'info');
        }
        
        function addLog(msg, type) {
            const logs = document.getElementById('logs');
            const log = document.createElement('div');
            log.className = 'log ' + type;
            log.textContent = msg;
            logs.insertBefore(log, logs.firstChild);
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(HTML)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"📥 Processing: {data}")
            await asyncio.sleep(1)
            await manager.broadcast(f"✅ Completed: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

def start_live_server(host: str = "0.0.0.0", port: int = 8080):
    print("🚀 StreamForge-Pro Live Server")
    print("📍 Created by: RAJSARASWATI JATAV")
    print(f"🌐 Server: http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    start_live_server()
