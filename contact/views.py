from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# CRUD - Update
def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':

        location = request.POST['location']
        email = request.POST['email']
        call = request.POST['call']
        iframe = request.POST['iframe']

        # Si champ est vide ou contient uniquement des espaces
        if not location.strip():  
            messages.error(request, "Please enter the location!")
            return redirect('edit_contact', id=id)  
        if not email.strip():  
            messages.error(request, "Please enter the email!")
            return redirect('edit_contact', id=id)  
        if not call.strip():  
            messages.error(request, "Please enter the phone number!")
            return redirect('edit_contact', id=id)  
        if not iframe.strip():  
            messages.error(request, "Please enter the location link!")
            return redirect('edit_contact', id=id)  


        contact.location = location
        contact.email = email
        contact.call = call
        contact.iframe = iframe


        contact.save()

        messages.success(request, "Your contact section has been successfully modified!")

        return redirect('/')
    
    return render(request, 'contact.html', {'contact': contact})