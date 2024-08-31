from plyer import notification
import config

def send_notification(message):
    notification.notify(
        title=config.NOTIFICATION_TITLE,
        message=message,
        timeout=10
    )
