from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template import RequestContext


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
            return render(request, 'login/index.html', {'error_message': 'Missing Username or Password'})
        else:
            user = auth.authenticate(username=username, password=password)
            if user is None:
                return render(request, 'login/index.html', {'error_message': 'Wrong Username or Password'})
            elif not user.has_perm('gettrafficlights.is_driver'):
                return render(request, 'login/index.html', {'error_message': "You don't have the required permissions"})
            else:
                auth.login(request, user)
                return redirect('map:map')

    return render(request, 'login/index.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login:login')