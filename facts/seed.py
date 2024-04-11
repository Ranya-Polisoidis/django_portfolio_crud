from .models import *
from django_seed import Seed

def run_facts():

    seeder = Seed.seeder()

    data = [
        {
            "client_count" : 232,
            "projects_count" : 521,
            "support_hours" : 1453,
            "workers_count" : 32
        },
    ]
    
    for item in data:
        seeder.add_entity(Facts,1,item)

    seeder.execute()
    print('Généré avec succès')