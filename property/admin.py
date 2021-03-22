
from property.models import Category, Place, Property, PropertyBook, PropertyImage, PropertyReview
from django.contrib import admin

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview )
admin.site.register(PropertyBook)