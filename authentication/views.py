from django.shortcuts import render, redirect
from django.contrib import messages

from django.db import connection


# Create your views here.
# def my_custom_sql(self):
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
    if request.method == 'POST':
        if register_emailId != "" and register_firstname != "" and register_lastname != "" and register_password != "" and register_date != "":
            status = email_id_status(register_emailId)
            if status == 'EMAIL ID TAKEN':
                messages.info(request, "Email Id is Already Registered")
            else:
                with connection.cursor() as cursor:
                    print(register_firstname, register_lastname, register_emailId, register_password, register_date)
                    cursor.callproc('insert_personal_details',
                                    [register_firstname, register_lastname, register_emailId, register_password,
                                     register_date])
                    context = {"registration_success": True}
                    return render(request, 'login.html', context)

    return render(request, 'Register.html')


def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username != "" and password != "":
        with connection.cursor() as cursor:
            cursor.execute("SELECT email_id,password FROM authentication_personaldetails WHERE email_id = %s",
                           [username])
            row = cursor.fetchone()

            if row == None:
                print("Invalid Credentials")
    return render(request, 'Login.html')
