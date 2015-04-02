from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from .serializers import *
import django_filters


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows themes to be viewed or edited
    """
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    lookup_field = 'title'
    filter_fields = ('title','elements__name',)
    ordering_fields = ('title',)

    
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'title'
    filter_fields = ('title','elements__name')
    ordering_fields = ('title', 'theme__title', 'elements__name')
    
class ElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_fields = ('name','book__title', 'theme__title',)
    ordering_fields = ('name', 'theme__title', 'book__title',)

    
class ElementImageAttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited
    """
    queryset = ElementImageAttribute.objects.all()
    serializer_class = ElementImageAttributeSerializer
    
class ElementTextAttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited
    """
    queryset = ElementTextAttribute.objects.all()
    serializer_class = ElementTextAttributeSerializer
    
class ImageFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited
    """
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer
   
class ElementAttributeLabelTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements label types to be viewed or edited
    """
    queryset = ElementAttributeLabelType.objects.all()
    serializer_class = ElementAttributeLabelTypeSerializer
