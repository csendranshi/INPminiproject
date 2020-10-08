from django.shortcuts import render

# Create your views here.

def world_view(request, *args, **kwargs):
    return render(request, "World.html", {})
