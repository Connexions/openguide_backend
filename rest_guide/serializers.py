from django.db.models import Q
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from file_storage.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')
    extra_kwargs = {
            'url': {'lookup_field': 'username'},     
    }
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group 
    fields = ('url', 'name')

class GetElementSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Element 
    fields = (
      'url',
    )
    
#    from pprint import pformat
#    import logging
#    logging.root.setLevel(logging.DEBUG)
#    logging.debug(pformat(theme_elements))
#    logging.debug(pformat(theme_elements))   
    

    
class BookSerializer(serializers.HyperlinkedModelSerializer):
  elements = serializers.SerializerMethodField()
  
  def get_elements(self, obj):
    
    book_elements = Element.objects.filter(book__pk=obj.id)
    elements = Element.objects.filter( (Q(book__pk=obj.id) | Q(theme__pk=obj.theme_id)), ~Q(pk__in = [o.element_id for o in book_elements if o.element_id]))
    serializer = GetElementSerializer(elements, context=self.context, many=True)
    element_urls=[]
    for element in serializer.data:
      element_urls.append(element['url'])
    return element_urls
  class Meta:
    model = Book
    fields = (
      'title',
      'url',
      'theme',
      'elements',
    )
    read_only_fields = ('elements',)
    extra_kwargs = {
            'url': {'lookup_field': 'title'},
            'theme': {'lookup_field': 'title'},
            #'elements':{'lookup_field': 'name'}
        }
    
class ThemeBookSerializer(serializers.HyperlinkedModelSerializer):
#  elements = serializers.HyperlinkedRelatedField(
#      many=True,
#      read_only=True,
#      view_name='element-detail'
#  )
  class Meta:
    model = Book
    fields = (
      'title',
      'url',
      'elements',
    )
    read_only_fields = ('elements',)
    extra_kwargs = {
            'url': {'lookup_field': 'title'},
            'theme': {'lookup_field': 'title'},
            #'elements':{'lookup_field': 'name'}
        }    
    

class ThemeSerializer(serializers.HyperlinkedModelSerializer):
  #books = ThemeBookSerializer(many=True)
  class Meta:
    model = Theme
    fields = (
      'title',
      'url',
      'books',
      'elements',
    )
    read_only_fields = ('books',)
    extra_kwargs = {
            'url': {'lookup_field': 'title'},
            'books': {'lookup_field': 'title'},
        }


    
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
#    fields = (
#      'label',
#      'label_type',
#    )

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
  #book = BookSerializer()
  parent = serializers.HyperlinkedRelatedField(
        source='element',
        read_only=True,
        view_name='element-detail'
    )
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
      'name',
      'url',
      'book',
      'theme',
      #'pub_date',
      #'mod_date',
      'book_part',
      'parent',
      'attributes',
      )
    extra_kwargs = {
            #'url': {'lookup_field': 'name'},
            'book': {'lookup_field': 'title'},
            'theme': {'lookup_field': 'title'},
        }
    
    
