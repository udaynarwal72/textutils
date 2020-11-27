"""I made this file : Uday Singh"""
from django.http import HttpResponse
def index(request):
    return HttpResponse("Uday Singh is a good boy") 
def about(request):
    return HttpResponse(" aboutUday Singh is a good boy") 
def read(request):
    with open("1.txt", "r") as d:
        a= d.read()
    return HttpResponse(a)
