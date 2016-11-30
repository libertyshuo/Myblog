#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(u'标题', max_length=50)
    author = models.CharField(u'作者', max_length=10)
    content = models.CharField(u'正文', max_length=2000)
    post_date = models.DateTimeField(u'发布时间',auto_now_add=True)
    class Meta:
        ordering = ['-post_date']