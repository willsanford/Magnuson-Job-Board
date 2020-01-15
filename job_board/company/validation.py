from .forms import CompanyCreationForm
from .models import Company, Job
from django.contrib import messages


# TODO : find a hash function that we can use here
def hash_funciton(input):
    return input



# This function validates a company that is trying to apply to a part of our website
# This funciton will rin through the fields on the from to validate. It will slowly build
# messages on the request object if need be, and then return a boolean delcaring if the company
# was successfully added to our system
def CompanyCreationValidation(request, form):
    valid = True          

    password1 = form.cleaned_data['password1']
    password2 = form.cleaned_data['password2']
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']

    # initial password check to see if the passwords match
    if password1 != password2:
        valid = False
        messages.warning(request, "Passwords do not match. Please try retyping them")
    
    # Check to see if this compnay has already been added to the site
    if Company.objects.filter(title=title).exists():
        valid = False
        messages.warning(request, "It seems like this company name already exists in our database. Maybe you have signed up before?")




    # if the conpmany application is valid, then we can create a new compnay 
    # object. This is where we store the hash of the password and not the plain text            
    if valid:
        c = Company(
            title = title,
            description = description,
            password = hash_funciton(password1)
        )
        c.save()
    
    return valid



