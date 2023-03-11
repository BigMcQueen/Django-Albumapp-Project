from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'chat/signup.html', {'success': 'success'})
        except IntegrityError:
            return render(request, 'chat/signup.html', {'error': 'このユーザー名はすでに登録されています！'})
    else:
        return render(request, 'chat/signup.html', {'method': 'GET method'})