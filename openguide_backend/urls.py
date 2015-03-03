from django.conf.urls import patterns, include, url
from django.contrib import admin

<<<<<<< HEAD
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_guide import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'themes', views.ThemeViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'elements', views.ElementViewSet)


urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]
=======
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/', include('file_storage.urls')),
)
>>>>>>> Added views for uploads, added thumbnail generation
