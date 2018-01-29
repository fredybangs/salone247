from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>WELCOME TO SALONE 247: SIERRA LEONE ON THE WEB</h1>")
