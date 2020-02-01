from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User


from django.contrib.auth.models import User
from .models import Profile
from staff.models import Job,Company

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid(): 
            form.save()

            user = User.objects.filter(username=form.cleaned_data['username']).first()
            if user is not None:
                login(request,user)

            # the password hash will be convrted into a valid url for continuity
            sent = send_mail(
                    'Subject here',
                    'Please log in usign the below link. Thank you! \n\n ' + 'http://localhost:8000/' + 'users/verifyAccount/'  + str(user.id),
                    form.cleaned_data['email'],
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )
            if sent == 1:
                messages.success(request, " A vlidation email was sent to your email. Please use the link in this email to validate your account")
            else:
                messages.warning(request, "Oops! For some reason the email you entered could be used. Please contact a staff member")

            messages.success(request, "Created successfully!!")
            return redirect('board-home')
        else:
            messages.warning(request, "This seems to be an invalid form. Please try again")
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

# checks the slug from the email againt the this users hashed password 
def verifyAccount(request, id):
    user = User.objects.filter(id=id).first()
    if user is not None:
        verified_users = Group.objects.get(name='verified') 
        verified_users.user_set.add(user)
        messages.success(request, "Congrats! Your account has been verified. Please enjoy!")
        return redirect('board-home')
    
    messages.warning(request, "There was an issue verifing your account. Please try again. If this does not work, try contacting a staff member at the Magnuson Center")
    return redirect('staff-verified')
