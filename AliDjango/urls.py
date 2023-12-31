"""AliDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('create-article/', views.create_blog_article, name='create_blog_article'),
    # path('create-contact/', views.create_contact_request, name='create_contact_request'),
    path('create-article/', views.CreateBlogArticleView.as_view(), name='create_blog_article'),
    path('create-contact/', views.CreateContactRequestView.as_view(), name='create_contact_request'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
