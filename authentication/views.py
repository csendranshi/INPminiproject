from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
# Create your views here.
from authentication.form import PersonalDetails
from django.contrib.auth.models import auth
from django.db import connection


# Create your views here.
# def my_custom_sql(self):


def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username != "" and password != "":
        print(username, password)
        with connection.cursor() as cursor:
            cursor.execute("SELECT email_id,password FROM authentication_personaldetails WHERE email_id = %s",
                           [username])
            row = cursor.fetchone()
            print(row)
    # else:
    Registerform = PersonalDetails()
    if request.method == 'POST':

        form = PersonalDetails(request.POST)
        if form.is_valid():
            form.save()
        redirect('auth/')

    context = {"form": Registerform}
    return render(request, 'authentication.html', context)
