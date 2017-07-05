from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True)
    pubdate = models.DateTimeField('保存日期', auto_now_add=True)
    modifieddate = models.DateTimeField('最后修改日期', auto_now=True)
    def __str__(self):
        return self.title