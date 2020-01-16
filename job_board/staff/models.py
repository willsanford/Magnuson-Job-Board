from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    # Lists for objects with choices
    HIRE_TYPES = [
        ('F', 'Full Time'),
        ('P','Part Time'),
        ('I', 'Intern'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_title")
    date_due = models.DateField()
    
    hire_type = models.CharField(max_length=1, choices=HIRE_TYPES)

    key_qualifications = models.TextField()
    additional_comments = models.TextField()
    job_location = models.TextField()
    contact_info = models.TextField()
    application_link = models.TextField()



    def __str__(self):
        return self.title + " - " + self.company.__str__()

