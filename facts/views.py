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

        facts.client_count = client_count
        facts.projects_count = projects_count
        facts.support_hours = support_hours
        facts.workers_count = workers_count

        facts.save()

        messages.success(request, 'Votre section facts à bien été modifier !')

        return redirect('/')
    
    return render(request, 'facts.html', {'facts': facts})