from rest_framework import serializers
from .models import Board, Notice
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    notices = serializers.HyperlinkedRelatedField(queryset=Notice.objects.all(), view_name='notice-detail', many=True)
    boards = serializers.HyperlinkedRelatedField(queryset=Board.objects.all(), view_name='board-detail', many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'notices', 'boards',)


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    """
     Class that serializes the boards model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Board
        fields = ('id', 'name', 'notices', 'user',)
        depth = 1


class NoticeModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    Notices serializer
    """

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Notice
        fields = ('id', 'title', 'created', 'user', 'board', 'body', 'slug', 'image', 'attachment')


