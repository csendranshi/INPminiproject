from django.shortcuts import render



# Create your views here.

# Create your views here.


def card_view(request, *args, **kwargs):
    return render(request, "newsCard.html", {})


def scroll_view(request, *args, **kwargs):
    return render(request, "top_stories.html", {})



