from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        user_name = request.POST['u_name']
        email = request.POST['email']
        password = request.POST['pwd']
        confirm_password = request.POST['confirm_pwd']

        if password==confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exits')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exits')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User Created')
                return redirect('login')
        else:
            messages.error(request, 'Password not matching')
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['u_name']
        password = request.POST['pwd']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login Successful')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')