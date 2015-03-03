# from django.contrib.auth.models import User, Group 
# from rest_framework import serializers
# 
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = User
#     fields = ('url', 'username', 'email', 'groups')
#     
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = Group 
#     fields = ('url', 'name')

from .models import Element, ElementAttributes, ElementAttributeType
from rest_framework import serializers

class ElementAttributeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ElementAttributeType
    fields = (
      'label',
    )


class ElementAttributesSerializer(serializers.ModelSerializer):
  attribute_type = ElementAttributeTypeSerializer()
  class Meta:
    model = ElementAttributes
    fields = (
      'attribute_type',
      'data',
      )
   

class ElementSerializer(serializers.ModelSerializer):
  element_attributes = ElementAttributesSerializer(many=True, required=False)
  class Meta:
    model = Element 
    fields = (
      'id',
      'name',
      'book',
      'pub_date',
      'mod_date',
      'book_part',
      'element_attributes',
      )
    depth = 2
    
    

