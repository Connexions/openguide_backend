import datetime
from django.db import models
from file_storage.models import ImageFile

# Create your models here.
class Element(models.Model):
  name = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  book = models.ManyToManyField(Book)
  def __str__(self):
    return self.name
  
  
class elementAttributes(models.Model):
  ANNOSRC = 'annoSrc'
  PDFSRC = 'pdfSrc'
  WEBSRC = 'webSrc'
  CNXML = 'cnxml'
  NOTE = 'note'
  STYLE = 'style'
  SLOT = 'slot'
  SKELETON = 'skeleton'
  SECTION = 'section'
  TYPE_CHOICES = (
    (ANNOSRC, 'annoSrc'),
    (PDFSRC, 'pdfSrc'),
    (WEBSRC, 'webSrc'),
    (CNXML, 'cnxml'),
    (NOTE, 'note'),
    (STYLE, 'style'),
    (SLOT, 'slot'),
    (SKELETON, 'skeleton')
    (SECTION, 'section')
  )

  element = models.ForeignKey(Element)
  type = models.CharField(max_length=25,
                          choices=TYPE_CHOICES)
  data = models.TextField('attribute data')
  def __str__(self):
    return self.type
    
  #Leaving in place for testing
  #annotatedSrc = models.ForeignKey(ImageFile)
  #pdfSrc = models.ForeignKey(ImageFile)
  #webSrc = models.ForeignKey(ImageFile)
  #cnxml = models.CharField('cnxml code')
  #note = models.CharField('W&N notes')
  #style = models.CharField('W&N font size/family')
  #slot = models.CharField('css slot code') 
  #skeleton = models.CharField('css skeleton')
  #section = models.CharField('section of book element is located')
  
    
    
 
  
class Book(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField('date published')
  theme = models.ForeignKey(Theme);
  def __str__(self):
    return self.title
    
class Theme(models.Model):
  MATH = 'M'
  SCIENCE = 'S'
  HUMANITIES = 'H'
  THEME_CHOICES = (
    (MATH, 'Math'),
    (SCIENCE, 'Science'),
    (HUMANITIES, 'Humanities')
  )
  title = models.CharField(max_length=1,
                           choices=THEME_CHOICES)
  def __str__(self):
    return self.title
    
      