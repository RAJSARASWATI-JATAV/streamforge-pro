"""Enhanced PyQt6 GUI with Full Features"""
try:
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                                 QHBoxLayout, QPushButton, QLineEdit, QTextEdit, 
                                 QLabel, QComboBox, QProgressBar, QListWidget, QTabWidget)
    from PyQt6.QtCore import Qt, QThread, pyqtSignal
    PYQT_AVAILABLE = True
except:
    PYQT_AVAILABLE = False

if PYQT_AVAILABLE:
    class DownloadThread(QThread):
        progress = pyqtSignal(int)
        finished = pyqtSignal(str)
        
        def __init__(self, url, quality):
            super().__init__()
            self.url = url
            self.quality = quality
        
        def run(self):
            import yt_dlp
            
            def progress_hook(d):
                if d['status'] == 'downloading':
                    try:
                        percent = float(d.get('_percent_str', '0%').replace('%', ''))
                        self.progress.emit(int(percent))
                    except:
                        pass
            
            ydl_opts = {
                'format': self.quality,
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'progress_hooks': [progress_hook],
                'quiet': True
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(self.url, download=False)
                    title = info.get('title', 'Unknown')
                    ydl.download([self.url])
                    self.finished.emit(f"✅ Downloaded: {title}")
            except Exception as e:
                self.finished.emit(f"❌ Error: {e}")

    class StreamForgeGUI(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("StreamForge-Pro Desktop")
            self.setGeometry(100, 100, 900, 700)
            
            central = QWidget()
            self.setCentralWidget(central)
            layout = QVBoxLayout(central)
            
            # Title
            title = QLabel("🎬 StreamForge-Pro Desktop")
            title.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
            layout.addWidget(title)
            
            # Tabs
            tabs = QTabWidget()
            tabs.addTab(self._create_download_tab(), "Download")
            tabs.addTab(self._create_queue_tab(), "Queue")
            tabs.addTab(self._create_history_tab(), "History")
            layout.addWidget(tabs)
            
            # Status bar
            self.statusBar().showMessage("Ready")
        
        def _create_download_tab(self):
            widget = QWidget()
            layout = QVBoxLayout(widget)
            
            # URL input
            url_layout = QHBoxLayout()
            url_layout.addWidget(QLabel("URL:"))
            self.url_input = QLineEdit()
            self.url_input.setPlaceholderText("Enter video URL...")
            url_layout.addWidget(self.url_input)
            layout.addLayout(url_layout)
            
            # Quality selector
            quality_layout = QHBoxLayout()
            quality_layout.addWidget(QLabel("Quality:"))
            self.quality_combo = QComboBox()
            self.quality_combo.addItems(['best', '1080p', '720p', '480p', 'audio'])
            quality_layout.addWidget(self.quality_combo)
            layout.addLayout(quality_layout)
            
            # Download button
            download_btn = QPushButton("📥 Download")
            download_btn.clicked.connect(self.start_download)
            download_btn.setStyleSheet("padding: 10px; font-size: 14px;")
            layout.addWidget(download_btn)
            
            # Progress bar
            self.progress_bar = QProgressBar()
            layout.addWidget(self.progress_bar)
            
            # Log
            self.log = QTextEdit()
            self.log.setReadOnly(True)
            layout.addWidget(self.log)
            
            return widget
        
        def _create_queue_tab(self):
            widget = QWidget()
            layout = QVBoxLayout(widget)
            
            layout.addWidget(QLabel("Download Queue:"))
            self.queue_list = QListWidget()
            layout.addWidget(self.queue_list)
            
            return widget
        
        def _create_history_tab(self):
            widget = QWidget()
            layout = QVBoxLayout(widget)
            
            layout.addWidget(QLabel("Download History:"))
            self.history_list = QListWidget()
            layout.addWidget(self.history_list)
            
            return widget
        
        def start_download(self):
            url = self.url_input.text()
            if not url:
                self.log.append("❌ Please enter a URL")
                return
            
            quality = self.quality_combo.currentText()
            self.log.append(f"📥 Starting download: {url}")
            self.log.append(f"🎯 Quality: {quality}")
            
            self.download_thread = DownloadThread(url, quality)
            self.download_thread.progress.connect(self.update_progress)
            self.download_thread.finished.connect(self.download_finished)
            self.download_thread.start()
            
            self.queue_list.addItem(f"{url} ({quality})")
        
        def update_progress(self, value):
            self.progress_bar.setValue(value)
            self.statusBar().showMessage(f"Downloading... {value}%")
        
        def download_finished(self, message):
            self.log.append(message)
            self.progress_bar.setValue(100)
            self.statusBar().showMessage("Ready")
            self.history_list.addItem(message)

def launch_gui():
    if not PYQT_AVAILABLE:
        print("❌ PyQt6 not installed!")
        print("Install: pip install PyQt6")
        return
    
    app = QApplication([])
    window = StreamForgeGUI()
    window.show()
    app.exec()

if __name__ == "__main__":
    launch_gui()
