from django.db import models
from django_markdown.models import MarkdownField
from django.http import request
from django.contrib.auth.models import User


class Board(models.Model):
    """
    A board will contain many different notices, more like the noticeboard in reality where a new board can be created every now and then
    """
    name = models.CharField(max_length=50, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #user = models.ForeignKey('auth.User', null=True, related_name='boards')

    def __str__(self):
        return self.name

    def notices(self):
        return self.notice_set.all()


class Notice(models.Model):
    """
    A notice can be pasted on many different notice boards, with an option of adding images
    """
    title = models.CharField(max_length=50, blank=False)
    body = models.TextField(help_text='Enter any message here')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, help_text='add a screenshot or image, this is optional')
    slug = models.SlugField(null=True, blank=True)
    attachment = models.FileField(verbose_name="attachment", blank=True, null=True, help_text='add optional attachment', upload_to='media/%Y/%m/%d')
    board = models.ForeignKey(Board, related_name="notices")
    user = models.ForeignKey('auth.User', null=True, related_name='notices')
    body = MarkdownField()

    def __str__(self):
        return self.title

