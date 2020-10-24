from django.shortcuts import render, redirect
import requests
from django.db import connection
import random

def cell_list(prefix, get_range):
    list_cell_string = []
    for i in get_range:
        cell_string = prefix + "-cell-"
        cell_string += str(i)
        list_cell_string.append(cell_string)
    return list_cell_string


def posts_view(request, *args, **kwargs):
    latest_cell = cell_list('latest', range(1, 15))
    health_cell = cell_list('health', range(1, 10))
    world_cell = cell_list('world', range(1, 11))
    business_cell = cell_list('business', range(1, 9))
    tech_cell= cell_list('technology',range(1,11))
    edu_cell = cell_list('education', range(1, 9))
    india_cell = cell_list('india', range(1, 11))
    dictionary_of_section_as_per_category = {
        'latest': latest_cell,
        'health': health_cell,
        'world': world_cell,
        'business': business_cell,
        'technology':tech_cell,
        'education':edu_cell,
        'india':india_cell
    }

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

            n = random.randint(10000, 999999)
            f = open("unique_id.txt", "a")
            f.write(str(n) + "\n")
            f.close()
            with connection.cursor() as cursor:
                print(article_image_link,
                      article_title,
                      article_category,
                      article_section,
                      article_content)
                cursor.execute('CALL news_database.latest_top_stories(%s,%s,%s,%s,%s,%s,%s,%s)',
                               [article_title, article_file_picture, article_image_link, article_content,
                                dict_of_user_details['email_id'], article_category,article_section,n])
                print("clean")
        context_of_top_stories = {'user': dict_of_user_details, 'cell_list': dictionary_of_section_as_per_category}
        return render(request, 'posts.html', context_of_top_stories)
    context = {'cell_list': dictionary_of_section_as_per_category}
    return render(request, 'posts.html', context)
