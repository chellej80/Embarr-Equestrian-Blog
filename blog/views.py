from django.shortcuts import render

from django.views import generic
from .models import Post


#Pagination limit amount of posts that appear on the page
#Create view of listed posts 


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
