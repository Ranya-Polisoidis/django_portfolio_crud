from django.shortcuts import render, redirect
from .models import *
from about.models import *


# Create your views here.

def index (request):
    image = About.objects.all()
    return render(request, "index.html", {"image": image})


def portfolio_details (request):
    # product = Product.objects.get(id=id)
    return render(request, "portfolio-details.html")

# def portfolio_details (request, id):
#     # product = Product.objects.get(id=id)
#     return render(request, "details", {"product": product})


# BackEnd
def administration (request):
    return render(request, "administration.html")

def administration_about (request):
    image = About.objects.all()
    return render(request, "about.html", {'image': image})

def administration_skills (request):
    return render(request, "skills.html")

def administration_portfolio (request):
    return render(request, "portfolio.html")

def administration_service (request):
    return render(request, "service.html")

def administration_testimonial (request):
    return render(request, "testimonial.html")

def administration_contact (request):
    return render(request, "contact.html")
# Fin BackEnd
