from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('map:map')
    if request.method == 'GET':
        return render(request, 'login/index.html')
    if request.method == 'POST':
        data = request.POST
        username = data.get('Username')
        password = data.get('Password')
        if username == "" or password == "":
            print 'error'
            # error
        else:
            user = auth.authenticate(username=username, password=password)
            print user
            if user is None:
                # A backend authenticated the credentials
                print 'error no user'
            elif not user.has_perm('gettrafficlights.is_driver'):
                print 'not driver'
            else:
                auth.login(request, user)
                return redirect('map:map')

    return render(request, 'login/index.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login:login')