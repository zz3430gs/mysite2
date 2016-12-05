from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.searchbar, name='search_box'),
    url(r'^', views.summaryArticle, name='summary'),

    # url(r'^$', views.results),

]
