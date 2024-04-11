import django
django.setup()
from about.seed import *
from facts.seed import *
from skills.seed import *


if __name__== '__main__':
    # run_about()
    # run_facts()
    run_skills()
