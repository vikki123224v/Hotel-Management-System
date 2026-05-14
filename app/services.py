import threading
import time

class NotificationService:
    """
    Simulates a Pub/Sub service for cloud architecture concepts.
    In a real cloud deployment, this could use Google Cloud Pub/Sub, AWS SNS/SQS, or Redis.
    """
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def publish(self, event_type, data):
        def notify():
            time.sleep(1) # Simulate network propagation delay
            for sub in self.subscribers:
                sub(event_type, data)
                
        # Fire in background thread so it doesn't block the request
        threading.Thread(target=notify, daemon=True).start()

# Global instance
notification_service = NotificationService()

def default_logger(event_type, data):
    print(f"\\n[PUB/SUB NOTIFICATION] EVENT: {event_type} | DATA: {data}\\n")

# Subscribe a default background worker that logs notifications to console
notification_service.subscribe(default_logger)
