from django.shortcuts import render

def index(request):
    return render(request, 'photoapp/home.html')

# def twitter(request):
#     return render(request, 'photoapp/twitterapi.py')

# Create your views here.
