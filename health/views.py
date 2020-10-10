from django.shortcuts import render


# Create your views here.
def health_view(request, *args, **kwargs):
    return render(request, "health.html", {})

