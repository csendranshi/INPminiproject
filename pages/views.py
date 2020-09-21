from django.shortcuts import render


# Create your views here.

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def auth_view(request, *args, **kwargs):
    return render(request, "loginform.html", {})
