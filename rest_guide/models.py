import datetime
from django.db import models
from file_storage.models import ImageFile

class Element(models.Model):
  name = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  mod_date = models.DateTimeField('modified date')
  book = models.ForeignKey(Book)
  def __str__(self):
    return self.name
  
  
class ElementAttributes(models.Model):
  element = models.ForeignKey(Element)
  attribute_type = models.ForeignKey(ElementAttributeType)
  data = models.TextField('attribute data')
  
  def __str__(self):
    return self.attribute_type
    
class ElementAttributeType(models.Model):
  label = models.CharField(max_length=25)
  
  def __str(self):
    return self.label
      
class Book(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  mod_date = models.DateTimeField('modified date')
  theme = models.ForeignKey(Theme);
  def __str__(self):
    return self.title
    
class Theme(models.Model):
  title = models.CharField(max_length=25)
  pub_date = models.DateTimeField('date published')
  mod_date = models.DateTimeField('modified date')
  def __str__(self):
    return self.title
    
