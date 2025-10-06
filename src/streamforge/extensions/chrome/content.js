// StreamForge-Pro Browser Extension - Content Script
// Created by RAJSARASWATI JATAV
// Copyright (c) 2025 RAJSARASWATI JATAV

// Detect video elements on page
function detectVideos() {
    const videos = document.querySelectorAll('video');
    const videoData = [];
    
    videos.forEach(video => {
        if (video.src) {
            videoData.push({
                url: video.src,
                title: document.title,
                duration: video.duration
            });
        }
    });
    
    return videoData;
}

// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'detectVideos') {
        const videos = detectVideos();
        sendResponse({ videos: videos });
    }
    return true;
});

// Auto-detect and notify
const videos = detectVideos();
if (videos.length > 0) {
    chrome.runtime.sendMessage({
        action: 'videosDetected',
        count: videos.length
    });
}
