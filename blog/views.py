from django.db.models import Count
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic import DetailView ,ListView
# Create your views here.
from.models import Post ,Category
from taggit.models import Tag


class PostList(ListView):
   model =Post
   paginate_by =1

   def get_queryset(self):
       name= self.request.GET.get('q','')
       object_list=Post.objects.filter(
         Q(title__icontains= name ) |
         Q(description__icontains= name ) 

       )   
       return object_list

class PostDetail(DetailView ):
    model =Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categries"] = Category.objects.all().annotate(post_count=Count('Post_category'))
        context["tags"] =Tag.objects.all()
        context["recent_post"]=Post.objects.all()[:3]
        return context



class PostsByCategory (ListView):
   model =Post

   def get_queryset(self):
       slug =self.kwargs['slug']
       object_list=Post.objects.filter(
         Q(category__name__icontains=slug)
       )   
       return object_list
        


class PostsByTags (ListView):
   model =Post

   def get_queryset(self):
       slug =self.kwargs['slug']
       object_list=Post.objects.filter(
         Q(tags__name__icontains=slug)
       )   
       return object_list