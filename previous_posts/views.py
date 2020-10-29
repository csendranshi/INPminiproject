from django.db import connection
from django.shortcuts import render


# Create your views here.
def prevpost_view(request, *args, **kwargs):
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
        with connection.cursor() as cursor:
            cursor.execute('CALL news_database.get_the_previous_posts_of_user(%s)', [dict_of_user_details['email_id']])
            rows = cursor.fetchall()
        list_of_prev_posts = []
        for post in rows:
            prev_posts = {
                'actual_category':post[2],
                'category': post[2].split('-')[0],
                'title': post[1],
                'news_unique_id': post[0],
                'time_of_post': post[3],
                'section': post[4]
            }
            list_of_prev_posts.append(prev_posts)

        context_of_top_stories = {'user': dict_of_user_details, 'prev_post': list_of_prev_posts}
        return render(request, "prevpost.html", context_of_top_stories)
    return render(request, "prevpost.html", {})
