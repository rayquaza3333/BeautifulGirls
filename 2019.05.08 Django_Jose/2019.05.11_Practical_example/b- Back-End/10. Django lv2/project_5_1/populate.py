import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_5_1.settings')

import django
django.setup()

from app_5_1.models import AccessRecord, Topic, Webpage
from app_5_2.models import Users
from faker import Faker
import random

fakegen=Faker()

topics = ['E-Commerce','Drop Shipping','News','Entertainment']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    return t

def populate(N=5):

    for pop in range(N):

        topic=add_topic()

        fake_name = fakegen.name()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create(topic = topic, name = fake_name, url = fake_url)[0]
        access = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

        print(f'Generating item number {pop+1}')

def users_populate(N =5):

    for n in range(N):
            first_name = fakegen.first_name()
            last_name = fakegen.last_name()
            email = fakegen.email()

            user = Users.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)
            print(f'Generating user No.{n+1}')

if __name__ == '__main__' :
    print('Start generating fake date')
    users_populate(20)
    print('Generation completed')
