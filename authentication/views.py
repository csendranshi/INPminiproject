from django.shortcuts import render, redirect

# Create your views here.
from authentication.form import PersonalDetails


# Create your views here.
def auth(request):
    Registerform = PersonalDetails()
    if request.method == 'POST':
        form = PersonalDetails(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form": Registerform}
    return render(request, 'authentication.html', context)
