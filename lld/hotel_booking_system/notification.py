class Notification:
    def __init__(self, receiver, message):
        self.receiver = receiver
        self.message = message

    def send(self):
        print(f"message sent to {self.receiver}")