from django.conf.urls import url
import blog.views as views
# import . from blog.views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<pk>[0-9]+)$',views.detail, name='detail'),
    url(r'^tags/$',views.get_tags, name="tag_list"),
    url(r'^tags/(?P<pk>[0-9]+)$', views.get_tags_tag, name='tag'),
    url(r'^categories/$', views.get_categories, name='category_list'),
    url(r'^categories/(?P<pk>[0-9]+)$', views.get_categories_category, name='category')
]