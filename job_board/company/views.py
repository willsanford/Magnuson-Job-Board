from django.shortcuts import render, redirect
from .forms import CompanyCreationForm
from .validation import CompanyCreationValidation
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'company/home.html')

def signUp(request):

    if request.method == 'POST':
        completed_form = CompanyCreationForm(request.POST)
        
        
        if completed_form.is_valid():
            valid = CompanyCreationValidation(request, completed_form)
            if valid:
                messages.success(request, "Congratulations. Your company has been added to our database. Try adding a job!")
                return redirect('company-add')
            else:
                context = {
                    'form': completed_form
                }
                return render(request, 'company/signUp.html', context)
        else:
            messages.warning(request, "This form was detected as invalid. This can happen if you inputs are too long. Look over your entries and try again")
            context = {
                'form': completed_form
            }
            return render(request, 'company/signUp.html', context)
    else:
        form = CompanyCreationForm()
        context = {
            'form': form
        }
        return render(request, 'company/signUp.html', context)

def add(request):
    return render(request, 'company/add.html')
