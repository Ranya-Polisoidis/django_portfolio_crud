from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request, "testimonial.html", {"testimonial":testimonial})


# CRUD - Update
def update_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)
    if request.method == 'POST':

        comment = request.POST['comment']
        name = request.POST['name']
        job = request.POST['job']

        # Si champ est vide ou contient uniquement des espaces
        if not comment.strip():  
            messages.error(request, "Please enter the comment!")
            return redirect('edit_testimonial', id=id)  
        if not name.strip():  
            messages.error(request, "Please enter the name!")
            return redirect('edit_testimonial', id=id)  
        if not job.strip():  
            messages.error(request, "Please enter the job!")
            return redirect('edit_testimonial', id=id)  
    

        # Vérifier si nouvelle image
        if 'image' in request.FILES:
            image = request.FILES['image']
            testimonial.image = image
        else:
        # Si aucune nouvelle image, garder l'image de base
            image = testimonial.image


        testimonial.comment = comment
        testimonial.name = name
        testimonial.job = job

        testimonial.save()

        messages.success(request, "Your testimonial section has been successfully modified!")

        return redirect('/')
    
    return render(request, 'testimonial_edit.html', {'testimonial': testimonial})

