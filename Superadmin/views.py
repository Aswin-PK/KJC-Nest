from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')
    # return HttpResponse("hello")

def login(request):
    return render(request, 'login.html')