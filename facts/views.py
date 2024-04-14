from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# CRUD - Update
def update_facts(request, id):
    facts = Facts.objects.get(id=id)
    if request.method == 'POST':

        client_count = request.POST['client_count']
        projects_count = request.POST['projects_count']
        support_hours = request.POST['support_hours']
        workers_count = request.POST['workers_count']

        # Validation pour vérifier si les champs sont vides ou non des entiers
        if not client_count.isdigit() or not projects_count.isdigit() or not support_hours.isdigit() or not workers_count.isdigit():
            messages.error(request, "Please enter valid integer values for all fields!")
            return redirect('edit_facts', id=id)

        # Mise à jour des données si la validation réussit
        facts.client_count = int(client_count)
        facts.projects_count = int(projects_count)
        facts.support_hours = int(support_hours)
        facts.workers_count = int(workers_count)


        facts.save()

        messages.success(request, "Your facts section has been successfully modified!")

        return redirect('/')
    
    return render(request, 'facts.html', {'facts': facts})