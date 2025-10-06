chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'download') {
    chrome.runtime.sendNativeMessage('com.streamforge.native', {
      action: 'download',
      url: request.url,
      quality: request.quality
    }, response => {
      if (chrome.runtime.lastError) {
        sendResponse({ success: false, error: chrome.runtime.lastError.message });
      } else {
        sendResponse({ success: true, jobId: response.job_id });
      }
    });
    return true;
  } else if (request.action === 'openApp') {
    chrome.tabs.create({ url: 'http://localhost:8000' });
  }
});

chrome.contextMenus.create({
  id: 'streamforge-download',
  title: 'Download with StreamForge',
  contexts: ['link', 'video', 'audio']
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === 'streamforge-download') {
    const url = info.linkUrl || info.srcUrl;
    chrome.runtime.sendNativeMessage('com.streamforge.native', {
      action: 'download',
      url: url,
      quality: 'best'
    });
  }
});
