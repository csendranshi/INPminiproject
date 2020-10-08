from django.shortcuts import render

# Create your views here.
def business_view(request, *args, **kwargs):
    return render(request, "Business.html", {})


