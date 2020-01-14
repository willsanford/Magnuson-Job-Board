# This is where we can create the custom search results form our data base
# in the future we can add parameters to the create jobs list function that cn curate the search
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .models import Job, Company

#creates a dummy company/job
def create_dummy():
    
    company1 = Company(
        title = "Company Title"
    )
    company1.save()

    job1 = Job(
        company = company1,
        title = "Architect",
        date_due = "March 20, 2021",
        content = "Alot of planning and writing and whatnot",
        link = "https://google.com",
        location = "New York"
    )
    job1.save()

    job2 = Job(
        company = company1,
        title = "IB Banking",
        date_due = "March 20, 2021",
        content = "The most Slithery little snakes",
        link = "https://google.com",
        location = "San Francisco"
    )
    job2.save()


    job3 = Job(
        company = company1,
        title = "Lab Technitian",
        date_due = "March 20, 2021",
        content = "Either incredibly interesting or incredibly dull. Depends on the day. I guess thats most jobs though",
        link = "https://google.com",
        location = "Boston"
    )
    job3.save()

#simple helper method to generate Q objects
def query_gen(term):
    return Q(title__icontains=term) | Q(content__icontains=term)


# Initial job creating function
def create_job_list(search_term, search_location):

    if search_term == None:
        return Job.objects.all()
    
    if search_location == None:
        q_filter_loc = Q(location__icontains="")
    else:
        q_filter_loc = Q(location__icontains=search_location)
    
    # we can create a list of keywords to loop our query over

    # TODO : if you query " " this crashes. Fix this. Just need something to start the OR chaining
    q_list = search_term.split()

    q_filter_key = query_gen(q_list[0])

    for q_word in q_list:
        q_filter_key = q_filter_key | query_gen(q_word)

    # we can then filter through the AND of the location and keyword query objects
    return Job.objects.filter( q_filter_key & q_filter_loc )




    # if search_term == None:
    #     job_list = Job.objects.all()
    # else:
    #     job_list = Job.objects.filter(
    #         Q(title__icontains=search_term) | 
    #         Q(content__icontains=search_term)
    #     )
    # return job_list
    