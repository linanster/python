# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def hello_handler(request):
    # return HttpResponse('Hello,World!')
    # return render(request, 'hello.html')
    # return render(request, 'hello.html', {'name': 'Allen'})
    article_Python = models.Article.objects.get(title='Python')
    article_Django = models.Article.objects.get(title='Django')
    return render(request, 'hello.html', {'article_Python': article_Python, 'article_Django': article_Django})

def blog1_main_handler(request):
    articles = models.Article.objects.all()
    return render(request, 'blog1_main.html', {'articles': articles})
def blog1_article_handler(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog1_article.html', {'article': article})
