
from django.shortcuts import render
from .wikipediaApi import summary

# Create your views here.

# def search(request):
#
#     if request.method == 'GET':
#         search_query = request.GET.get('search_box', None)
#
#         return wikipedia.summary(search_query)

def searchbar(request):
    return render(request, 'header.html')

def summaryArticle(request):
    query = request.GET.get('search_box')
    if query:
        sum = summary(query)
        return render(request, 'results.html', {'sum': sum})

