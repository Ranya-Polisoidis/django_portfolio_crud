from django.shortcuts import render, redirect
from .models import *
from about.models import *
from about.views import *

# Create your views here.

def index (request):
    about = About.objects.first()
    return render(request, "index.html", {"about": about})

def header (request):
    about = About.objects.all()
    return render(request, "header.html", {"about": about})

# BackEnd
def administration (request):
    about = About.objects.first()
    return render(request, "administration.html", {"about": about})



# def administration_about (request):
#     about = About.objects.all()
#     return render(request, "about.html", {'about': about})

# def administration_skills (request):
#     return render(request, "skills.html")

# def administration_portfolio (request):
#     return render(request, "portfolio.html")

# def administration_service (request):
#     return render(request, "service.html")

# def administration_testimonial (request):
#     return render(request, "testimonial.html")

# def administration_contact (request):
#     return render(request, "contact.html")
# Fin BackEnd
