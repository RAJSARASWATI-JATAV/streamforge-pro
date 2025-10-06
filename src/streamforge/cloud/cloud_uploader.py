"""Cloud Upload Integration - Google Drive, Dropbox, OneDrive"""
import os
from pathlib import Path

class CloudUploader:
    def __init__(self):
        self.providers = ['google_drive', 'dropbox', 'onedrive']
    
    def upload_to_google_drive(self, file_path, folder_id=None):
        """Upload to Google Drive"""
        try:
            from googleapiclient.discovery import build
            from googleapiclient.http import MediaFileUpload
            from google.oauth2.credentials import Credentials
            
            creds = Credentials.from_authorized_user_file('token.json')
            service = build('drive', 'v3', credentials=creds)
            
            file_metadata = {'name': Path(file_path).name}
            if folder_id:
                file_metadata['parents'] = [folder_id]
            
            media = MediaFileUpload(file_path, resumable=True)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            
            print(f"✅ Uploaded to Google Drive: {file.get('id')}")
            return file.get('id')
        except Exception as e:
            print(f"❌ Google Drive upload failed: {e}")
            return None
    
    def upload_to_dropbox(self, file_path, dropbox_path='/'):
        """Upload to Dropbox"""
        try:
            import dropbox
            
            token = os.getenv('DROPBOX_TOKEN')
            dbx = dropbox.Dropbox(token)
            
            with open(file_path, 'rb') as f:
                dbx.files_upload(f.read(), f"{dropbox_path}/{Path(file_path).name}")
            
            print(f"✅ Uploaded to Dropbox")
            return True
        except Exception as e:
            print(f"❌ Dropbox upload failed: {e}")
            return False
    
    def upload_to_onedrive(self, file_path):
        """Upload to OneDrive"""
        print("⚠️ OneDrive integration coming soon!")
        return False
    
    def auto_upload(self, file_path, provider='google_drive'):
        """Auto upload to specified provider"""
        if provider == 'google_drive':
            return self.upload_to_google_drive(file_path)
        elif provider == 'dropbox':
            return self.upload_to_dropbox(file_path)
        elif provider == 'onedrive':
            return self.upload_to_onedrive(file_path)
        else:
            print(f"❌ Unknown provider: {provider}")
            return False

if __name__ == "__main__":
    uploader = CloudUploader()
    print("☁️ Cloud Uploader")
    print("1. Google Drive")
    print("2. Dropbox")
    print("3. OneDrive")
    
    choice = input("\nSelect provider: ")
    file_path = input("File path: ")
    
    if choice == '1':
        uploader.upload_to_google_drive(file_path)
    elif choice == '2':
        uploader.upload_to_dropbox(file_path)
    elif choice == '3':
        uploader.upload_to_onedrive(file_path)
