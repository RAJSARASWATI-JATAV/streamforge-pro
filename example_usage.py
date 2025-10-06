"""
StreamForge-Pro - Example Usage
Demonstrates how to use the simple downloader
"""

from src.streamforge.core.simple_downloader import SimpleDownloader


def example_1_basic_download():
    """Example 1: Basic video download"""
    print("\n" + "="*60)
    print("Example 1: Basic Video Download")
    print("="*60)
    
    downloader = SimpleDownloader(output_dir="downloads/videos")
    
    # Replace with actual video URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example URL
    
    downloader.download(url, quality="best")


def example_2_audio_extraction():
    """Example 2: Extract audio only"""
    print("\n" + "="*60)
    print("Example 2: Audio Extraction")
    print("="*60)
    
    downloader = SimpleDownloader(output_dir="downloads/audio")
    
    # Replace with actual video URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example URL
    
    downloader.download(url, audio_only=True)


def example_3_specific_quality():
    """Example 3: Download with specific quality"""
    print("\n" + "="*60)
    print("Example 3: Specific Quality Download")
    print("="*60)
    
    downloader = SimpleDownloader(output_dir="downloads/720p")
    
    # Replace with actual video URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example URL
    
    downloader.download(url, quality="720p")


def example_4_get_info():
    """Example 4: Get video information"""
    print("\n" + "="*60)
    print("Example 4: Get Video Information")
    print("="*60)
    
    downloader = SimpleDownloader()
    
    # Replace with actual video URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example URL
    
    info = downloader.get_video_info(url)
    
    if info:
        print("\n✅ Successfully retrieved video information!")


def main():
    """Main function to run examples"""
    print("\n🎬 StreamForge-Pro - Example Usage")
    print("="*60)
    print("\nAvailable Examples:")
    print("1. Basic video download")
    print("2. Audio extraction (MP3)")
    print("3. Specific quality download (720p)")
    print("4. Get video information")
    print("5. Run all examples")
    print("0. Exit")
    
    choice = input("\nSelect example (0-5): ").strip()
    
    if choice == "1":
        example_1_basic_download()
    elif choice == "2":
        example_2_audio_extraction()
    elif choice == "3":
        example_3_specific_quality()
    elif choice == "4":
        example_4_get_info()
    elif choice == "5":
        print("\n⚠️  Running all examples will download multiple files!")
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == 'y':
            example_1_basic_download()
            example_2_audio_extraction()
            example_3_specific_quality()
            example_4_get_info()
    elif choice == "0":
        print("\n👋 Goodbye!")
        return
    else:
        print("\n❌ Invalid choice!")
        return
    
    print("\n✨ Examples completed!")
    print("📁 Check the 'downloads' folder for your files")


if __name__ == "__main__":
    main()
