from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Created successfully!!")
            return redirect('board-home')
        else:
            messages.warning(request, "invalid form")
            return redirect('register')
    else :
        form = UserRegisterForm()
        context = {
            "form" : form
        }

        return render(request, 'users/register.html', context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Logged In')
                return redirect('board-home')
            else:
                messages.warning(request, "Either the username or password entered does not match our database. Please try again!")
                return redirect('login')
        else:
            messages.warning(request, "Either the username or password entered does not match our database. Please try again!")
            return redirect('login')


    else :
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'users/login.html', context)


def logout_request(request):
    logout(request)

    return redirect('login')
