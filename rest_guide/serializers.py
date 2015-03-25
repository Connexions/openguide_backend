from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from file_storage.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
     model = User
     fields = ('url', 'username', 'email', 'groups')
     
class GroupSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
     model = Group 
     fields = ('url', 'name')

class ThemeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Theme
    fields = (
      'url',
      'title',
      'pub_date',
      'mod_date',
    )

class BookSerializer(serializers.HyperlinkedModelSerializer):
  theme = ThemeSerializer()
  class Meta:
    model = Book
    fields = (
      'url',
      'title',
      'pub_date',
      'mod_date',
      'theme',
    )
    
class BookPartSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = BookPart
    fields = (
      'section',
    )
    
class ImageFileSerializer(serializers.HyperlinkedModelSerializer):
  image = serializers.SerializerMethodField()
  thumb = serializers.SerializerMethodField()
  
  def get_image(self, obj):
        return obj.image.url
    
  def get_thumb(self, obj):
        return obj.thumbnail_url
  
  class Meta:
    model = ImageFile
    fields = (
      'url',
      'date_created',
      'date_modified',
      'image',
      'thumb',
    )
    
class ElementAttributeLabelTypeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ElementAttributeLabelType
    fields = (
      'label',
      'label_type',
    )

class ElementImageAttributeSerializer(serializers.HyperlinkedModelSerializer):
  image = serializers.StringRelatedField()
  thumb = serializers.SerializerMethodField()
  
  def get_thumb(self, obj):
        return obj.image.thumbnail_url
  
  class Meta:
    model = ElementImageAttribute
    fields = (
      'label',
      'image',
      'thumb',
    )

class ElementTextAttributeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ElementTextAttribute
    fields = (
      'label',
      'text',
    )

class ElementAttributeHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
  def to_representation(self, value):
        
        if isinstance(value, ElementImageAttribute):
            serializer = ElementImageAttributeSerializer(value, context=self.context)
        elif isinstance(value, ElementTextAttribute):
            serializer = ElementTextAttributeSerializer(value, context=self.context)
        else:
            raise Exception('Unexpected type of element attribute object')

        return serializer.data
  

class ElementSerializer(serializers.HyperlinkedModelSerializer):
  book = BookSerializer()
  book_part = serializers.SlugRelatedField(
        read_only=True,
        slug_field='section'
    )
  attributes = ElementAttributeHyperlinkedRelatedField(
               many=True,
               read_only=True,
               view_name='elementattribute-detail'  
  )
  class Meta:
    model = Element 
    fields = (
      'url',
      'name',
      'book',
      'pub_date',
      'mod_date',
      'book_part',
      'attributes',
      )
    
    
    
