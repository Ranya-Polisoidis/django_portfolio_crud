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
            "city": "Brussels, Belgium",
            "age": 39,
            "degree": "Master's degree in Computer Science",
            "email": "jeandupont@gmail.com",
            "freelance": "Available",
            "description": "Passionate about web development for over 10 years, I have built a solid expertise in frontend, backend, and database design, working on a variety of projects ranging from small applications to complex systems. My mastery of technologies such as HTML, CSS, JavaScript, Python, Django, Vue.js, and Node.js, combined with my commitment to continuous learning, make me a valuable asset for any development team.",
            "profession": "Full Stack Developer",
            "about_you": "I am a passionate developer dedicated to creating high-performing and intuitive web applications. With over 10 years of experience in software development and project management, my expertise spans both frontend and backend development, as well as robust database design. I am also skilled in deploying and maintaining large-scale applications.",
            "more_info": "I have worked on a multitude of projects, ranging from small web applications to complex enterprise systems. I have deep expertise in technologies such as HTML, CSS, JavaScript, Python, Django, Vue.js, and Node.js. My passion for continuous learning and commitment to best development practices make me a valuable asset to any development team."
        },
    ]

    for item in data:
        seeder.add_entity(About,1,item)

    seeder.execute()
    print('Généré avec succès')
