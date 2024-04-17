from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader #for routing templates
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def addstudent (request):
  if request.method == 'POST':
    first_name = request.POST.get('fname',)
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('number')
    age = request.POST.get('age')

    mydata = {'fname':first_name, 'lname':last_name, 'email':email, 'number':phone, 'age':age}
    print(mydata)

    obj1 = registerstudents(first_name=first_name,last_name=last_name,email=email,phone_number=phone,age=age )
    obj1.save()

  #data=registerstudents().objects.all()
  #context={'data':data}
  return render(request,'dashboard.html')










