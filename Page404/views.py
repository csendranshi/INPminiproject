from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
def handler404(request, *args, **argv):
    return render(request, "ErrorPage.html")


def handler500(request, *args, **argv):
    return render(request, "ErrorPage.html")
