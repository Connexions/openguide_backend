from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_guide import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'themes', views.ThemeViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'labels', views.ElementAttributeLabelTypeViewSet)
router.register(r'elements', views.ElementViewSet)
router.register(r'images', views.ImageFileViewSet)



urlpatterns = [
    url(r'^data/v1/', include(router.urls)),
    url(r'^data/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^data/api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^data/admin/', include(admin.site.urls)),
    url(r'^data/files/', include('file_storage.urls')),
]
