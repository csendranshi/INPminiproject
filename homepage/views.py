from django.shortcuts import render
import requests


# Create your views here.
def home_view(request, *args, **kwargs):
    top_stories = "https://newsapi.org/v2/top-headlines?country=in&apiKey=95c4ed43f7644dc8a05175665cd04b7a"
    # 95c4ed43f7644dc8a05175665cd04b7a - api key
    r = requests.get(top_stories).json()
    top = []
    for i in r['articles']:
        top_story = {
            'image': i['urlToImage'],
            'title': i['title'],
            'content': i['content']
        }
        top.append(top_story)
    context_of_top_stories = {'top_stories': top}
    return render(request, "index.html", context_of_top_stories)
