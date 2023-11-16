from django.contrib import admin
from .models import BlogArticle, ContactRequest

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_datetime', 'is_online']
    prepopulated_fields = {'slug': ('title',)}

class ContactRequestAdmin(admin.ModelAdmin):
    readonly_fields = ['email', 'name', 'content', 'date']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
