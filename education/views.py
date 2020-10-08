from django.shortcuts import render


# Create your views here.
def education_view(request, *args, **kwargs):
    return render(request, "Education.html", {})
