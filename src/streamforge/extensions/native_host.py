"""Native Messaging Host for Browser Extensions"""
import json
import sys
import struct
import asyncio
from typing import Dict, Any

class NativeMessagingHost:
    """Handle communication between browser extension and StreamForge"""
    
    def __init__(self, download_manager):
        self.download_manager = download_manager
        
    def read_message(self) -> Dict[str, Any]:
        """Read message from browser extension"""
        raw_length = sys.stdin.buffer.read(4)
        if not raw_length:
            return None
        message_length = struct.unpack('=I', raw_length)[0]
        message = sys.stdin.buffer.read(message_length).decode('utf-8')
        return json.loads(message)
    
    def send_message(self, message: Dict[str, Any]):
        """Send message to browser extension"""
        encoded = json.dumps(message).encode('utf-8')
        sys.stdout.buffer.write(struct.pack('=I', len(encoded)))
        sys.stdout.buffer.write(encoded)
        sys.stdout.buffer.flush()
    
    async def handle_download(self, url: str, quality: str = "best"):
        """Handle download request from extension"""
        job_id = await self.download_manager.add_download(url, quality)
        return {"status": "success", "job_id": job_id}
    
    async def run(self):
        """Main message loop"""
        while True:
            message = self.read_message()
            if not message:
                break
                
            action = message.get("action")
            
            if action == "download":
                result = await self.handle_download(
                    message.get("url"),
                    message.get("quality", "best")
                )
                self.send_message(result)
            elif action == "status":
                status = self.download_manager.get_download_status(message.get("job_id"))
                self.send_message({"status": "success", "data": status})
