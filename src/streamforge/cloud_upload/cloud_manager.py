"""Cloud Upload Manager"""
import asyncio
import boto3
from google.cloud import storage as gcs
from azure.storage.blob import BlobServiceClient
from pathlib import Path
from typing import Optional, Dict

class CloudUploadManager:
    """Manage uploads to various cloud providers"""
    
    def __init__(self):
        self.aws_s3 = None
        self.gcp_storage = None
        self.azure_blob = None
        
    def configure_aws(self, access_key: str, secret_key: str, bucket: str, region: str = 'us-east-1'):
        """Configure AWS S3"""
        self.aws_s3 = {
            'client': boto3.client('s3', 
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region
            ),
            'bucket': bucket
        }
        
    def configure_gcp(self, credentials_path: str, bucket: str):
        """Configure Google Cloud Storage"""
        self.gcp_storage = {
            'client': gcs.Client.from_service_account_json(credentials_path),
            'bucket': bucket
        }
        
    def configure_azure(self, connection_string: str, container: str):
        """Configure Azure Blob Storage"""
        self.azure_blob = {
            'client': BlobServiceClient.from_connection_string(connection_string),
            'container': container
        }
        
    async def upload_to_aws(self, file_path: Path, object_name: Optional[str] = None) -> str:
        """Upload file to AWS S3"""
        if not self.aws_s3:
            raise ValueError("AWS S3 not configured")
            
        object_name = object_name or file_path.name
        
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, 
            self.aws_s3['client'].upload_file,
            str(file_path), 
            self.aws_s3['bucket'], 
            object_name
        )
        
        return f"s3://{self.aws_s3['bucket']}/{object_name}"
        
    async def upload_to_gcp(self, file_path: Path, object_name: Optional[str] = None) -> str:
        """Upload file to Google Cloud Storage"""
        if not self.gcp_storage:
            raise ValueError("GCP Storage not configured")
            
        object_name = object_name or file_path.name
        bucket = self.gcp_storage['client'].bucket(self.gcp_storage['bucket'])
        blob = bucket.blob(object_name)
        
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, blob.upload_from_filename, str(file_path))
        
        return f"gs://{self.gcp_storage['bucket']}/{object_name}"
        
    async def upload_to_azure(self, file_path: Path, blob_name: Optional[str] = None) -> str:
        """Upload file to Azure Blob Storage"""
        if not self.azure_blob:
            raise ValueError("Azure Blob not configured")
            
        blob_name = blob_name or file_path.name
        blob_client = self.azure_blob['client'].get_blob_client(
            container=self.azure_blob['container'],
            blob=blob_name
        )
        
        with open(file_path, 'rb') as data:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, blob_client.upload_blob, data, overwrite=True)
        
        return f"azure://{self.azure_blob['container']}/{blob_name}"
        
    async def auto_upload(self, file_path: Path, provider: str = 'aws') -> Dict[str, str]:
        """Auto upload to configured provider"""
        result = {'status': 'success', 'url': None}
        
        try:
            if provider == 'aws' and self.aws_s3:
                result['url'] = await self.upload_to_aws(file_path)
            elif provider == 'gcp' and self.gcp_storage:
                result['url'] = await self.upload_to_gcp(file_path)
            elif provider == 'azure' and self.azure_blob:
                result['url'] = await self.upload_to_azure(file_path)
            else:
                result['status'] = 'error'
                result['message'] = f'{provider} not configured'
        except Exception as e:
            result['status'] = 'error'
            result['message'] = str(e)
            
        return result
