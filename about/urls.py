
from about.views import AboutView
from django.urls import path


app_name ='about'

urlpatterns = [
    path('',AboutView.as_view() ,name='about'),
]
