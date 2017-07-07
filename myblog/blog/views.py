from django.shortcuts import render
from django.http import HttpResponse
from . import models

# 测试样例1
def test1(request):
    return HttpResponse("Test!!")
# 测试样例2
def test2(request):
    post = models.Posts.objects.get(pk=1)
    return render(request, 'blog/test.html', {'post':post})
# ----------
# --前台界面--

# 主页
def index(request):
    return HttpResponse('Hello world')
# 文章页面
# ----------
# 后台界面

# ----------