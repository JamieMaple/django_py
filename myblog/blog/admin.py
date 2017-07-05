from django.contrib import admin
from blog.models import Posts
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "content")

admin.site.register(Posts, PostsAdmin)