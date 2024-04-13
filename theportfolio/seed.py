from .models import *
from django_seed import Seed

def run_theportfolio():

    seeder = Seed.seeder()

    data = [
        {
            "image" : "images/portfolio-1.jpg",
            "title" : "4k",
            "filter": "filter-app",
        },
        {
            "image" : "images/portfolio-2.jpg",
            "title" : "Your brand serum",
            "filter": "filter-web",
        },
        {
            "image" : "images/portfolio-3.jpg",
            "title" : "Tube mockup",
            "filter": "filter-app",
        },
        {
            "image" : "images/portfolio-4.jpg",
            "title" : "Cactus",
            "filter": "filter-card",
        },
        {
            "image" : "images/portfolio-5.jpg",
            "title" : "Aerin",
            "filter": "filter-web",
        },
        {
            "image" : "images/portfolio-6.jpg",
            "title" : "Cocooil",
            "filter": "filter-app",
        },
        {
            "image" : "images/portfolio-7.jpg",
            "title" : "Acqua Panna",
            "filter": "filter-card",
        },
        {
            "image" : "images/portfolio-8.jpg",
            "title" : "Furniture",
            "filter": "filter-card",
        },
        {
            "image" : "images/portfolio-9.jpg",
            "title" : "Meal",
            "filter": "filter-web",
        },

    ]
    
    for item in data:
        seeder.add_entity(Theportfolio,1,item)

    seeder.execute()
    print('Généré avec succès')