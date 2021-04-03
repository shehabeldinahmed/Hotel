from typing import Counter
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from  property.models import Category, Property,Place
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post

# Create your views here.
def home (request):
  category=Category.objects.all()    
  place =Place.objects.all().annotate(property_count=Count('property_place'))
  resturant_list=Property.objects.filter(category__name='Restaurant')[0:5]
  hotel_list=Property.objects.filter(category__name='Hotel')[0:5]
  places_list=Property.objects.filter(category__name='Places')[0:5]
  recent_post=Post.objects.all()[:4]

  user_count= User.objects.all().count()
  resturant_count=Property.objects.filter(category__name='Restaurant').count()
  hotel_count=Property.objects.filter(category__name='Hotel').count()
  places_count=Property.objects.filter(category__name='Places').count()
 


  context={'place':place,'category':category ,'resturant_list':resturant_list,
  'hotel_list':hotel_list,'places_list':places_list,'recent_post':recent_post,
  'user_count':user_count,'resturant_count':resturant_count,'hotel_count':hotel_count,
  'places_count':places_count,


  }
  return render(request,'settings/home.html',context)


def home_search(request):
      
  name =request.GET.get('name')
  place=request.GET.get('place')
  print(name ,place)
  property_list =Property.objects.filter(
      Q(name__icontains =name)&
      Q(place__name__icontains =place)
  )

  context={'property_list':property_list}
  return render (request , 'settings/home_search.html',context)


def category_searh(request ,category):
  category=Category.objects.get(name=category)
  property_list =Property.objects.filter(category=category
    
      
  )


  
  context={'property_list':property_list}    
  return render (request , 'settings/home_search.html',context)
     