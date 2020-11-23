from django.shortcuts import render, redirect
import requests
from django.db import connection
import random
import math


def cell_list(prefix, get_range):
    list_cell_string = []
    for i in get_range:
        cell_string = prefix + "-cell-"
        cell_string += str(i)
        list_cell_string.append(cell_string)
    return list_cell_string


def OTPgen():
    nums = '0123456789'
    otp = ""

    for i in range(8):
        otp += nums[math.floor(random.random() * 10)]
    return otp


def EditContent(string):
    new_string = string.replace("'", "\\'")
    # new_string = new_string.replace("\"", "\\\"")
    return new_string


def posts_view(request, *args, **kwargs):
    global dict_of_user_details
    latest_cell = cell_list('latest', range(1, 12))
    health_cell = cell_list('health', range(1, 10))
    world_cell = cell_list('world', range(1, 11))
    business_cell = cell_list('business', range(1, 9))
    tech_cell = cell_list('technology', range(1, 11))
    edu_cell = cell_list('education', range(1, 11))
    india_cell = cell_list('india', range(1, 11))
    dictionary_of_section_as_per_category = {
        'latest': latest_cell,
        'health': health_cell,
        'world': world_cell,
        'business': business_cell,
        'technology': tech_cell,
        'education': edu_cell,
        'india': india_cell
    }

    if request.session.has_key('logged_in'):
        print("SESSION AT POSTS VIEW", request.session.has_key('logged_in'))
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

        # print(binary,letter_binary)

        if request.method == 'POST':

            article_image_link = request.POST.get('imageLink')
            article_title = request.POST.get('postTitle')
            article_category = request.POST.get('category')
            article_section = request.POST.get('section')
            article_content = request.POST.get('postDesc')
            article_file_picture = request.POST.get('finalPictureValue')
            print("THis is", article_category)
            if article_category == '' or article_category is None:
                message = "Choose A Category"
                context = {"registration_success": False, 'cell_list': dictionary_of_section_as_per_category,
                           'message': message}
                return render(request, 'posts.html', context)
            if article_section == '' or article_section is None:
                message = "Choose A Category"
                context = {"registration_success": False, 'cell_list': dictionary_of_section_as_per_category,
                           'message': message}
                return render(request, 'posts.html', context)
            if article_image_link == '' and article_file_picture == '':
                message = "Enter Image Link or Select An Image"
                context = {"registration_success": False, 'cell_list': dictionary_of_section_as_per_category,
                           'message': message}
                return render(request, 'posts.html', context)

            file1 = open('textfile.txt', 'a+')
            file1.seek(0)
            with connection.cursor() as cursor:
                while 1:
                    addotp = OTPgen()
                    file1.seek(0)
                    if addotp in file1.read():
                        print("exists", addotp)
                        continue
                    else:
                        file1.write(addotp + "\n")
                        # file1.write("\n")
                        if article_category.split('-')[0] == 'latest' and article_section == 'latest-cell-1':
                            cursor.execute('CALL news_database.latest_top_stories(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link,
                                            EditContent(article_content),
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-'), row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print("latest-cell-1")
                        elif article_category.split('-')[0] == 'latest':
                            cursor.execute('CALL news_database.update_latest_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link,
                                            EditContent(article_content),
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-'), row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print('latest')
                        elif article_category.split('-')[0] == 'india':
                            cursor.execute('CALL news_database.update_india_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link,
                                            EditContent(article_content),
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-'), row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print('india')
                        elif article_category.split('-')[0] == 'education':
                            print("Entering Education")
                            cursor.execute('CALL news_database.update_education_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link,
                                            EditContent(article_content),
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-'), row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print('education')
                        elif article_category.split('-')[0] == 'business':
                            cursor.execute('CALL news_database.update_business_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link,
                                            EditContent(article_content),
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-'), row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print('business')
                        elif article_category.split('-')[0] == 'world':
                            cursor.execute('CALL news_database.update_world_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link,
                                            EditContent(article_content),
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-'), row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print('world')
                        elif article_category.split('-')[0] == 'technology':
                            print("Entering Technology Cursor For Execution")
                            cursor.execute(
                                'CALL news_database.update_technology_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                [article_title, article_file_picture, article_image_link, article_content,
                                 dict_of_user_details['email_id'], article_category, article_section,
                                 addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-')[0], row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)

                            print('technology')
                        elif article_category.split('-')[0] == 'health':
                            cursor.execute('CALL news_database.update_health_grid(%s,%s,%s,%s,%s,%s,%s,%s)',
                                           [article_title, article_file_picture, article_image_link, article_content,
                                            dict_of_user_details['email_id'], article_category, article_section,
                                            addotp])
                            row = cursor.fetchone()
                            print(article_category.split('-')[0], row)
                            if row is not None:
                                context_of_top_stories = {"registration_success": False, "registration_failure": True,
                                                          'user': dict_of_user_details,
                                                          'cell_list': dictionary_of_section_as_per_category}
                                return render(request, 'posts.html', context_of_top_stories)
                            print('health')

                        else:
                            print("Un-Successfull")

                        context_of_top_stories = {"registration_success": True, 'user': dict_of_user_details,
                                                  'cell_list': dictionary_of_section_as_per_category}
                        return render(request, 'posts.html', context_of_top_stories)

            print(article_image_link,
                  article_title,
                  article_category,
                  article_section,
                  )

            print("clean")
        context_of_top_stories = {"registration_success": False, 'user': dict_of_user_details,
                                  'cell_list': dictionary_of_section_as_per_category}
        return render(request, 'posts.html', context_of_top_stories)
    context_of_top_stories = {"registration_success": False,
                              'cell_list': dictionary_of_section_as_per_category}
    return render(request, 'Login.html', context_of_top_stories)
