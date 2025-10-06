"""SQLite Database Manager"""
import sqlite3
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_path="streamforge.db"):
        self.db_path = Path(db_path)
        self.conn = None
        self.init_db()
    
    def init_db(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS downloads (
                id TEXT PRIMARY KEY,
                url TEXT,
                title TEXT,
                status TEXT,
                progress REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_download(self, download_id, url, title):
        self.conn.execute(
            'INSERT INTO downloads (id, url, title, status, progress) VALUES (?, ?, ?, ?, ?)',
            (download_id, url, title, 'queued', 0)
        )
        self.conn.commit()
    
    def update_progress(self, download_id, progress, status='downloading'):
        self.conn.execute(
            'UPDATE downloads SET progress=?, status=? WHERE id=?',
            (progress, status, download_id)
        )
        self.conn.commit()
    
    def get_all_downloads(self):
        cursor = self.conn.execute('SELECT * FROM downloads ORDER BY created_at DESC')
        return cursor.fetchall()
    
    def get_stats(self):
        cursor = self.conn.execute('''
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN status='completed' THEN 1 ELSE 0 END) as completed,
                AVG(progress) as avg_progress
            FROM downloads
        ''')
        return cursor.fetchone()
