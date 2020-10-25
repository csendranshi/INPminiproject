from django.db import connection
from django.shortcuts import render


# Create your views here.

# Create your views here.
def article_view(request, grid_category, section, unique_id):
    print("This is the ", unique_id, grid_category, section)
    with connection.cursor() as cursor:
        cursor.execute('CALL news_database.get_the_row_with_respective_grid_section(%s,%s,%s)',
                       [grid_category, unique_id, section])
        row = cursor.fetchone()
        print(row)
        article_dict = {
            'title': row[1],
            'image': row[2],
            'image_link': row[3],
            'content': row[4],
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
            'suscriber_access': request.session['suscriber_priority']

        }
        context_of_top_stories = {'user': dict_of_user_details, 'article_dictionary': article_dict}
        return render(request, "article.html", context_of_top_stories)
    context = {'article_dictionary': article_dict}
    return render(request, "article.html", context)
