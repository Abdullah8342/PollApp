from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World Your at the poll index')
