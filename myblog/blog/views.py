from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import markdown
from . import models

# --前台界面--

# 主页 / 分页
def index(request):
    post_list = models.Post.objects.all().order_by("-pubdate")
    return render(request, 'blog/index.html', {"post_list":post_list})

# 文章页面
def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    #MarkDown
    post.content = markdown.markdown(post.content,
                                     extensions=['markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc',])
    tags = models.Tag.objects.filter(post=post)
    return render(request, 'blog/postPage.html', {'post':post, 'tags':tags})

# 归档
def archives(request):
    dates =  models.Post.objects.dates('pubdate', 'month', order='DESC')
    return render(request, 'blog/archive_index.html',  {'dates':dates})
def archives_get_archive(request, year, month):
    post_list = models.Post.objects.filter(pubdate__year=year, pubdate__month=month).order_by('-pubdate')
    return render(request, 'blog/archive.html', {'post_list':post_list, 'year':year, 'month':month})

# tags
def get_tags(request):
    tags = models.Tag.objects.all().order_by("name")
    return render(request, 'blog/tags.html', {'tags':tags})
def get_tags_tag(request, pk):
    tag = models.Tag.objects.get(pk=pk)
    post_list = models.Post.objects.filter(tags = tag).order_by("-pubdate")
    return render(request, 'blog/archive.html', {'post_list':post_list, 'tag':tag})

# categories
def get_categories(request):
    categories = models.Category.objects.all().order_by("name")
    return render(request, 'blog/categories.html', {'categories': categories})

def get_categories_category(request, pk):
    category = models.Category.objects.get(pk=pk)
    post_list = models.Post.objects.filter(category=category).order_by("-pubdate")
    return render(request, 'blog/archive.html', {'post_list':post_list, 'category':category})

# 分页
# ----------
# 后台界面

# ----------