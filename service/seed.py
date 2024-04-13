from .models import *
from django_seed import Seed

def run_service():

    seeder = Seed.seeder()

    data = [
        {
            "title" : "My Services",
            "description" : "I offer a comprehensive range of services covering custom web development, performance optimization, data security, system integration, mobile app development, and technology consulting.",
            "class_css": "bi bi-briefcase" 
        },
        {
            "title" : "Proposed Tasks",
            "description" : "My work includes detailed analysis of client needs, development of customized solutions, implementation of advanced security measures, integration of third-party systems, creation of mobile applications, and strategic technology consultation.",
            "class_css": "bi bi-card-checklist" 
        },
        {
            "title" : "Evolution of My Work",
            "description" : "My professional approach is constantly evolving to incorporate the latest technological advancements, allowing me to provide increasingly efficient and innovative solutions to my clients.",
            "class_css": "bi bi-bar-chart" 
        },
        {
            "title" : "Objectives",
            "description" : "My primary objective is to build strong relationships with clients, deliver high-quality projects within agreed deadlines, and expand my business to reach new markets, offering diversified and high-quality services.",
            "class_css": "bi bi-binoculars" 
        },
        {
            "title" : "My Ideas",
            "description" : "I am constantly exploring new ideas and innovative approaches to address my clients' technological challenges, providing tailored and scalable solutions.",
            "class_css": "bi bi-brightness-high" 
        },
        {
            "title" : "Organization",
            "description" : "I meticulously organize my work by adhering to a precise schedule, ensuring timely delivery while upholding the quality of my deliverables. My approach revolves around collaboration with clients, promoting open communication and transparency throughout the development process.",
            "class_css": "bi bi-calendar4-week" 
        },

    ]
    
    for item in data:
        seeder.add_entity(Service,1,item)

    seeder.execute()
    print('Généré avec succès')