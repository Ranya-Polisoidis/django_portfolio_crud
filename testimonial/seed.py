from .models import *
from django_seed import Seed

def run_testimonial():

    seeder = Seed.seeder()

    data = [
        {
            "comment" : "Great job! Your expertise in web development has been remarkable. The solutions you've created really met our needs and exceeded our expectations. Thank you for your professionalism and dedication.",
            "image" : "images/testimonials-1.jpg",
            "name" : "Saul Goodman",
            "job": "Ceo Founder",
        },
        {
            "comment": "I'm very impressed with your expertise in web development. Your ability to understand our specific needs and translate them into effective technical solutions has been outstanding. Your work has truly made a difference for our company.",
            "image" : "images/testimonials-2.jpg",
            "name" : "Sara Wilsson",
            "job": "Designer",
        },
        {
            "comment": "Your expertise in web development has been a valuable asset to our project. Your technical skills combined with your collaborative approach enabled seamless project execution. Thank you for your exceptional contribution!",
            "image" : "images/testimonials-3.jpg",
            "name" : "Jena Karlis",
            "job": "Store Owner",
        },
        {
            "comment": "I want to commend you on your expertise in web development. Your thorough understanding of technologies and your ability to quickly solve problems have been remarkable. It was a pleasure working with you!",
            "image" : "images/testimonials-4.jpg",
            "name" : "Matt Brandon",
            "job": "Freelancer",
        },
        {
            "comment": "Your expertise in web development has been a key factor in our success. Your informed advice and innovative solutions helped us achieve our goals within the specified timelines. We are grateful for your excellent work!",
            "image" : "images/testimonials-5.jpg",
            "name" : "John Larson",
            "job": "Entrepreneur",
        },
    ]
    
    for item in data:
        seeder.add_entity(Testimonial,1,item)

    seeder.execute()
    print('Généré avec succès')