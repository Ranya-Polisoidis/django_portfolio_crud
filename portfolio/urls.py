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

    path('administration/', administration, name="administration"),

    # Avec first sans boucle 
    path('administration/about/edit/<int:id>/', update_about, name="edit_about"),
    path('administration/facts/edit/<int:id>/', update_facts, name="edit_facts"),

    # Avec all avec for
    path('administration/skills/', skills, name="skills"),
    path('administration/skills/add/', add_skills, name="add_skills"),
    path('administration/skills/edit/<int:id>/', update_skills, name="edit_skills"),
    path('administration/skills/delete/<int:id>/', destory_skills, name="delete_skills"),

    path('administration/theportfolio/', theportfolio, name="theportfolio"),
    path('administration/theportfolio/add/', add_theportfolio, name="add_theportfolio"),
    path('administration/theportfolio/edit/<int:id>/', update_theportfolio, name="edit_theportfolio"),
    path('administration/theportfolio/delete/<int:id>/', destory_theportfolio, name="delete_theportfolio"),

    path('administration/service/', service, name="service"),
    path('administration/service/edit/<int:id>/', update_service, name="edit_service"),

    # Testimoniale tout faire je pense

    # contacte juste modifier

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)