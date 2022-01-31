from django.shortcuts import render

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
   return render(request, 'register.html')

def login(request):
   return render(request, 'login.html')

def insertuser(request):
   context={}
   if(request.method == 'GET'):
      return render(request,'register.html',context)
   else:
      context['method'] = 'post'
      return render(request, 'register.html', context)


