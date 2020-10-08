from django.shortcuts import render, redirect

# Create your views here.
from authentication.form import PersonalDetails


# Create your views here.
def auth(response):
    Registerform = PersonalDetails()
    if response.method == 'POST':
        form = PersonalDetails(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form": Registerform}
    return render(response, 'authentication.html', context)
