from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Notice, Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ("name", "created",)


class NoticeAdmin(MarkdownModelAdmin):
    list_display = ('title',  'created', 'body', 'board', 'attachment', 'image', )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Board, BoardAdmin)
