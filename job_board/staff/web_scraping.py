import bs4
from .models import Job, Company

# In this module we will use Beautiful Soup to do some web scraping on specific companies career 
# boards to generate Job and Company objects. Each company will need its own function and will use 

# TODO : we will eventually want this in some other file like a json or csv file so it can be easily modified
#        by outsides so we can also make sure the imput is valid and out whole function is not broken
# is the use_terms variable is false then we will just find all jobs
use_terms = False
search_terms = [
    'Software Developer',
    'Engineer',
]

# This function scrapes the norwest Job board at 'http://careers.nvp.com/'. Each job is under a div
# with a 'careers-item' class. This is where we begin the search

def NorWestScrape():
    link = 'http://careers.nvp.com/'

    # Get the beautiful soup request
    page = requests.get(link).content
    soup = bs4.BeautifulSoup(page, 'html.parser')

    # The first item with this class is the headers, so we remove this
    jobs = soup.find_all("div", class_='careers-item')[1:]

    for job in jobs:
        # This pulls apart the contents of the entire div
        job_contents = job.get_text('|', strip=True).split('|')
        job_link = link + job.contents[0]('a')[0]['href']

        company = job_contents[0]
        title = job_contents[1]
        location = job_contents[2]

        # first we will check to see if this company already exists in our database
        # If it is not we can add it
        if not Company.objects.filter(title=company).exists():
            c = Company(title=company, decsription='We have no description for this company yet.')
            c.save()
        new_job = Job(company=Company.objects.filter(title=company).first()
                      title=title,
                      location=location)
        new_job.save()


