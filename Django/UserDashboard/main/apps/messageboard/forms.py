from django import forms
from .models import Message, Comment

class MessageForm(forms.Form):
    message = forms.CharField(max_length=1000)
        

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1000)
    
    