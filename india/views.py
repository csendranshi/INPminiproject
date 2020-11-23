from django.db import connection
from django.shortcuts import render



# Create your views here.
def india_view(request, *args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * from india_grid')
        rows = cursor.fetchall()

        list_of_india = []
        for row in rows:
            india_dict = {
                'section': row[0],
                'title': row[1],
                'image': row[2],
                'image_link': row[3],
                'category': row[6],
                'news_unique_id': row[8]
            }
            list_of_india.append(india_dict)
        # print(list_of_india)
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
        context_of_top_stories = {'user': dict_of_user_details, 'india_stories': list_of_india}
        return render(request, "India.html", context_of_top_stories)
    context = {'india_stories': list_of_india}
    return render(request, "India.html", context)
