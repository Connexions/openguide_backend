from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
import os

fs_store = FileSystemStorage(location=settings.DOCUMENT_ROOT)
fs_image_store = FileSystemStorage(location=settings.IMAGE_DOCUMENT_ROOT, base_url=settings.IMAGE_MEDIA_URL)

class StoredFile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BinaryFile(StoredFile):
    file = models.FileField(storage=fs_store)

class ImageFile(StoredFile):
    file = models.ImageField(storage=fs_image_store)
    
    def __str__(self):
      return '%s' % (self.file)

    def _thumbnail_url(self):
        filename, ext = os.path.splitext(self.file.name)
        new_file_path = settings.IMAGE_MEDIA_URL + filename[2:] + "_thumbnail.png"

        return new_file_path
    thumbnail_url = property(_thumbnail_url)
  
    def admin_thumbnail(self):
       
        return u'<img src="%s" />' % (self.thumbnail_url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True