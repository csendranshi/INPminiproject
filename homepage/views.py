from django.db import connection
from django.shortcuts import render
import requests


def boolean_function(s):
    return True if s == 1 else False


# Create your views here.
def home_view(request, *args, **kwargs):
    # top_stories = "https://newsapi.org/v2/top-headlines?country=in&apiKey=95c4ed43f7644dc8a05175665cd04b7a"
    # # 95c4ed43f7644dc8a05175665cd04b7a - api key
    # r = requests.get(top_stories).json()
    top = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM top_stories")
        row = cursor.fetchall()

    for i in row:
        top_story = {
            'id':i[0],
            'title': i[1],
            'image':i[2],
            'image_link': i[3]
        }
        top.append(top_story)
    if request.session.has_key('logged_in'):
        print(request.session.has_key('logged_in'))
        dict_of_user_details = {
            'admin_access': request.session['admin_access'],
            'journal_access': request.session['journal_access'],
            'logged_in': request.session['logged_in'],
            'first_name': request.session['first_name'],
            'last_name': request.session['last_name'],
            'email_id': request.session['email_id'],
            'suscriber_access': request.session['suscriber_priority']

        }
        context_of_top_stories = {'top_stories': top, 'user': dict_of_user_details}
        return render(request, "index.html", context_of_top_stories)
    context_of_top_stories = {'top_stories': top}
    return render(request, "index.html", context_of_top_stories)
