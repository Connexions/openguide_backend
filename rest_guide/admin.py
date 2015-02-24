from django.contrib import admin
from .models import Element, Book, Theme, ElementAttributes, ElementAttributeType, BookPart

# Register your models here.
class ElementAttributesInline(admin.TabularInline):
  model = ElementAttributes
  extra = 5
  
class ElementAdmin(admin.ModelAdmin):
  inlines = [ElementAttributesInline]
  list_display = ('name', 'book_part', 'book', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['name']


admin.site.register(Element, ElementAdmin)
admin.site.register(Book)
admin.site.register(BookPart)
admin.site.register(Theme)
admin.site.register(ElementAttributeType)

