from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from rest_guide import api

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/elements/$', api.ElementList.as_view()),
    url(r'^api/elements/(?P<pk>[0-9]+)/$', api.ElementDetail.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns = format_suffix_patterns(urlpatterns)
# 
# 
# 
# from django.conf.urls import include, url
# from rest_framework import routers
# from openguide_backend.rest_guide import views
# #from django.contrib import admin
# #from django.contrib.auth.models import User
# #from rest_framework import router, serializers, viewsets
# 
# router = router.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# 
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'openguide_backend.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^', include('rest_guide.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# ]
