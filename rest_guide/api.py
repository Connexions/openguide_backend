from .models import Element, ElementAttributes, ElementAttributeType
from .serializers import ElementSerializer, ElementAttributesSerializer,ElementAttributeTypeSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class ElementList(APIView):
  
  def get(self, request, formant=None):
    elements = Element.objects.filter()
    serialized_elements = ElementSerializer(elements, many=True)
    return Response(serialized_elements.data)
  
  
  
class ElementDetail(APIView):
  
  def get_object(self, pk):
    try:
      return Element.objects.get(pk=pk)
    except Element.DoesNotExist:
      raise Http404
      
      
  def get(self, request, pk, format=None):
    element = self.get_object(pk)
    serialized_element = ElementSerializer(element)
    return Response(serialized_element.data)
    