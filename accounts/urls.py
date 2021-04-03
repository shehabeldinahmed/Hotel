
from django.urls import path

from accounts.views import profile, profile_edit, signup

app_name='accounts'

urlpatterns = [
    path('',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('profile_edit/',profile_edit,name='profile_edit'),
]
