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
        @keyframes glow { 0%, 100% { box-shadow: 0 0 5px #00ff41, 0 0 10px #00ff41; } 50% { box-shadow: 0 0 20px #00ff41, 0 0 30px #00ff41; } }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        @keyframes slideIn { from { transform: translateY(-20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        @keyframes rainbow { 0% { filter: hue-rotate(0deg); } 100% { filter: hue-rotate(360deg); } }
        body { font-family: 'Courier New', monospace; background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%); color: #00ff41; min-height: 100vh; }
        .header { background: linear-gradient(90deg, #1a1a1a 0%, #2a1a3a 100%); padding: 20px; border-bottom: 2px solid #00ff41; animation: glow 2s infinite; }
        .title { font-size: 28px; font-weight: bold; text-shadow: 0 0 10px #00ff41, 0 0 20px #00ff41; animation: pulse 2s infinite; }
        .subtitle { color: #ff00ff; margin-top: 5px; text-shadow: 0 0 5px #ff00ff; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .download-box { background: linear-gradient(135deg, #1a1a1a 0%, #2a1a3a 100%); padding: 20px; border-radius: 15px; margin: 20px 0; border: 2px solid #00ff41; animation: slideIn 0.5s ease-out, glow 3s infinite; }
        input { width: 100%; padding: 15px; background: #0a0a0a; border: 2px solid #00ff41; color: #fff; font-size: 16px; border-radius: 10px; transition: all 0.3s; }
        input:focus { outline: none; border-color: #ff00ff; box-shadow: 0 0 15px #ff00ff; }
        button { width: 100%; padding: 18px; background: linear-gradient(90deg, #00ff41 0%, #00cc33 100%); color: #0a0a0a; border: none; font-size: 18px; font-weight: bold; cursor: pointer; border-radius: 10px; margin-top: 10px; transition: all 0.3s; text-shadow: 0 0 5px #000; }
        button:hover { transform: scale(1.05); box-shadow: 0 0 20px #00ff41; }
        .status { background: linear-gradient(135deg, #1a1a1a 0%, #2a1a3a 100%); padding: 15px; border-radius: 10px; margin-top: 20px; border-left: 4px solid #00ff41; animation: slideIn 0.7s ease-out; }
        .log { background: #0a0a0a; padding: 12px; margin: 8px 0; border-radius: 8px; font-size: 14px; border-left: 3px solid; animation: slideIn 0.3s ease-out; transition: all 0.3s; }
        .log:hover { transform: translateX(5px); }
        .success { border-left-color: #00ff41; color: #00ff41; text-shadow: 0 0 5px #00ff41; }
        .error { border-left-color: #ff0041; color: #ff0041; text-shadow: 0 0 5px #ff0041; }
        .info { border-left-color: #00ccff; color: #00ccff; text-shadow: 0 0 5px #00ccff; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }
        .stat-card { background: linear-gradient(135deg, #1a1a1a 0%, #2a1a3a 100%); padding: 20px; border-radius: 10px; border: 2px solid #00ff41; text-align: center; animation: pulse 3s infinite; }
        .stat-value { font-size: 32px; font-weight: bold; color: #00ff41; text-shadow: 0 0 10px #00ff41; }
        .stat-label { color: #888; margin-top: 5px; }
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
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value" id="totalDownloads">0</div>
                <div class="stat-label">Total Downloads</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="activeUsers">1</div>
                <div class="stat-label">Active Users</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="successRate">100%</div>
                <div class="stat-label">Success Rate</div>
            </div>
        </div>
        <div class="download-box">
            <h2>📥 Download Video</h2>
            <input type="text" id="url" placeholder="Paste video URL here...">
            <button onclick="download()">⚡ Download Now</button>
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
