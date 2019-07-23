import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_4.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from app_4.models import Topic, Webpage, AccessReCord
from faker import Faker

fakegen = Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        #get the topuc for the entry

        top = add_topic()
        # create the fake data for the entry

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry

        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]

        # creata a fake access record for that Webpag

        acc_rec = AccessReCord.objects.get_or_create(name = webpg, date = fake_date)[0]

        print(f'Population No.{entry +1} completed')


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('population completed!')
