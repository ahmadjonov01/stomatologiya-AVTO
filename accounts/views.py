from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def login_user(request):
    print(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ('SIZ RO`YHATDAN O`TMAGANSIZ'))
            return redirect('login_user')
    else:
        return render(request, 'pages/examples/login.html')
