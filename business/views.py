from django.shortcuts import render
from django.db import connection, Error

# Create your views here.
def business_view(request, *args, **kwargs):
    list_of_business = []
    with connection.cursor() as cursor:
        try:
            cursor.execute('SELECT * from business_grid')
            rows = cursor.fetchall()


            for row in rows:
                business_dict = {
                    'section': row[0],
                    'title': row[1],
                    'image': row[2],
                    'image_link': row[3],
                    'category':row[6],
                    'news_unique_id':row[8]
                }
                list_of_business.append(business_dict)
            print(list_of_business)
        except Error as err:
            return render(request, "ErrorPage.html", {"Error": err})
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
        context_of_top_stories = {'user': dict_of_user_details,'business_stories': list_of_business}
        return render(request, "Business.html", context_of_top_stories)
    context = {'business_stories': list_of_business}
    return render(request, "Business.html", context)
