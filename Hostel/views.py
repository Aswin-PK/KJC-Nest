from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'hostel/dashboard.html')
    # return HttpResponse("hello")

def transactions(request):
    return render(request, 'hostel/view_transaction.html')