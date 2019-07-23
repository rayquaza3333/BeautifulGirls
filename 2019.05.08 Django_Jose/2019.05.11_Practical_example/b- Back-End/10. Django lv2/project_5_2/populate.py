import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','app_5_2.settings')

import django
django.setup()

import random
from faker import Faker
from app_5_2.models import AccessRecord, Topic, Webpage

fakegen = Faker()

topics= ['Social Media','Drop Shipping','E-Commerce','News','Entertainment']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    return t

def populate(N = 5):

    for acc in range(N):

    t = add_topic()


    fake_name = fakegen.name()
    fake_date = fakegen.date()
    fake_url = fakegen.url()

    webpg = Webpage.objects.get_or_create(topic = t, name = fake_name, url = fake_url)
    access = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)

    print(f'Generating pop number {acc+1}')

if __name__ ='__main__':
    print('Generating population')
    populate(20)
    print('Generating population completed')
