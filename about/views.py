from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# CRUD - Update
def update_about(request, id):
    about = About.objects.get(id=id)
    if request.method == 'POST':

        # Si je modifie rien pour img, erreur donc je le mets dans une cond. (juste en bas)
        # image = request.FILES['image']

        name = request.POST['name']

        # Le input est de type date et ne garde pas la value précédente donc je la force
        # birthday = request.POST['birthday']

        # Récupérer le champ birthday du formulaire
        birthday = request.POST['birthday']

        # Vérifier si le champ de date est vide
        if not birthday:
            # Si vide je garde le précédents (juste avec le value et name (suffit pas car le input est de type date et le garde pas))
            birthday = about.birthday

        website = request.POST['website']
        phone = request.POST['phone']
        city = request.POST['city']
        age = request.POST['age']
        degree = request.POST['degree']
        email = request.POST['email']
        freelance = request.POST['freelance']
        description = request.POST['description']
        profession = request.POST['profession']
        about_you = request.POST['about_you']
        more_info = request.POST['more_info']

        # Vérifier si nouvelle image
        if 'image' in request.FILES:
            image = request.FILES['image']
            about.image = image
        else:
        # Si aucune nouvelle image, garder l'image de base
            image = about.image

        about.name = name
        about.birthday = birthday
        about.website = website
        about.phone = phone
        about.city = city
        about.age = age
        about.degree = degree
        about.email = email
        about.freelance = freelance
        about.description = description
        about.profession = profession
        about.about_you = about_you
        about.more_info = more_info
        
        about.save()

        messages.success(request, 'Your about section has been successfully modified!')

        return redirect('/')
    
    return render(request, 'about.html', {'about': about})
