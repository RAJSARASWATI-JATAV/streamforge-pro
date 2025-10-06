"""Batch Download Processor"""
import asyncio
from pathlib import Path
from typing import List
import yt_dlp

class BatchProcessor:
    def __init__(self, output_dir="downloads/batch"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def process_file(self, file_path: str):
        """Process URLs from a text file"""
        urls = []
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        print(f"📋 Found {len(urls)} URLs")
        return await self.process_urls(urls)
    
    async def process_urls(self, urls: List[str]):
        """Process multiple URLs"""
        results = []
        total = len(urls)
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{total}] Processing: {url}")
            success = await self._download_single(url)
            results.append({'url': url, 'success': success})
        
        # Summary
        successful = sum(1 for r in results if r['success'])
        print(f"\n✅ Batch complete: {successful}/{total} successful")
        return results
    
    async def _download_single(self, url: str):
        """Download single video"""
        ydl_opts = {
            'format': 'best',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"  ✅ Success")
            return True
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            return False

async def main():
    """Test batch processor"""
    processor = BatchProcessor()
    
    print("🎬 Batch Download Processor")
    print("\n1. From file")
    print("2. Manual entry")
    choice = input("\nSelect: ")
    
    if choice == '1':
        file_path = input("Enter file path: ")
        await processor.process_file(file_path)
    else:
        print("\nEnter URLs (empty line to finish):")
        urls = []
        while True:
            url = input()
            if not url:
                break
            urls.append(url)
        await processor.process_urls(urls)

if __name__ == "__main__":
    asyncio.run(main())
