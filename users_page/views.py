from django.shortcuts import render
from django.db import connection
import json
import time


def users_view(request, *args, **kwargs):
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

        with connection.cursor() as cursor:
            cursor.execute(
                'Select first_name,last_name,admin_priority,journalist_priority,suscriber_priority,profile_picture from news_database.personal_details;')
            rows = cursor.fetchall()
            list_of_users = []
            for row in rows:
                dict_of_user = {
                    'first_name': row[0],
                    'admin': row[2],
                    'suscriber': row[4],
                    'journalist': row[3],

                    'last_name': row[1],
                    'pro_pic': row[5]
                }
                list_of_users.append(dict_of_user)
                with open('users_page_json.json', 'w') as outfile:
                    json.dump(dict_of_user, outfile)

            with open('users_page_json.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)


            print(list_of_users)
            print("latest-cell-1")

        context_of_top_stories = {'user': dict_of_user_details, 'user_details': json_object}
        return render(request, "users_page.html", context_of_top_stories)

    return render(request, "users_page.html", {})
