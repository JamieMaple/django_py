from django.shortcuts import render
from django.http import HttpResponse
from . import models

# 测试样例1
def test1(request):
    return HttpResponse("Test!!")
# 测试样例2
def test2(request):
    return render(request, 'blog/test.html', context={'index':'prop'})
# ----------

# --前台界面--

# 主页
def index(request):
    post_list = models.Post.objects.all().order_by("-pubdate")
    return render(request, 'blog/index.html', {'post_list':post_list})
# 文章页面
# ----------
# 后台界面

# ----------