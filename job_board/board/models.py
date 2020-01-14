from django.db import models



class Company(models.Model):
    title = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_title")
    date_due = models.CharField(max_length=30)
    content = models.TextField()
    location = models.TextField()
    link = models.TextField()



    def __str__(self):
        return self.title + " - " + self.company.__str__()

