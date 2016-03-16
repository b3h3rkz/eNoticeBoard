from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework import views
from Noticeboard import views

router = DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'notices', views.NoticeViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url('^markdown/', include('django_markdown.urls')),
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

