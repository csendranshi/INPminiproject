from django.shortcuts import render
from django.db import connection, Error
import requests


# Create your views here.
def education_view(request, *args, **kwargs):
    with connection.cursor() as cursor:
        try:
            cursor.execute('SELECT * from education_grid')
            rows = cursor.fetchall()

            list_of_education = []
            for row in rows:
                education_dict = {
                    'section': row[0],
                    'title': row[1],
                    'image': row[2],
                    'image_link': row[3],
                    'category': row[6],
                    'news_unique_id': row[8]
                }
                list_of_education.append(education_dict)
        except Error as err:
            return render(request, "ErrorPage.html", {"Error": err})
        # print(list_of_education)

    if request.session.has_key('logged_in'):
        # print(request.session.has_key('logged_in'))
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
        context_of_top_stories = {'user': dict_of_user_details, 'education_stories': list_of_education}
        return render(request, "Education.html", context_of_top_stories)
    context = {'education_stories': list_of_education}
    return render(request, "Education.html", context)
