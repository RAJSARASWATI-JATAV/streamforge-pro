"""Social Media Integration Manager"""
import asyncio
from pathlib import Path
from typing import Optional, Dict, List
import tweepy
from instagrapi import Client as InstaClient
import facebook

class SocialMediaManager:
    """Manage social media integrations"""
    
    def __init__(self):
        self.twitter_api = None
        self.instagram_client = None
        self.facebook_api = None
        
    def configure_twitter(self, api_key: str, api_secret: str, 
                         access_token: str, access_secret: str):
        """Configure Twitter API"""
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        self.twitter_api = tweepy.API(auth)
        
    def configure_instagram(self, username: str, password: str):
        """Configure Instagram"""
        self.instagram_client = InstaClient()
        self.instagram_client.login(username, password)
        
    def configure_facebook(self, access_token: str):
        """Configure Facebook API"""
        self.facebook_api = facebook.GraphAPI(access_token)
        
    async def post_to_twitter(self, text: str, media_path: Optional[Path] = None) -> Dict:
        """Post to Twitter"""
        if not self.twitter_api:
            raise ValueError("Twitter not configured")
            
        try:
            if media_path:
                media = self.twitter_api.media_upload(str(media_path))
                tweet = self.twitter_api.update_status(status=text, media_ids=[media.media_id])
            else:
                tweet = self.twitter_api.update_status(status=text)
                
            return {
                'status': 'success',
                'tweet_id': tweet.id,
                'url': f'https://twitter.com/user/status/{tweet.id}'
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
            
    async def post_to_instagram(self, image_path: Path, caption: str) -> Dict:
        """Post to Instagram"""
        if not self.instagram_client:
            raise ValueError("Instagram not configured")
            
        try:
            media = self.instagram_client.photo_upload(str(image_path), caption)
            return {
                'status': 'success',
                'media_id': media.id,
                'url': f'https://instagram.com/p/{media.code}'
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
            
    async def post_to_facebook(self, message: str, media_path: Optional[Path] = None) -> Dict:
        """Post to Facebook"""
        if not self.facebook_api:
            raise ValueError("Facebook not configured")
            
        try:
            if media_path:
                with open(media_path, 'rb') as f:
                    post = self.facebook_api.put_photo(image=f, message=message)
            else:
                post = self.facebook_api.put_object('me', 'feed', message=message)
                
            return {
                'status': 'success',
                'post_id': post['id'],
                'url': f'https://facebook.com/{post["id"]}'
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
            
    async def share_download(self, file_path: Path, platforms: List[str], 
                            caption: str = "") -> Dict[str, Dict]:
        """Share downloaded content to multiple platforms"""
        results = {}
        
        for platform in platforms:
            if platform == 'twitter':
                results['twitter'] = await self.post_to_twitter(caption, file_path)
            elif platform == 'instagram':
                results['instagram'] = await self.post_to_instagram(file_path, caption)
            elif platform == 'facebook':
                results['facebook'] = await self.post_to_facebook(caption, file_path)
                
        return results
        
    async def auto_share_on_download(self, file_path: Path, platforms: List[str]):
        """Automatically share when download completes"""
        caption = f"Downloaded via StreamForge-Pro 🎬"
        return await self.share_download(file_path, platforms, caption)
        
    async def get_twitter_trends(self, location_id: int = 1) -> List[str]:
        """Get Twitter trending topics"""
        if not self.twitter_api:
            raise ValueError("Twitter not configured")
            
        trends = self.twitter_api.get_place_trends(location_id)
        return [trend['name'] for trend in trends[0]['trends'][:10]]
        
    async def download_twitter_media(self, tweet_url: str) -> List[str]:
        """Download media from Twitter tweet"""
        if not self.twitter_api:
            raise ValueError("Twitter not configured")
            
        tweet_id = tweet_url.split('/')[-1]
        tweet = self.twitter_api.get_status(tweet_id, tweet_mode='extended')
        
        media_urls = []
        if 'media' in tweet.entities:
            for media in tweet.extended_entities['media']:
                if media['type'] == 'video':
                    variants = media['video_info']['variants']
                    video_url = max(
                        [v for v in variants if v['content_type'] == 'video/mp4'],
                        key=lambda x: x.get('bitrate', 0)
                    )['url']
                    media_urls.append(video_url)
                else:
                    media_urls.append(media['media_url_https'])
                    
        return media_urls
