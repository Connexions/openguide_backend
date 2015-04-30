from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
from PIL import Image
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
    image = models.ImageField(storage=fs_image_store)
    
    def __str__(self):
      return '%s' % (self.image.url)
    

    def _thumbnail_url(self):
        filename, ext = os.path.splitext(self.image.name)
        new_file_path = settings.IMAGE_MEDIA_URL + filename[2:] + "_thumbnail" + ext

        return new_file_path
    thumbnail_url = property(_thumbnail_url)
  
    def admin_thumbnail(self):
        if self.image.path:   
          return u'<img src="%s" />' % (self.thumbnail_url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
    
    def save(self, *args, **kwargs):
        """
        Make and save the thumbnail for the photo here.
        """
        super(ImageFile, self).save(*args, **kwargs)
        if not self.make_thumbnail():
            raise Exception('Could not create thumbnail - is the file type valid?')

    def make_thumbnail(self):
        """
        Create and save the thumbnail for the photo (simple resize with PIL).
        """
        #fh = fs_image_store.open(self.image.path, 'r')
        THUMB_SIZE = (128,128)
        #try:
        image = Image.open(self.image.path)
        #except:
        #   return False

        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
        #fh.close()

        # Path to save to, name, and extension
        thumb_name, thumb_extension = os.path.splitext(self.image.path)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumbnail' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail
        image.save(thumb_filename, FTYPE)


        return True
      
