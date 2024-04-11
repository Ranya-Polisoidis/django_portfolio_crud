from .models import *
from django_seed import Seed

def run_skills():

    seeder = Seed.seeder()

    data = [
        {
            "langages" : "HTML",
            "percentage" : 100,
        },
        {
            "langages" : "CSS",
            "percentage" : 90,
        },
        {
            "langages" : "JavaScript",
            "percentage" : 75,
        },
        {
            "langages" : "PHP",
            "percentage" : 80,
        },
        {
            "langages" : "WordPress/CMS",
            "percentage" : 90,
        },
        {
            "langages" : "Photoshop",
            "percentage" : 55,
        }
    ]
    
    for item in data:
        seeder.add_entity(Skills,1,item)

    seeder.execute()
    print('Généré avec succès')