from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
# Create your views here.


def article_list(request):
    article_list = Article.objects.all()
    

    context = {'articles': article_list}

    return render(request, 'articles/article_list.html', context)

def article_detail(request, slug):
    article_detail = Article.objects.get(slug=slug)

    article = article_detail

    return render(request, 'articles/article_detail.html', {'article':article})