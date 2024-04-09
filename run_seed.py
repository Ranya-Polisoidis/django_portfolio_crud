import django
django.setup()
from about.seed import *

if __name__== '__main__':
    run_about()
