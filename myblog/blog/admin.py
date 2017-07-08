from django.contrib import admin
from blog.models import Post, Category, Tag
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "pubdate", "category")

admin.site.register(Post, PostsAdmin)
admin.site.register(Category)
admin.site.register(Tag)