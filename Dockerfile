# StreamForge-Pro Docker Image
# Created by RAJSARASWATI JATAV
# Copyright (c) 2025 RAJSARASWATI JATAV

FROM python:3.11-slim

LABEL maintainer="RAJSARASWATI JATAV <rajsaraswatijatav@outlook.com>"
LABEL description="StreamForge-Pro - Advanced Multi-Platform Media Downloader"
LABEL version="2.0.0"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements_complete.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements_complete.txt

# Copy application
COPY . .

# Expose port for web interface
EXPOSE 8000

# Run application
CMD ["python", "streamforge_hacker.py"]
