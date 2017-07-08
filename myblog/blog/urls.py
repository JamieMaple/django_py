from django.conf.urls import url
import blog.views as views
# import . from blog.views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<pk>[0-9]+)$',views.detail, name='detail')
]