from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def register(request):
    return render(request, 'register.html')

def registerdata(request):
    # return render(request, 'register.html')
    print(request.method)
    print(request.POST)
    name=request.POST.get('fname')
    email=request.POST.get('email')
    contact=request.POST.get('contactno')
    print(name,email,contact)




