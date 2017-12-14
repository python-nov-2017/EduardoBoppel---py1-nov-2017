from __future__ import unicode_literals

from django.db import models
from ..accounts.models import User

class Message(models.Model):
    message = models.TextField()
    from_id = models.ForeignKey(User, related_name="sent_messages")
    to_id = models.ForeignKey(User, related_name="received_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    from_id = models.ForeignKey(User, related_name="sent_comments")
    message_id = models.ForeignKey(Message, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
