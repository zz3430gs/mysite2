from django.shortcuts import render

def index(request):
    return render(request, 'photoapp/home.html')

# Create your views here.
