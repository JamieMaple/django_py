from django.conf.urls import url
import blog.views as views
# import . from blog.views
urlpatterns = [
    url(r'^test1/$', views.test1),
    url(r'^test2/$', views.test2),
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<pk>[0-9]+)$',views.detail, name='detail')
]