from django.shortcuts import render, redirect
from .job_search import create_job_list
from staff.models import Job, Company
from django.contrib import messages
from django.contrib.auth.models import User  
from users.models import Profile  

# This is a dud at this point doesnt really do anything that I want it to. This was a prototype of search before we made search a thing
# TODO : totally change this up
def home(request):
        return render(request, 'board/home.html')

    
def search(request):

    #deals with the action of users saving jobs
    save_button = request.GET.get('save_button')
    if save_button:
        
        #We can add or remove this job to the saved list of the viewer
        job_id = request.GET.get('job_id')
        job = Job.objects.filter(id=job_id).first()
        if save_button == 'save':
            request.user.profile.savedJobs.add(job)
        else:   
            request.user.profile.savedJobs.remove(job)

    #genrates a list of saved jobs 
    saved_jobs = request.user.profile.savedJobs.all()[::1]

    q_location = request.GET.get("q_location")
    q_keyword = request.GET.get("q_keyword")

    #quick fix that deals with 'None' as a string as a keyword. Dont know where this comes from
    if q_keyword == 'None':
        q_keyword = None


    search_list = create_job_list(q_keyword, q_location)

    context = {
        'jobs' : search_list,
        'saved_jobs' : saved_jobs,
        'include_jumbo' : True,
        "search_keyword" : q_keyword,
        "search_location" : q_location,
        "num_results" : str(len(search_list)),
    }
    return render(request, "board/search.html", context)



def about(request):
    return render(request, "board/about.html")


def single_job(request, id):
    job = Job.objects.filter(id=id)
    if job.exists():
        context = {
            'job' : job.first()
        }
        return render(request, 'board/single_job.html', context)
    else:
        messages.warning(request,'It looks like there was some error in your search. Either this job does not exist anymore, or there is some error in our database. Please try again.')
        return redirect('board-home')
    context = {
        'ID' : id
    }
    

def single_company(request, id):
    company = Company.objects.filter(id=id)
    if company.exists():
        context = {
            'company' : company.first(),
            'jobs' : Job.objects.filter(company=company.first())
        }
        return render(request, 'board/single_company.html', context)
    else:
        messages.warning(request,'It looks like there was some error in your search. Either this company  does not exist anymore, or there is some error in our database. Please try again.')
        return redirect('board-home')