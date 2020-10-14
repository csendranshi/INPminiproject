from django.shortcuts import render, redirect
import requests


# Create your views here.
def posts_view(request, *args, **kwargs):

        # return render(request, "posts.html", context_of_top_stories)
    return render(request, 'posts.html',{})
