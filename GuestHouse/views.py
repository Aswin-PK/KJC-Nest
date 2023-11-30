from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'guesthouse/dashboard.html')
    # return HttpResponse("hello")



