
from about.views import aboutview
from django.urls import path


app_name ='about'

urlpatterns = [
    path('', aboutview ,),
]
