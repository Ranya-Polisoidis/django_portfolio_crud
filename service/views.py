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
            messages.error(request, "Please enter the title!")
            return redirect('edit_service', id=id)  
        
        if not description.strip():  
            messages.error(request, "Please enter the description!")
            return redirect('edit_service', id=id)  

        service.title = title
        service.description = description

        service.save()

        messages.success(request, "Your service section has been successfully modified!")

        return redirect('/')
    
    return render(request, 'service_edit.html', {'service': service})


