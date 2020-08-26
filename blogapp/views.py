from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blogapp/index.html'
    context_object_name = 'posting'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'
    context_object_name = 'details'
