from django.shortcuts import render


# Create your views here.
def health_view(request, *args, **kwargs):
    if request.session.has_key('logged_in'):
        print(request.session.has_key('logged_in'))
        dict_of_user_details = {
            'admin_access': request.session['admin_access'],
            'journal_access': request.session['journal_access'],
            'logged_in': request.session['logged_in'],
            'first_name': request.session['first_name'],
            'last_name': request.session['last_name']

        }
        context_of_top_stories = {'user': dict_of_user_details}
        return render(request, "health.html", context_of_top_stories)
    return render(request, "health.html", {})
