from django import forms
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import *
from file_storage.models import *

# Register your models here.

TEXT_ATTRIBUTE_LABELS = (
  ('Font', 'Font'),
  ('Color', 'Color')
)

IMAGE_ATTRIBUTE_LABELS = (
  ('PDF', 'PDF'),
  ('Web', 'Web')
)


class ElementTextAttributeForm(forms.ModelForm):
  label = forms.ChoiceField(widget=forms.Select, choices=TEXT_ATTRIBUTE_LABELS)

class ElementImageAttributeForm(forms.ModelForm):
  label = forms.ChoiceField(widget=forms.Select, choices=IMAGE_ATTRIBUTE_LABELS)  
  
class ElementAttributeChildAdmin(PolymorphicChildModelAdmin):
  base_model = ElementAttribute
  
  
class ElementImageAttributeAdmin(ElementAttributeChildAdmin):
  form = ElementImageAttributeForm

class ElementTextAttributeAdmin(ElementAttributeChildAdmin):
  form = ElementTextAttributeForm

class ElementAttributeParentAdmin(PolymorphicParentModelAdmin):
  base_model = ElementAttribute
  child_models = (
    (ElementImageAttribute, ElementImageAttributeAdmin),
    (ElementTextAttribute, ElementTextAttributeAdmin), 
  )
  
class ElementImageAttributeInline(admin.TabularInline):
  model = ElementImageAttribute
  form = ElementImageAttributeForm
  fk_name = 'element'
  readonly_fields = ['elementattribute_ptr']
  extra = 0

  
class ElementTextAttributeInline(admin.TabularInline):
  model = ElementTextAttribute
  form = ElementTextAttributeForm
  fk_name = 'element'
  readonly_fields = ['elementattribute_ptr']
  extra = 0

class ElementAdmin(admin.ModelAdmin):
  inlines = [ElementImageAttributeInline,ElementTextAttributeInline]
  list_display = ('name', 'book_part', 'book', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['name']

admin.site.register(ElementAttribute, ElementAttributeParentAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Book)
admin.site.register(BookPart)
admin.site.register(Theme)

