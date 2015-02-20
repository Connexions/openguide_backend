import datetime
from django.db import models
from file_storage.models import ImageFile
from enumfields import EnumField
from enum import Enum  # Uses Ethan Furman's "enum34" backport


class Element(models.Model):
  name = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  book = models.ManyToManyField(Book)
  def __str__(self):
    return self.name
  
  
class elementAttributes(models.Model):
  
  class Types(Enum):
    PDFSRC = 'pSrc'
    CNXML = 'cnxml'
    NOTE = 'note'
    FONTCOLOR = 'color'
    FONTSIZE = 'fsize'
    FONTFAM = 'ffam' 
    SLOT = 'sl'
    SKELETON = 'sk'
    SECTION = 'sect'
    
    class Labels:
      PDFSRC = 'PDF Screenshot'
      FONTCOLOR = 'Font Color'
      FONTSIZE = 'Font Size'
      FONTFAM = 'Font Family' 
      SLOT = 'Slot Code'
      SKELETON = 'Skeleton Code'
      SECTION = 'Book Section'

  element = models.ForeignKey(Element)
  type = EnumField(Types, max_length=10) 
  data = models.TextField('attribute data')
  
  def __str__(self):
    return self.type
    
    
class Book(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  theme = models.ForeignKey(Theme);
  def __str__(self):
    return self.title
    
class Theme(models.Model):
  
  class Types(Enum):
    MATH = 'M'
    SCIENCE = 'S'
    HUMANITIES = 'H'
  
  title = EnumField(Types, max_length=1)
  def __str__(self):
    return self.title