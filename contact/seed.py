from .models import *
from django_seed import Seed

def run_contact():

    seeder = Seed.seeder()
    
    data = [
        {
            'location': "Rue de l'Elpma 123 1000 Bruxelles Belgique",
            "email": "infodev@example.com",
            "call": "+32 2 123 45 67",
            "iframe": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12097.433213460943!2d-74.0062269!3d40.7101282!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb89d1fe6bc499443!2sDowntown+Conference+Center!5e0!3m2!1smk!2sbg!4v1539943755621",
        },
    ]

    for item in data:
        seeder.add_entity(Contact,1,item)

    seeder.execute()
    print('Généré avec succès')