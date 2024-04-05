from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #for routing templates
def registration(request):
    return HttpResponse("Welcome to registration!")
# Create your views here.

def mypage(request):
   template = loader.get_template('register.html')
   return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render)

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render)




