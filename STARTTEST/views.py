from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    if(request.method=='POST'):
        first_name=request.POST.get('firstname')    
        second_name=request.POST.get('lastname')
        password=request.POST.get('password') 
    return render(request,'signup.html')
