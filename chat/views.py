from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'chat/signup.html', {'context': 'success'})
        except IntegrityError:
            return render(request, 'chat/signup.html', {'context': 'このユーザー名はすでに登録されています！'})
    else:
        return render(request, 'chat/signup.html', {'context': 'GET method'})
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'chat/signin.html', {'context': 'サインインしました'})
        else:
            return render(request, 'chat/signin.html', {'context': 'サインインできませんでした'})
    else:
        return render(request, 'chat/signin.html', {'context': 'GET method'})