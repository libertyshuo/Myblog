# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=10, verbose_name='\u4f5c\u8005')),
                ('content', models.CharField(max_length=2000, verbose_name='\u6b63\u6587')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
