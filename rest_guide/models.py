import datetime
from django.db import models
from django.utils import timezone
from file_storage.models import ImageFile
from polymorphic import PolymorphicModel


class Theme(models.Model):
  title = models.CharField(max_length=25)
  pub_date = models.DateTimeField('date published', auto_now_add=True)
  mod_date = models.DateTimeField('modified date', auto_now=True)
  def __str__(self):
    return self.title

class Book(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published', auto_now_add=True)
  mod_date = models.DateTimeField('modified date', auto_now=True)
  theme = models.ForeignKey(Theme, related_name='books')
  def __str__(self):
    return self.title
    
class BookPart(models.Model):
  section = models.CharField(max_length=50)
  def __str__(self):
    return self.section
    
class Element(models.Model):
  name = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published', auto_now_add=True)
  mod_date = models.DateTimeField('modified date', auto_now=True)
  book = models.ForeignKey(Book, blank=True, null=True, related_name='elements')
  book_part = models.ForeignKey(BookPart)
  theme = models.ForeignKey(Theme, blank=True, null=True, related_name='elements')
  element = models.ForeignKey('self', blank=True, null=True, related_name='parent')
  def __str__(self):
    return self.name
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Published recently?'


class ElementAttribute(PolymorphicModel):
  element = models.ForeignKey(Element, related_name='attributes')
  label = models.CharField(max_length=25)
  
  def __str__(self):
    return '%s' % (self.label)
  
  
class ElementImageAttribute(ElementAttribute):
  image = models.ForeignKey(ImageFile, blank=True, null=True)
  
  def __str__(self):
    return '%s: %s' % (self.label, self.image)
  
class ElementTextAttribute(ElementAttribute):
  text = models.TextField()
  
  def __str__(self):
    return '%s: %s' % (self.label, self.text)

class ElementAttributeLabelType(models.Model):
  IMAGE = 'IMG'
  TEXT = 'TXT'
  LABEL_TYPE_CHOICES = (
    (IMAGE, 'Image'),
    (TEXT, 'Text'),
  )
  label = models.CharField(max_length=25, unique=True)
  label_type = models.CharField(max_length=3, choices=LABEL_TYPE_CHOICES, default=TEXT) 
  
  def __str__(self):
    return self.label
  
  