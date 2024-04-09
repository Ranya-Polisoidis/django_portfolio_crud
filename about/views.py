from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# Juste modifier  (ici c'est crée)

# def create_image(request):
#     if request.method == 'POST':
#         image = request.FILES['image']
#         image = About(image=image)
#         image.save()
#         return redirect('index')

# Faire en sorte de modifier 


# CRUD - Update
def update_about(request, id):
    about = About.objects.get(id=id)
    if request.method == 'POST':
        image = request.FILES['image']
        # name = request.POST['name']
        birthday = request.POST['birthday']
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

        # # Message d'erreur (mes modifs: "/" en "/about") ou directe autre manière par about (si name="about" dans urls.py)
        # if int(prix) < 5: 
        #     messages.error(request, 'Pas assez cher (après ma modificaton)')
        #     # return redirect("/about")  
        #     return redirect("about")  

        # about.image = image
        # about.name = name
        about.birthday = birthday
        about.website = website
        about.phone = phone
        about.city = city
        # if image is None:
        #     about.image = about.image
        # else:
        about.image = image
        about.age = age
        about.degree = degree
        about.email = email
        about.freelance = freelance
        about.description = description
        about.profession = profession
        about.about_you = about_you
        about.more_info = more_info
        #
        about.save()

        # Message de succès (mes modifs: crée par modifier) 
        messages.success(request, 'Votre section about à bien été modifier !')

        # return redirect('/products') # ex
        return redirect('/')
    
    return render(request, 'about.html', {'about': about})
