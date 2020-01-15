from django import forms
from .models import Job,Company

HIRE_TYPES = [
        ('F', 'Full Time'),
        ('P','Part Time'),
        ('I', 'Intern'),
    ]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'title',
            'password',
        ]


class CompanyCreationForm(forms.Form):

    title = forms.CharField(label='Comapny Title', 
                            max_length=100, 
                            required=True)
    description = forms.CharField(label='Add a brief description of your company for potential applicants to view',
                                  widget=forms.Textarea,
                                  required=True)
    password1 = forms.CharField(label='Company Password', 
                                max_length=100,
                                required=True)
    password2 = forms.CharField(label='Re-enter Company Password', 
                                max_length=100,
                                required=True)


