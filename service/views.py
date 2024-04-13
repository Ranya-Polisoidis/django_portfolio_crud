from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def service(request):
    service = Service.objects.all()
    return render(request, "service.html", {"service":service})


# CRUD - Update
def update_service(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']

        # Si le champs est vide
        if not title.strip():  
            messages.error(request, 'Veuillez saisir le titre !')
            return redirect('edit_service', id=id)  
        
        if not description.strip():  
            messages.error(request, 'Veuillez saisir la description !')
            return redirect('edit_service', id=id)  

        service.title = title
        service.description = description

        service.save()

        messages.success(request, 'Votre section service a bien été modifier !')

        return redirect('/')
    
    return render(request, 'service_edit.html', {'service': service})


