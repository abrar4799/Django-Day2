from django.shortcuts import render
from .models import MyRegister2
from django.shortcuts import redirect

# Create your views here
from django.http import HttpResponse

def index(request,name):
   return HttpResponse(f'<h1>Welcome {name}</h1>')

def navbar(request):
   return render(request , 'nv.html')

def contactus(request):
   return render(request, 'contactus.html')

def about(request):
   return render(request, 'about.html')

def register(request):
   if(request.method == 'GET'):
     return render(request, 'register.html')
   else:
      MyRegister2.objects.create(userName=request.POST['userName'] , password2=request.POST['password2'] , email=request.POST['email'])
      return redirect(login)


def login(request):
   if(request.method == 'GET'):
      return render(request, 'Login.html')
   else:
      pass
def checklogin(request):
  if(request.method == 'POST'):
       #check Pass & UserName
      user= MyRegister2.objects.filter(userName=request.POST['userName'] , password2=request.POST['password2'])
      if(user is not None):
          return render(request, 'nv.html')
      else:
          return render(request, 'login.html')




