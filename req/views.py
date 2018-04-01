from django.http import HttpResponse
from django.shortcuts import render
from .models import Request
# Create your views here.


def handle(request, params=None):
    params = 'explicit_params=' + str(params)
    info = ' '.join(map(
        str,
        [
            request.method,
            request.body,
            request.content_params,
            request.content_params,
            request.path,
            request.path_info,
            request.COOKIES,
            params,
        ]
    ))
    r = Request(head=str(request), body=info)
    r.save()
    return HttpResponse('your request added to db')


def show(request):
    requests = Request.objects.all()
    return render(request, 'req/show.html', {'requests': requests})
