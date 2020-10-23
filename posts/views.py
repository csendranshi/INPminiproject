from django.shortcuts import render, redirect
import requests
from django.db import connection

def posts_view(request, *args, **kwargs):
    if request.session.has_key('logged_in'):
        dict_of_user_details = {
            'admin_access': request.session['admin_access'],
            'journal_access': request.session['journal_access'],
            'logged_in': request.session['logged_in'],
            'first_name': request.session['first_name'],
            'last_name': request.session['last_name'],
            'email_id': request.session['email_id'],
            'suscriber_access': request.session['suscriber_priority']
        }

        # print(binary,letter_binary)

        article_content = request.POST.get('postDesc')
        if request.method == 'POST':
            article_image_link = request.POST.get('imageLink')
            article_title = request.POST.get('postTitle')
            article_category = request.POST.get('category')
            article_section = request.POST.get('section')
            article_file_picture = request.POST.get('finalPictureValue')
            print(article_image_link,
                  article_title,
                  article_category,
                  article_section,
                  article_content)

            with connection.cursor() as cursor:
                print()
                cursor.execute('CALL news_database.latest_top_stories(%s,%s,%s,%s,%s,%s)',
                               [article_title, article_file_picture, article_image_link, article_content,
                                dict_of_user_details['email_id'], article_category])
                print("clean")
        context_of_top_stories = {'user': dict_of_user_details}
        return render(request, 'posts.html', context_of_top_stories)
    return render(request, 'posts.html', {})
