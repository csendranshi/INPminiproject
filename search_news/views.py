import time

from django.db import connection
from django.shortcuts import render


# Create your views here.
def search_view(request, *args, **kwargs):
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
        if request.method == 'POST':
            search_text = request.POST.get('search_text')
            print("The Search Text Entered is: ", search_text)
            with connection.cursor() as cursor:
                cursor.execute('CALL news_database.search_news(%s)',
                               [search_text])
                rows = cursor.fetchall()
                print(rows)
                if rows == ():
                    context_of_top_stories = {'user': dict_of_user_details,
                                              'error_message': True}
                    return render(request, "search.html", context_of_top_stories)
                list_of_stories = []
                for row in rows:
                    stories_dict = {
                        'section': row[4],
                        'title': row[5],
                        'image': row[1],
                        'image_link': row[2],
                        'category': row[3],
                        'news_unique_id': row[0]
                    }
                    list_of_stories.append(stories_dict)

            context_of_top_stories = {'user': dict_of_user_details, 'search_stories': list_of_stories,
                                      'show_search_svg': False}
            return render(request, "search.html", context_of_top_stories)
        return render(request, "search.html", {'show_search_svg': True, 'user': dict_of_user_details})
