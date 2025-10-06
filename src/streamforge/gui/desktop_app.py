"""PyQt6 Desktop GUI Application"""
try:
    from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel
    from PyQt6.QtCore import Qt
    PYQT_AVAILABLE = True
except:
    PYQT_AVAILABLE = False

class StreamForgeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StreamForge-Pro Desktop")
        self.setGeometry(100, 100, 800, 600)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        layout.addWidget(QLabel("🎬 StreamForge-Pro Desktop"))
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter video URL...")
        layout.addWidget(self.url_input)
        
        download_btn = QPushButton("Download")
        download_btn.clicked.connect(self.download)
        layout.addWidget(download_btn)
        
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)
    
    def download(self):
        url = self.url_input.text()
        self.log.append(f"Downloading: {url}")

def launch_gui():
    if not PYQT_AVAILABLE:
        print("Install PyQt6: pip install PyQt6")
        return
    
    app = QApplication([])
    window = StreamForgeGUI()
    window.show()
    app.exec()

if __name__ == "__main__":
    launch_gui()
