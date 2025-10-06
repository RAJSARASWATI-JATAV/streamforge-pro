document.getElementById('downloadBtn').addEventListener('click', async () => {
  const quality = document.getElementById('quality').value;
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
  chrome.runtime.sendMessage({
    action: 'download',
    url: tab.url,
    quality: quality
  }, response => {
    const status = document.getElementById('status');
    status.style.display = 'block';
    if (response.success) {
      status.className = 'success';
      status.textContent = '✅ Download started successfully!';
    } else {
      status.className = 'error';
      status.textContent = '❌ Error: ' + response.error;
    }
  });
});

document.getElementById('openApp').addEventListener('click', () => {
  chrome.runtime.sendMessage({ action: 'openApp' });
});
