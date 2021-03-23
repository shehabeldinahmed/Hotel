
from property.views import PropertyDetail, PropertyList
from django.urls import path


app_name ='property'

urlpatterns = [
    path('',PropertyList.as_view(), name='property_list'),
    path('<slug:slug>',PropertyDetail.as_view(), name='property_detail'),
]
