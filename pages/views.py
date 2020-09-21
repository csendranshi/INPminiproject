from django.shortcuts import render


# Create your views here.

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "index.html", {})
