"""Telegram Bot for StreamForge-Pro - Complete Implementation"""
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import yt_dlp
from pathlib import Path

class StreamForgeTelegramBot:
    def __init__(self, token):
        self.token = token
        self.app = Application.builder().token(token).build()
        self.downloads_dir = Path("downloads/telegram")
        self.downloads_dir.mkdir(parents=True, exist_ok=True)
        self._setup_handlers()
    
    def _setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("download", self.download_command))
        self.app.add_handler(CommandHandler("quality", self.quality_command))
        self.app.add_handler(CommandHandler("stats", self.stats_command))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_url))
        self.app.add_handler(CallbackQueryHandler(self.button_callback))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_text = """
🎬 **StreamForge-Pro Telegram Bot**

Welcome! I can download videos from 1000+ sites!

**Quick Start:**
• Send me any video URL
• Choose quality
• Get your video!

**Commands:**
/download <url> - Download video
/quality - Set default quality
/stats - View statistics
/help - Show help

**Supported Sites:**
YouTube, Instagram, Twitter, TikTok, Facebook, and 1000+ more!
        """
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = """
📖 **How to Use:**

**1. Download Video:**
   • Send video URL directly
   • Or use: /download <url>

**2. Choose Quality:**
   • Select from buttons
   • Or set default: /quality

**3. Get Video:**
   • Wait for processing
   • Download file

**Examples:**
• `https://youtube.com/watch?v=...`
• `/download https://instagram.com/p/...`

**Features:**
✅ 1000+ sites supported
✅ Multiple quality options
✅ Fast downloads
✅ Audio extraction
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def download_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("❌ Please provide a URL!\n\nUsage: /download <url>")
            return
        
        url = context.args[0]
        await self.process_download(update, url)
    
    async def handle_url(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        url = update.message.text.strip()
        
        if url.startswith('http://') or url.startswith('https://'):
            await self.process_download(update, url)
        else:
            await update.message.reply_text("❌ Please send a valid URL!")
    
    async def process_download(self, update: Update, url: str):
        keyboard = [
            [InlineKeyboardButton("🎬 Best Quality", callback_data=f"dl_best_{url}")],
            [InlineKeyboardButton("📺 1080p", callback_data=f"dl_1080p_{url}"),
             InlineKeyboardButton("📺 720p", callback_data=f"dl_720p_{url}")],
            [InlineKeyboardButton("📺 480p", callback_data=f"dl_480p_{url}"),
             InlineKeyboardButton("📺 360p", callback_data=f"dl_360p_{url}")],
            [InlineKeyboardButton("🎵 Audio Only (MP3)", callback_data=f"dl_audio_{url}")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text("🎯 Select Quality:", reply_markup=reply_markup)
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        
        data = query.data
        if data.startswith('dl_'):
            parts = data.split('_', 2)
            quality = parts[1]
            url = parts[2]
            
            await query.edit_message_text("⏳ Downloading... Please wait...")
            await self.download_video(query, url, quality)
    
    async def download_video(self, query, url: str, quality: str):
        try:
            ydl_opts = {
                'outtmpl': str(self.downloads_dir / '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
            }
            
            if quality == 'audio':
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            elif quality == 'best':
                ydl_opts['format'] = 'best'
            else:
                ydl_opts['format'] = f'bestvideo[height<={quality.replace("p", "")}]+bestaudio/best'
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'video')
                filename = ydl.prepare_filename(info)
            
            await query.edit_message_text("📤 Uploading...")
            
            file_path = Path(filename)
            if file_path.exists():
                file_size = file_path.stat().st_size / (1024*1024)
                
                if file_size > 50:
                    await query.edit_message_text(
                        f"❌ File too large ({file_size:.1f}MB)\n"
                        f"Telegram limit: 50MB\n\n"
                        f"Try lower quality."
                    )
                else:
                    with open(file_path, 'rb') as f:
                        if quality == 'audio':
                            await query.message.reply_audio(audio=f, title=title, caption=f"🎵 {title}")
                        else:
                            await query.message.reply_video(video=f, caption=f"🎬 {title}\n📊 Quality: {quality}")
                    
                    await query.edit_message_text("✅ Download complete!")
                    file_path.unlink()
            else:
                await query.edit_message_text("❌ Download failed!")
        
        except Exception as e:
            await query.edit_message_text(f"❌ Error: {str(e)}")
    
    async def quality_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("🎬 Best", callback_data="set_quality_best")],
            [InlineKeyboardButton("📺 1080p", callback_data="set_quality_1080p"),
             InlineKeyboardButton("📺 720p", callback_data="set_quality_720p")],
            [InlineKeyboardButton("📺 480p", callback_data="set_quality_480p")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("⚙️ Set Default Quality:", reply_markup=reply_markup)
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        stats_text = """
📊 **Bot Statistics**

✅ Status: Online
🌐 Supported Sites: 1000+
⚡ Speed: Fast
💾 Storage: Available
        """
        await update.message.reply_text(stats_text, parse_mode='Markdown')
    
    def run(self):
        print("🤖 StreamForge Telegram Bot Starting...")
        print("✅ Bot is running!")
        self.app.run_polling()

def main():
    print("🎬 StreamForge-Pro Telegram Bot")
    print("="*60)
    
    token = input("\n🔑 Enter your Telegram Bot Token: ").strip()
    
    if not token:
        print("❌ Token required!")
        print("\n📖 How to get token:")
        print("   1. Open Telegram")
        print("   2. Search for @BotFather")
        print("   3. Send /newbot")
        print("   4. Follow instructions")
        print("   5. Copy token")
        return
    
    bot = StreamForgeTelegramBot(token)
    bot.run()

if __name__ == "__main__":
    main()
