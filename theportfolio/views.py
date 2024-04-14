from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def theportfolio(request):
    theportfolio = Theportfolio.objects.all()
    return render(request, "theportfolio.html", {"theportfolio":theportfolio})

# Crée
def add_theportfolio(request):
    if request.method == "POST": 

        title = request.POST['title']

        # Vérifier si le champ title est vide ou contient uniquement des espaces
        if not title.strip():  
            messages.error(request, "Please enter the title!")
            return redirect('add_theportfolio') 
        
        # Vérifier si il y a une image
        if 'image' not in request.FILES:
            messages.error(request, "Please select an image!")
            return redirect('add_theportfolio')
        else:
            image = request.FILES['image']

        theportfolio = Theportfolio(image=image,title=title)
        theportfolio.save()
        messages.success(request, "Your element has been successfully added!")

        return redirect('/')  
    
    return render(request, "theportfolio_add.html")


# CRUD - Update
def update_theportfolio(request, id):
    theportfolio = Theportfolio.objects.get(id=id)
    if request.method == 'POST':

        title = request.POST['title']

        # Si le champ title est vide ou contient uniquement des espaces
        if not title.strip():  
            messages.error(request, "Please enter the title!")
            return redirect('edit_theportfolio', id=id)  
        
        # Vérifier si nouvelle image
        if 'image' in request.FILES:
            image = request.FILES['image']
            theportfolio.image = image
        else:
        # Si aucune nouvelle image, garder l'image de base
            image = theportfolio.image


        theportfolio.title = title

        theportfolio.save()

        messages.success(request, "Your element has been successfully modified!")

        return redirect('/')
    
    return render(request, 'theportfolio_edit.html', {'theportfolio': theportfolio})


# CRUD - Delete
def destory_theportfolio(request, id):
    theportfolio = Theportfolio.objects.get(id=id)
    theportfolio.delete()
    messages.success(request, "Your element has been successfully deleted!")
    return redirect('/')