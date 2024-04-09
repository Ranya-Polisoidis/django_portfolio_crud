from .models import *
from django_seed import Seed

def run_about():

    seeder = Seed.seeder()
    
    data = [
        {
            'image': 'images/profile-img.jpg',
            "name": "Jean Dupont",
            "birthday": "1985-03-20",
            "website": "www.jeandupont.com",
            "phone": "+32 123 456 789",
            "city": "Bruxelles, Belgique",
            "age": 39,
            "degree": "Master en informatique",
            "email": "jeandupont@gmail.com",
            "freelance": "Disponible",
            "description": "Passionné par le développement web depuis plus de 10 ans, j'ai acquis une expertise solide en frontend, backend et en conception de bases de données, travaillant sur une variété de projets allant des petites applications aux systèmes complexes. Ma maîtrise des technologies telles que HTML, CSS, JavaScript, Python, Django, Vue.js et Node.js, associée à mon engagement pour l'apprentissage continu, font de moi un atout précieux pour toute équipe de développement.",
            "profession": "Développeur Full Stack",
            "about_you": "Je suis un développeur passionné par la création d'applications web performantes et intuitives. Fort de plus de 10 ans d'expérience dans le développement de logiciels et la gestion de projets, mon expertise couvre à la fois le développement frontend et backend, ainsi que la conception de bases de données robustes. Je suis également compétent dans le déploiement et la maintenance d'applications à grande échelle.",
            "more_info": "J'ai travaillé sur une multitude de projets, allant de petites applications web à des systèmes d'entreprise complexes. Je possède une expertise approfondie dans les technologies telles que HTML, CSS, JavaScript, Python, Django, Vue.js et Node.js. Ma passion pour l'apprentissage continu et mon engagement envers les meilleures pratiques de développement font de moi un atout précieux pour toute équipe de développement."
        },
    ]

    for item in data:
        seeder.add_entity(About,1,item)

    seeder.execute()
    print('Généré avec succès')
