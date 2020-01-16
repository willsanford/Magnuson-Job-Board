from django import forms
from .models import Job,Company

HIRE_TYPES = [
        ('F', 'Full Time'),
        ('P','Part Time'),
        ('I', 'Intern'),
    ]

class CompanyCreationForm(forms.Form):

    title = forms.CharField(label='Comapny Title', 
                            max_length=100, 
                            required=True)
    description = forms.CharField(label='Add a brief description of the company for potential applicants to view',
                                  widget=forms.Textarea,
                                  required=True)


class JobCreationForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), 
                                    empty_label="Choose the name of the related company")
    title = forms.CharField(max_length=100,
                            label='Position title')
    date_due = forms.DateField(label='Application Due Date',
                               required=False,
                               widget=forms.SelectDateWidget)
    hire_type = forms.ChoiceField(choices=HIRE_TYPES,
                                  label='Enter the hire category') 
    key_qualifications = forms.CharField(label='Enter the key qualifications you are looking for in a canidate',
                                         widget=forms.Textarea)
    additional_comments = forms.CharField(label='Enter a description of the position or any other comments you might have',
                                          widget=forms.Textarea)
    job_location = forms.CharField(label='Enter the location of this position',
                                    max_length=500)
    contact_info = forms.CharField(label='Enter the contact info a potential applicant should use',
                                   widget=forms.Textarea)
    application_link = forms.CharField(label='Enter any links a potential applicant could use to access this job offer or the company site',
                                       max_length=1000)

