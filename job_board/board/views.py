from django.shortcuts import render
from django.core.paginator import Paginator
from .job_search import create_job_list
from .models import Job, Company



# This is a dud at this point doesnt really do anything that I want it to. This was a prototype of search before we made search a thing
# TODO : totally change this up
def home(request):

    # TODO : We want this term to come from the request eventaully
    q_location = request.GET.get("q_location")
    q_keyword = request.GET.get("q_keyword")

    search_list = create_job_list(q_keyword, q_location)

    
    

    context = {
        'jobs' : search_list,
        'include_jumbo' : True,
        "search_keyword" : q_keyword,
        "search_location" : q_location,
        "num_results" : str(len(search_list))
    }


    return render(request, "board/home.html", context)

def search(request):


    #TODO : We want this term to come from the request eventaully
    q_location = request.GET.get("q_location")
    q_keyword = request.GET.get("q_keyword")

    search_list = create_job_list(q_keyword, q_location)

    context = {
        'jobs' : search_list,
        'include_jumbo' : True,
        "search_keyword" : q_keyword,
        "search_location" : q_location,
        "num_results" : str(len(search_list)),
    }
    return render(request, "board/search.html", context)



def about(request):
    return render(request, "board/about.html")
