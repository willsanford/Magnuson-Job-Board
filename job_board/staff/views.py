from django.shortcuts import render, redirect
from .forms import CompanyCreationForm, JobCreationForm
from django.contrib import messages
from .models import Job, Company
from django.contrib.auth.decorators import user_passes_test


# This function is used in all staff views to check if the the user has the required staff permissions
def staff_perm(user):
    return user.groups.filter(name = 'admin' ).exists()


@user_passes_test(staff_perm, login_url='board-home')
def home(request):
    return render(request, 'staff/home.html')

@user_passes_test(staff_perm, login_url='board-home')
def addCompany(request):

    if request.method == 'POST':
        completed_form = CompanyCreationForm(request.POST)
        if completed_form.is_valid():
            addCompanyData(completed_form)
            messages.success(request, "Succsessfully added " + completed_form.cleaned_data['title'] + ' to the database')
            return redirect('staff-home')
        else:
            messages.warning(request, 'This input doesn\'t seen to be valid. Try again')
            return redirect('staff-add-company')
    else:
        form = CompanyCreationForm()
        context = {
            'form': form
        }
        return render(request, 'staff/addCompany.html', context)

@user_passes_test(staff_perm, login_url='board-home')
def addJob(request):

    if request.method == 'POST':
        completed_form = JobCreationForm(request.POST)
        if completed_form.is_valid():
            addJobData(completed_form)
            messages.success(request, "We have added the " + completed_form.cleaned_data['title'] + " from " +
                                        completed_form.cleaned_data['company'].title + " to the database.")
            return redirect('staff-home')
        else:
            messages.warning(request, 'This input doesn\'t seen to be valid. Try again')
            return redirect('staff-add-job')
    else:
        form = JobCreationForm()
        context = {
            'form' : form
        }
    return render(request, 'staff/addJob.html', context)

def addCompanyData(form):
    c = Company(title=form.cleaned_data['title'],
                description=form.cleaned_data['description'])
    c.save()

def addJobData(form):
    j = Job(title=form.cleaned_data['title'],
            company=form.cleaned_data['company'],
            date_due=form.cleaned_data['date_due'],
            hire_type=form.cleaned_data['hire_type'],
            key_qualifications=form.cleaned_data['key_qualifications'],
            additional_comments=form.cleaned_data['additional_comments'],
            job_location=form.cleaned_data['job_location'],
            contact_info=form.cleaned_data['contact_info'],
            application_link=form.cleaned_data['application_link'],)

    j.save()





