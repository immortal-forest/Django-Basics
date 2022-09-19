from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article


# Create your views here.

# templates: <appname>/<modelname>_<view>.html

# Class Based Views
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

