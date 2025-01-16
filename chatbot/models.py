from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    # Get the first user from the database or define another way to provide a default sender
    default_sender = User.objects.first()  # Make sure this doesn't return None

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE, default=default_sender)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.timestamp}"
