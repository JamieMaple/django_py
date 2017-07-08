from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

# --前台界面--

# 主页
def index(request):
    post_list = models.Post.objects.all().order_by("-pubdate")
    return render(request, 'blog/index.html', {'post_list':post_list})
# 文章页面
def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'blog/postPage.html', {'post':post})
# ----------
# 后台界面

# ----------