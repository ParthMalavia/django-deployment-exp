import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

import  random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'SocialMedia', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    
    for _ in range(N):
        topic = add_topic()
        
        url = fakegen.url()
        date = fakegen.date()
        name = fakegen.company()
        
        webpage = Webpage.objects.get_or_create(topic = topic, url=url, name=name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpage, date=date)[0]


if __name__ == "__main__":
    print("Generating data ...")
    populate(30)
    print("Data generation completed.")

