from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.urls import reverse

from ..accounts.models import User
from .models import Message, Comment
from .forms import MessageForm, CommentForm



class MessageList(View):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        messages = Message.objects.filter(to_id = pk)
        messageform = MessageForm()
        commentform = CommentForm()
        context = {
            'user': user,
            'messages': messages,
            'messageform': messageform,
            'commentform': commentform
        }
        return render(request, 'messageboard/message_list.html', context)


    def post(self,request, pk):
        
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            message = Message.objects.create(
                message = request.POST['message'],
                from_id = User.objects.get(email=request.user),
                to_id = User.objects.get(id=pk)
            )
            message.save()
        
        
        return redirect(reverse('messages:message_list', kwargs={'pk': pk }))


class PostComment(View):
    def post(self, request, pk, id):
    
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = Comment.objects.create(
                comment = request.POST['comment'],
                from_id = User.objects.get(email=request.user),
                message_id = Message.objects.get(id=id),
            )
            comment.save()

        return redirect(reverse('messages:message_list', kwargs={'pk': pk }))
        

