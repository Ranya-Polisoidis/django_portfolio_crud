"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
# from about.views import *

# Pour importer des images depuis les fichiers de notre (pc, tel ...)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    # path('header/', header),

    path('administration/', administration, name="administration"),

    # path('administration/about/', administration_about, name="administration_about"),
    path('administration/about/edit/<int:id>/', update_about, name="edit_about"),
    # path('administration/about/delete/<int:id>', destroy, name="delete"),

    path('administration/facts/edit/<int:id>/', update_facts, name="edit_facts"),


    # path('create', create) # faire modifier et supp le profil pas crée 
    # path('administration/skills/', administration_skills, name="administration_skills"),
    # path('administration/portfolio/', administration_portfolio, name="administration_portfolio"),
    # path('administration/service/', administration_service, name="administration_service"),
    # path('administration/testimonial/', administration_testimonial, name="administration_testimonial"),
    # path('administration/contact/', administration_contact, name="administration_contact")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)