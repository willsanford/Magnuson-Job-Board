from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'company/home.html')

def signUp(request):

    if request.method == 'POST':
        return render(request, 'company/signUp.html')
    else:
        return render(request, 'company/signUp.html')

def add(request):
    return render(request, 'company/add.html')
