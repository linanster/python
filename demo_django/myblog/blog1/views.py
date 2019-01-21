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

def article_list_page(request):
    articles = models.Article.objects.all()
    return render(request, 'blog1_article_list.html', {'articles': articles})

def article_content_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog1_article_content.html', {'article': article})

def article_edit_page(request, article_id):
    # 新建博客
    if str(article_id) == '0':
	return render(request, 'blog1_article_edit.html')
    # 修改博客
    else:
	article = models.Article.objects.get(pk=article_id)
	return render(request, 'blog1_article_edit.html', {'article': article})


def article_edit_action(request):
    article_title = request.POST.get('article_title')
    article_content = request.POST.get('article_content')
    article_id = request.POST.get('article_id')
    # 新建博客
    if article_id == '0':
	models.Article.objects.create(title=article_title, content=article_content)
	articles = models.Article.objects.all()
	return render(request, 'blog1_article_list.html', {'articles': articles})
    # 修改博客
    else:
	article = models.Article.objects.get(pk=article_id)
	article.title = article_title
	article.content = article_content
	article.save()
	return render(request, 'blog1_article_content.html', {'article': article})
