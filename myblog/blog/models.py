from django.db import models
from django.urls import reverse
import django.utils.timezone as timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk':self.pk})

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'pk':self.pk})

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True)
    pubdate = models.DateTimeField('保存日期', auto_now_add=True)
    modifieddate = models.DateTimeField('修改日期', default=timezone.now())
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})