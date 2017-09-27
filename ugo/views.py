# encoding: utf-8
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from ugo.models import urlist


# Create your views here.
def index(request):
    template = get_template('transfer_index.html')
    now = datetime.now
    dante_test_parameter = "Dante's Homepage"
    user_lists = list()
    user_lists.append({'name': 'Richard'})
    user_lists.append({'name': 'John'})
    user_lists.append({'name': 'Mary'})
    html = template.render(locals())
    return HttpResponse(html)


def about(request):
    return HttpResponse("It's Dante.")


def hello(request, username):
    return HttpResponse("Hello " + username)


def listall(request):
    template = get_template('transfer_listall.html')
    all = urlist.objects.all()
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)


def gourl(request, short_url):
    try:
        rec = urlist.objects.get(short_url=short_url)
        target_url = rec.src_url
        rec.count += 1
        rec.save()
    except:
        target_url = '/notfound/' + short_url
    return redirect(target_url)


def notfound(request, id):
    template = get_template('transfer_notfound.html')
    now = datetime.now
    html = template.render({'id': id, 'now': now})
    return HttpResponse(html)

def about(request):
    template = get_template('transfer_About.html')
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)