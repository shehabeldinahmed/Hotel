
from setting.views import home, home_search ,category_searh
from django.urls import path


app_name='setting'

urlpatterns = [
    path('', home ,name='home'),
    path('search/', home_search ,name='home_search'),
    path('category/<slug:category>', category_searh ,name='category_searh'),
]
