from django.shortcuts import render

# Create your views here.
def Technology_view(request, *args, **kwargs):
    return render(request, "technology.html", {})

