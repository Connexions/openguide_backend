from django.contrib import admin
from .models import *

# Register your models here.
class ImageFileAdmin(admin.ModelAdmin):
  readonly_fields = ('admin_thumbnail',)
  
  
admin.site.register(ImageFile, ImageFileAdmin)

