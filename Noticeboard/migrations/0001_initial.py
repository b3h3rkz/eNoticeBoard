# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, help_text='add a screenshot or image, this is optional', upload_to='')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, help_text='add optional attachment', null=True, upload_to='media/%Y/%m/%d', verbose_name='attachment')),
                ('body', django_markdown.models.MarkdownField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices', to='Noticeboard.Board')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notices', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
