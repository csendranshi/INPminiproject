from django.shortcuts import render, redirect
from django.contrib import messages
from werkzeug.security import generate_password_hash, check_password_hash
from django.db import connection
from django.contrib.sessions.models import Session
from django.template import RequestContext


# Create your views here.
# def my_custom_sql(self):
def boolean_function(s):
    return True if s == 1 else False


def email_id_status(email_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL verify_email_id(%s,@level)", [email_id])
        cursor.execute("SELECT @level")
        row = cursor.fetchone()[0]
        return row


def auth(request):
    register_firstname = request.POST.get('reg_firstname')
    register_lastname = request.POST.get('reg_lastname')
    register_emailId = request.POST.get('reg_emailId')
    register_password = request.POST.get('reg_password')
    register_date = request.POST.get('dateofbirth')
    register_phone_no = request.POST.get('reg_phone_number')
    register_gender = request.POST.get('Gender')
    userdetails = {
        'firstname': register_firstname,
        'lastname': register_lastname,
        'emailId': register_emailId,
        'password': '',
        'date': register_date,
        'phone_no': register_phone_no,
    }
    if request.method == 'POST':
        if register_gender is None:
            return render(request, 'Register.html', {'message': 'Select A Gender', 'userdetails': userdetails})
        if register_emailId != "" and register_firstname != "" and register_lastname != "" and register_password != "" and register_date != "":
            hashed_password = generate_password_hash(register_password, method="sha256")
            print(register_firstname, register_lastname, register_emailId, hashed_password,
                  register_date, register_gender, register_phone_no)
            print(register_phone_no, register_gender)
            status = email_id_status(register_emailId)
            if status == 'EMAIL ID TAKEN':
                userdetails = {
                    'firstname': register_firstname,
                    'lastname': register_lastname,
                    'emailId': '',
                    'password': '',
                    'date': register_date,
                    'phone_no': register_phone_no,
                    'gender': register_gender
                }
                return render(request, 'Register.html',
                              {'message': 'Email Id Is Already Registered', 'userdetails': userdetails})
            else:
                # with connection.cursor() as cursor:
                #     print()
                #     cursor.execute('CALL news_database.insert_personal_details(%s,%s,%s,%s,%s,%s,%s)',
                #                    [register_firstname, register_lastname, register_emailId, hashed_password,
                #                     register_date, register_gender, register_phone_no])
                    context = {"registration_success": True}
                    return render(request, 'Login.html', context)

    return render(request, 'Register.html')


def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    if username != " " and password != " " and username != None and password != None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM personal_details WHERE email_id = %s",
                           [username])
            row = cursor.fetchone()
            print(row)
            userdetails = {
                'email': username,
                'status': 'Invalid Credentials'
            }
            if row is None:
                context = {"registration_success": False, "userdetails": userdetails}
                return render(request, 'Login.html', context)
            else:
                if check_password_hash(row[4], password):
                    messages.info(request, "Valid Credentials")
                    request.session['logged_in'] = True
                    request.session['journal_access'] = boolean_function(row[7])
                    request.session['admin_access'] = boolean_function(row[6])
                    request.session['suscriber_priority'] = boolean_function(row[8])
                    request.session['first_name'] = row[1]
                    request.session['last_name'] = row[2]
                    request.session['email_id'] = row[3]
                    request.session['profile_picture'] = row[12]
                    dict_of_user_details = {
                        'admin_access': request.session['admin_access'],
                        'journal_access': request.session['journal_access'],
                        'logged_in': request.session['logged_in'],
                        'first_name': request.session['first_name'],
                        'last_name': request.session['last_name'],
                        'email_id': request.session['email_id'],
                        'suscriber_access': request.session['suscriber_priority'],
                        'profile_picture':request.session['profile_picture']

                    }
                    print(dict_of_user_details)
                    context = {"registration_success": False, 'user': dict_of_user_details}
                    return redirect('/')
                else:
                    context = {"registration_success": False, "userdetails": userdetails}
                    return render(request, 'Login.html', context)
    return render(request, 'Login.html')


def Logout(request):
    request.session['logged_in'] = False
    request.session['journal_access'] = False
    request.session['admin_access'] = False
    request.session['suscriber_priority'] = False
    dict_of_user_details = {
        'admin_access': request.session['admin_access'],
        'journal_access': request.session['journal_access'],
        'logged_in': request.session['logged_in'],
        'first_name': "",
        'last_name': "",
        'suscriber_access': request.session['suscriber_priority']
    }
    context = {'user': dict_of_user_details}
    return render(request, 'Login.html', context)
