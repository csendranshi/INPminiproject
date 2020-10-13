from django.shortcuts import render
import requests
# Create your views here.
def posts_view(request, *args, **kwargs):
    return render(request, "posts.html", {})