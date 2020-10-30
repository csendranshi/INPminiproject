from django.shortcuts import render
from django.db import connection
import time

# Create your views here.
def profile_view(request, *args, **kwargs):
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
            password1 = request.POST.get('pass1')
            password2 = request.POST.get('pass2')
            profile_picture = request.POST.get('image-data')
            print(password1, password2, profile_picture)
            if profile_picture != None and profile_picture != '':
                with connection.cursor() as cursor:
                    cursor.execute('CALL news_database.update_profile_picture(%s,%s)',
                                   [dict_of_user_details['email_id'], profile_picture])
                    time.sleep(2)
                print("Successfully Clear")
            if password1 == password2:
                print(password1, password2, profile_picture)

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM personal_details WHERE email_id=%s",
                           [dict_of_user_details['email_id']])
            row = cursor.fetchone()

            profile_details = {
                'first_name': request.session['first_name'],
                'last_name': request.session['last_name'],
                'email_id': request.session['email_id'],
                'journal_access': request.session['journal_access'],
                'suscriber_access': request.session['suscriber_priority'],
                'gender': row[9],
                'phone_no': row[10],
                'profile_picture': row[12]
            }
            email_id = profile_details['email_id']
            print("This", profile_details['profile_picture'])

        context_of_top_stories = {'user': dict_of_user_details, 'profile_details': profile_details}
        return render(request, "profile.html", context_of_top_stories)

    return render(request, "profile.html", {})
