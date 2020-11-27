from django.http import HttpResponse

def name(request):
    a = "Enter your name"
    return HttpResponse(a)