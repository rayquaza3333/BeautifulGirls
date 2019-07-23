# Tell django where our setting module exist. The reason for this maybe:
# This population folder is not a built-in folder of django Projects.
# So we have to tell Django about this foilder so that it can apply code from here.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_5.settings')

#setting up django environment
import django
django.setup()

#what does
import random
from app_5.models import Topic, AccessRecord, Webpage
from faker import Faker

fakegen = Faker()

topics= ['Search','Market place', 'E-commerce','Drop shipping','Food delivery','News']
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    return t

def populate(N=5):

    for pop in range(N):

        topic = add_topic()

        fake_name = fakegen.name()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create(topic = topic, name = fake_name, url = fake_url)[0]
        access = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]
        print(f'Populating pop number {pop +1}')


if __name__ == '__main__':
    populate(20)
