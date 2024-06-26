from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def skills(request):
    skills = Skills.objects.all()
    return render(request, "skills.html", {"skills":skills})

# Crée
def add_skills(request):
    if request.method == "POST": 

        langages = request.POST['langages']
        percentage = request.POST['percentage']

        # Si le champ langages est vide ou contient uniquement des espaces
        if not langages.strip():  
            messages.error(request, "Please enter the language!")
            return redirect('add_skills') 
        
        skills = Skills(langages=langages,percentage=percentage)
        skills.save()
        messages.success(request, "Your skill has been successfully added!")

        return redirect('/')  
    
    return render(request, "skills_add.html")

# CRUD - Update
def update_skills(request, id):
    skills = Skills.objects.get(id=id)
    if request.method == 'POST':

        langages = request.POST['langages']
        percentage = request.POST['percentage']

        # Comme au-dessus
        if not langages.strip():  
            messages.error(request, "Please enter the language!")
            return redirect('edit_skills', id=id)  

        skills.langages = langages
        skills.percentage = percentage

        skills.save()

        messages.success(request, "Your skill has been successfully modified!")

        return redirect('/')
    
    return render(request, 'skills_edit.html', {'skills': skills})

# CRUD - Delete
def destory_skills(request, id):
    skills = Skills.objects.get(id=id)
    skills.delete()
    messages.success(request, "Your skill has been successfully deleted!")
    # return redirect('/')
    return redirect('/')