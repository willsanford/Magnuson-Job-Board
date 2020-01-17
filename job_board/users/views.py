from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from django.contrib.auth.models import User
from .models import Profile
from staff.models import Job,Company

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


@login_required(redirect_field_name='login', login_url='/login/')
def logout_request(request):
    logout(request)

    return redirect('login')

@login_required(redirect_field_name='login', login_url='/login/')
def profile(request, username):
    user = User.objects.filter(username=username).first()
    #deals with the action of users saving jobs
    save_button = request.GET.get('save_button')
    if save_button:
        #We can add or remove this job to the saved list of the viewer
        job_id = request.GET.get('job_id')
        job = Job.objects.filter(id=job_id).first()
        user.profile.savedJobs.remove(job)


    
    context = {
        'name' : username,
        'jobs' : user.profile.savedJobs.all()
    }

    return render(request, 'users/profile.html', context)