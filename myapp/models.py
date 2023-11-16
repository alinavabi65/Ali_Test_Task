from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_datetime = models.DateTimeField()
    is_online = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogArticle, self).save(*args, **kwargs)

class ContactRequest(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
