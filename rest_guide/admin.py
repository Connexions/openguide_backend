from django import forms
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import *
from file_storage.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

class ElementTextAttributeForm(forms.ModelForm):
  label = forms.ModelChoiceField(queryset=ElementAttributeLabelType.objects.filter(label_type='TXT'), to_field_name="label", empty_label=None)

class ElementImageAttributeForm(forms.ModelForm):
  label = forms.ModelChoiceField(queryset=ElementAttributeLabelType.objects.filter(label_type='IMG'), to_field_name="label", empty_label=None)

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
  exclude = ('mod_date','pub_date')
  list_filter = ['pub_date']
  search_fields = ['name']


admin.site.register(ElementAttribute, ElementAttributeParentAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Book)
admin.site.register(BookPart)
admin.site.register(Theme)
admin.site.register(ElementAttributeLabelType)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
