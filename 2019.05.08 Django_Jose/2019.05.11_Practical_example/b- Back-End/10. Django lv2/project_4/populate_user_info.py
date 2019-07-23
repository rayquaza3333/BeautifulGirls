import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_4.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from app_4.models import Users
from faker import Faker

fakegen = Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_user():
    fake_first_name= fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_email = fakegen.email()
    user = Users.objects.get_or_create(email= fake_email, first_name= fake_first_name, last_name= fake_last_name)[0]
    user.save()
    return user

def populate(N=5):

    for entry in range(N):
        #get the topic for the entry

        user = add_user()

        print(f'Population No.{entry +1} completed')


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('population completed!')
