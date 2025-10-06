"""
StreamForge-Pro Setup Script
Created by Raj Saraswati
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="streamforge-pro",
    version="1.0.0",
    author="Raj Saraswati",
    author_email="raj@streamforge.pro",
    description="Advanced Multi-Platform Media Downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajsaraswati/streamforge-pro",
    project_urls={
        "Bug Reports": "https://github.com/rajsaraswati/streamforge-pro/issues",
        "Source": "https://github.com/rajsaraswati/streamforge-pro",
        "Documentation": "https://docs.streamforge.pro"
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "yt-dlp>=2023.12.30",
        "requests>=2.31.0",
        "aiohttp>=3.9.0",
        "click>=8.1.0",
        "rich>=13.7.0",
        "pyyaml>=6.0",
        "aiosqlite>=0.19.0",
        "pillow>=10.1.0",
        "psutil>=5.9.0",
        "tqdm>=4.66.0",
    ],
    extras_require={
        "gui": ["PyQt6>=6.6.0", "qasync>=0.24.0"],
        "web": ["fastapi>=0.104.0", "uvicorn>=0.24.0", "websockets>=12.0"],
        "mobile": ["kivy>=2.2.0"],
        "all": [
            "PyQt6>=6.6.0", "qasync>=0.24.0",
            "fastapi>=0.104.0", "uvicorn>=0.24.0",
            "websockets>=12.0", "kivy>=2.2.0"
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "streamforge=streamforge.__main__:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
