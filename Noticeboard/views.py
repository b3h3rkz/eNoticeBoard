from django.shortcuts import render
from .models import Notice, Board
from .serializers import NoticeModelSerializer, BoardSerializer, AuthorSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Endpoint to show creators of Notices and Boards
    """

    queryset = User.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BoardViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions for boards
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)


class NoticeViewSet(viewsets.ModelViewSet):
    """

    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for notices
    """
    queryset = Notice.objects.all()
    serializer_class = NoticeModelSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



