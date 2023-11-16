from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticle , ContactRequest
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views import View

class ArticleDetailView(DetailView):
    model = BlogArticle
    template_name = 'article_detail.html' 
    context_object_name = 'article'


class ArticleListView(ListView):
    model = BlogArticle
    paginate_by = 5
    template_name = 'article_list.html'  
    context_object_name = 'articles'  

class CreateBlogArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_article.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = User.objects.first()
        publication_datetime = timezone.now()

        article = BlogArticle(title=title, content=content, author=author, publication_datetime=publication_datetime)

        article.save()
        return HttpResponse("create_article...")
    
class CreateContactRequestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_contact.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        name = request.POST.get('name')
        content = request.POST.get('content')
        contact_request = ContactRequest(email=email, name=name, content=content)
        contact_request.save()
        return HttpResponse("create_contact...")
    

# ------ Func Base

# def create_blog_article(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         author = User.objects.first() 
#         article = BlogArticle(title=title, content=content, author=author)
#         article.save()
#         return HttpResponse("create_blog!")
#     return render(request, 'create_article.html')

# def create_contact_request(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         name = request.POST.get('name')
#         content = request.POST.get('content')
#         contact_request = ContactRequest(email=email, name=name, content=content)
#         contact_request.save()
#         return HttpResponse("create_contact")
#     return render(request, 'create_contact.html')

