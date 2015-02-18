from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage

fs_store = FileSystemStorage(location=settings.DOCUMENT_ROOT)
fs_image_store = FileSystemStorage(location=settings.IMAGE_DOCUMENT_ROOT)

class StoredFile(models.Model):
    file = models.FileField(storage=fs_store)
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        abstract = True

class ImageFile(StoredFile):
    file = models.ImageField(storage=fs_image_store)
