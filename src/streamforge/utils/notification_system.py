"""Desktop Notification System"""
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except:
    PLYER_AVAILABLE = False

class NotificationSystem:
    def send(self, title, message):
        if PLYER_AVAILABLE:
            notification.notify(title=title, message=message, timeout=5)
        else:
            print(f"📢 {title}: {message}")
