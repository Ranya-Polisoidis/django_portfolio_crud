from .models import *
from django_seed import Seed

def run_homebackground():

    seeder = Seed.seeder()
    
    data = [
        {
            'image': 'images/homebackground.jpg',
        },
    ]

    for item in data:
        seeder.add_entity(Homebackground,1,item)

    seeder.execute()
    print('Généré avec succès')
