import datetime
from django.db import models
from django.utils import timezone
#from file_storage.models import ImageFile


class Theme(models.Model):
  title = models.CharField(max_length=25)
  pub_date = models.DateTimeField('date published')
  mod_date = models.DateTimeField('modified date')
  def __str__(self):
    return self.title

class Book(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  mod_date = models.DateTimeField('modified date')
  theme = models.ForeignKey(Theme)
  def __str__(self):
    return self.title
    
class BookPart(models.Model):
  section = models.CharField(max_length=50)
  def __str__(self):
    return self.section
    
class Element(models.Model):
  name = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  mod_date = models.DateTimeField('modified date')
  book = models.ForeignKey(Book)
  book_part = models.ForeignKey(BookPart)
  def __str__(self):
    return self.name
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Published recently?'
  

class ElementAttributeType(models.Model):
  label = models.CharField(max_length=25)
  
  def __str__(self):
    return self.label
      
  
class ElementAttributes(models.Model):
  element = models.ForeignKey(Element, related_name='attributes')
  attribute_type = models.ForeignKey(ElementAttributeType)
  data = models.TextField('attribute data')
  
  
  def __str__(self):
    return '%s: %s' % (self.attribute_type, self.data)
    
