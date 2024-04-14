import django
django.setup()
from app.seed import * # Pour run_homebackground
from about.seed import *
from facts.seed import *
from skills.seed import *
from theportfolio.seed import *
from service.seed import *
from testimonial.seed import *
from contact.seed import *


if __name__== '__main__':
    # run_homebackground()
    # run_about()
    run_facts()
    # run_skills()
    # run_theportfolio()
    # run_service()
    # run_testimonial()
    # run_contact()

