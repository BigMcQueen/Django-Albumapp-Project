from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import Chat
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('listview')
        except IntegrityError:
            return render(request, 'chat/signup.html', {'context': 'このユーザー名はすでに登録されています！'})
    else:
        return render(request, 'chat/signup.html', {'context': 'GET method'})
    
def signin_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'chat/signin.html', {'context': 'サインインできませんでした'})
    else:
        return render(request, 'chat/signin.html', {'context': 'GET method'})

@login_required
def listview_func(request):
    object_list = Chat.objects.all()
    return render(request, 'chat/listview.html', {'object_list': object_list})