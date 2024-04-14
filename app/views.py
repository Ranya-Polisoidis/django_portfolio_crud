from django.shortcuts import render, redirect
from .models import * # pour homebackground
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
from testimonial.models import *
from testimonial.views import *
from contact.models import *
from contact.views import *
from django.contrib import messages


# Create your views here.

def index (request):
    homebackground=Homebackground.objects.first()
    about = About.objects.first()
    facts = Facts.objects.first()
    skills = Skills.objects.all()
    theportfolio = Theportfolio.objects.all()
    # J'aurais pu aussi faire des first (comme pour about et facts mais + limiter)
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    contact = Contact.objects.first()
    return render(request, "index.html", {"homebackground": homebackground, "about": about, "facts": facts, "skills": skills, "theportfolio": theportfolio, "service": service, "testimonial":testimonial, "contact":contact})


def administration (request):
    homebackground=Homebackground.objects.first()
    about = About.objects.first()
    facts = Facts.objects.first()
    skills = Skills.objects.all()
    theportfolio = Theportfolio.objects.all()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    contact = Contact.objects.first()
    return render(request, "administration.html", {"homebackground": homebackground, "about": about, "facts": facts, "skills": skills, "theportfolio": theportfolio, "service": service, "testimonial":testimonial, "contact":contact})

# CRUD - Update
def update_homebackground(request, id):
    homebackground = Homebackground.objects.get(id=id)
    if request.method == 'POST':

        # Vérifier si nouvelle image
        if 'image' in request.FILES:
            image = request.FILES['image']
            homebackground.image = image
        else:
        # Si aucune nouvelle image, garder l'image de base
            image = homebackground.image
        
        homebackground.save()

        messages.success(request, 'Your home background has been successfully modified!')

        return redirect('/')
    
    return render(request, 'homebackground.html', {'homebackground': homebackground})
