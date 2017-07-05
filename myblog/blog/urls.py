from django.conf.urls import url
import blog.views as views
# import . from blog.views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^test1/$', views.test1),
    url(r'^test2/$', views.test2),
]