from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage

fs_store = FileSystemStorage(location=settings.DOCUMENT_ROOT)
fs_image_store = FileSystemStorage(location=settings.IMAGE_DOCUMENT_ROOT)

class StoredFile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BinaryFile(StoredFile):
    file = models.FileField(storage=fs_store)

class ImageFile(StoredFile):
    file = models.ImageField(storage=fs_image_store)
