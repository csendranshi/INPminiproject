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
    print(row)
    for i in row:
        top_story = {
            'id':i[8],
            'title': i[1],
            'image':i[2],
            'image_link': i[3],
            'section': i[7],
            'category': i[6],
            'news_unique_id': i[8]
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
            'suscriber_access': request.session['suscriber_priority'],
            'profile_picture':request.session['profile_picture']

        }
        context_of_top_stories = {'top_stories': top, 'user': dict_of_user_details}
        return render(request, "index.html", context_of_top_stories)
    context_of_top_stories = {'top_stories': top}
    return render(request, "index.html", context_of_top_stories)


def Latest_view(request, *args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * from latest_grid')
        rows = cursor.fetchall()

        list_of_latest = []
        for row in rows:
            latest_dict = {
                'section': row[0],
                'title': row[1],
                'image': row[2],
                'image_link': row[3],
                'category':row[6],
                'news_unique_id':row[8]
            }
            list_of_latest.append(latest_dict)
        print(list_of_latest)
    if request.session.has_key('logged_in'):
        print(request.session.has_key('logged_in'))
        dict_of_user_details = {
            'admin_access': request.session['admin_access'],
            'journal_access': request.session['journal_access'],
            'logged_in': request.session['logged_in'],
            'first_name': request.session['first_name'],
            'last_name': request.session['last_name'],
            'email_id': request.session['email_id'],
            'suscriber_access': request.session['suscriber_priority'],
            'profile_picture': request.session['profile_picture']

        }
        context_of_top_stories = {'user': dict_of_user_details, 'latest_stories': list_of_latest}
        return render(request, "index.html", context_of_top_stories)
    context = {'latest_stories': list_of_latest}
    return render(request, "index.html", context)