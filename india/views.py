from django.shortcuts import render

# Create your views here.
def india_view(request, *args, **kwargs):
    return render(request, "India.html", {})

