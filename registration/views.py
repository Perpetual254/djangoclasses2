from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #for routing templates

from registration.models import registerstudents


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

def about(request):
    template =loader.get_template('about.html')
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())



def addstudent (request):
  if request.method == 'POST':
    name = request.POST.get('fname','lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    age = request.POST.get('age')
    query = registerstudents(student=name,email=email,phone=phone,age=age )
    query.save()


    data= registerstudents.objects.all();
    context = {'data':data }
    return render(request, 'dashboard.html', context)








