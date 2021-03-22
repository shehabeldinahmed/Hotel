
from about.views import aboutview
from django.urls import path

urlpatterns = [
    path('', aboutview ,),
]
