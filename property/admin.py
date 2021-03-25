
from property.models import Category, Place, Property, PropertyBook, PropertyImage, PropertyReview
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Property , SomeModelAdmin)
admin.site.register(PropertyImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview )
admin.site.register(PropertyBook)