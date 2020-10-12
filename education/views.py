from django.shortcuts import render
import requests


# Create your views here.
def education_view(request, *args, **kwargs):
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
    if request.session.has_key('logged_in'):
        print(request.session.has_key('logged_in'))
        dict_of_user_details = {
            'admin_access': request.session['admin_access'],
            'journal_access': request.session['journal_access'],
            'logged_in': request.session['logged_in'],
            'first_name': request.session['first_name'],
            'last_name': request.session['last_name']

        }
        context_of_top_stories = {'top_stories': top, 'user': dict_of_user_details}
        return render(request, "Education.html", context_of_top_stories)
    context_of_top_stories = {'top_stories': top}
    return render(request, "Education.html", context_of_top_stories)
