from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from django.template.loader import get_template
from messageRoom.forms import MessageForm
from messageRoom.models import Message
from datetime import datetime
from django.utils import timezone

def board(request):
        template = get_template('board.html')
        messages = Message.objects.all()
        response_string = list()
        for q in messages:
                response_string.append({'message_sentance': '<br>'.join(["user: %s, subject: %s, time: %s" % (q.user, q.subject, q.publication_date)])})
        now = datetime.now
        html = template.render(locals())
        return HttpResponse(html)

def post(request):
        if request.method == 'POST':
                form = MessageForm(request.POST)
                if form.is_valid():
                        message = Message(user=form.cleaned_data['user'],subject=form.cleaned_data['subject'], publication_date=timezone.now())
                        message.save()
                        return redirect('/board/')
        else:
                form = MessageForm()
        return render(request,'post.html',{'form': form})
        