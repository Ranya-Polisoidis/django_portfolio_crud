from django.shortcuts import render, redirect
from .models import *
from about.models import *
from about.views import *
from facts.models import *
from facts.views import *
from skills.models import *
from skills.views import *
from theportfolio.models import *
from theportfolio.views import *
from service.models import *
from service.views import *

# Create your views here.

def index (request):
    about = About.objects.first()
    facts = Facts.objects.first()
    skills = Skills.objects.all()
    theportfolio = Theportfolio.objects.all()
    # service = Service.objects.first()
    service = Service.objects.all()
    return render(request, "index.html", {"about": about, "facts": facts, "skills": skills, "theportfolio": theportfolio, "service": service})


def administration (request):
    about = About.objects.first()
    facts = Facts.objects.first()
    skills = Skills.objects.all()
    theportfolio = Theportfolio.objects.all()
    # service = Service.objects.first()
    service = Service.objects.first()
    return render(request, "administration.html", {"about": about, "facts": facts, "skills": skills, "theportfolio": theportfolio, "service": service})


# Voir pour mon image
# def update_facts (request):
#     about = About.objects.first()
#     facts = Facts.objects.first()
#     skills = Skills.objects.all()
#     return render(request, "facts.html", {"about": about, "facts": facts,  "skills": skills})


# def about (request):
#     about = About.objects.first()
#     facts = Facts.objects.first()
#     skills = Skills.objects.all()
#     return render(request, "administration.html", {"about": about, "facts": facts,  "skills": skills})

