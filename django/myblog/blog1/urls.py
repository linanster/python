"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^hello/', views.hello_handler),
    url(r'^$', views.article_list_page),
    url(r'^article_content/(?P<article_id>[0-9]+)$', views.article_content_page, name='article_content'),
    url(r'^article_edit_page/(?P<article_id>[0-9]+)$', views.article_edit_page, name='article_edit_page'),
    url(r'^article_edit_action$', views.article_edit_action, name='article_edit_action'),
]




