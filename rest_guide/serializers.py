from django.db.models import Q
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from file_storage.models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')
    extra_kwargs = {
            'url': {'lookup_field': 'username'},     
    }
    
class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group 
    fields = ('url', 'name')

class GetElementSerializer(serializers.ModelSerializer):
  class Meta:
    model = Element 
    depth=1
    
class BookSerializer(serializers.ModelSerializer):
  elements = serializers.SerializerMethodField()
  
  def get_elements(self, obj):
    elements = Element.objects.filter((Q(book__pk=obj.id) | Q(theme__pk=obj.theme_id)),
    ~Q(pk__in = Element.objects.filter(book__pk=obj.id, element__isnull=False).values_list('element', flat=True)))
    serializer = ElementSerializer(elements, context=self.context, many=True)
    return serializer.data
  class Meta:
    model = Book
    fields = (
      'id',
      'title',
      'url',
      'theme',
      'elements',
    )
    read_only_fields = ('elements',)
    depth=1

    
    



    
class BookPartSerializer(serializers.ModelSerializer):
  class Meta:
    model = BookPart
    fields = (
      'id',
      'section',
    )
    
class ImageFileSerializer(serializers.ModelSerializer):
  image = serializers.SerializerMethodField()
  thumb = serializers.SerializerMethodField()
  
  def get_image(self, obj):
        return obj.image.url
    
  def get_thumb(self, obj):
        return obj.thumbnail_url
  
  class Meta:
    model = ImageFile
    fields = (
      'id',
      'url',
      'date_created',
      'date_modified',
      'image',
      'thumb',
    )
    
class ElementAttributeLabelTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ElementAttributeLabelType

class ElementImageAttributeSerializer(serializers.ModelSerializer):
  image = serializers.StringRelatedField()
  thumb = serializers.SerializerMethodField()
  
  def get_thumb(self, obj):
        return obj.image.thumbnail_url
  
  class Meta:
    model = ElementImageAttribute
    fields = (
      'id',
      'label',
      'image',
      'thumb',
    )

class ElementTextAttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ElementTextAttribute
    fields = (
      'id',
      'label',
      'text',
    )

class ElementAttributeRelatedField(serializers.RelatedField):
  def to_representation(self, value):
        
        if isinstance(value, ElementImageAttribute):
            serializer = ElementImageAttributeSerializer(value, context=self.context)
        elif isinstance(value, ElementTextAttribute):
            serializer = ElementTextAttributeSerializer(value, context=self.context)
        else:
            raise Exception('Unexpected type of element attribute object')

        return serializer.data
  

class ElementSerializer(serializers.ModelSerializer):
  parent = serializers.PrimaryKeyRelatedField(
        source='element',
        read_only=True,
    )
  book_part = serializers.SlugRelatedField(
        read_only=True,
        slug_field='section'
    )
  element_attributes = ElementAttributeRelatedField(
               many=True,
               read_only=True,
  )
  class Meta:
    model = Element 
    fields = (
      'id',
      'name',
      'url',
      'book',
      'theme',
      'pub_date',
      'mod_date',
      'book_part',
      'parent',
      'element_attributes',
      )
    depth=1
    
class ThemeSerializer(serializers.ModelSerializer):
  elements = ElementSerializer(many=True)
  
  class Meta:
    model = Theme
    fields = (
      'id',
      'title',
      'url',
      'books',
      'elements',
    )
    read_only_fields = ('books',)
    depth=2