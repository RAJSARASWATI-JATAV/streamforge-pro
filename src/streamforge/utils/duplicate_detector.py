"""Duplicate File Detector"""
import hashlib
from pathlib import Path

class DuplicateDetector:
    def __init__(self):
        self.hashes = {}
    
    def get_file_hash(self, filepath):
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def find_duplicates(self, directory):
        print(f"🔍 Scanning for duplicates in {directory}")
        duplicates = []
        for file in Path(directory).rglob('*'):
            if file.is_file():
                file_hash = self.get_file_hash(file)
                if file_hash in self.hashes:
                    duplicates.append((file, self.hashes[file_hash]))
                else:
                    self.hashes[file_hash] = file
        print(f"Found {len(duplicates)} duplicates")
        return duplicates
