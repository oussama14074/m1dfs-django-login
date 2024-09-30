from django.contrib import admin
from django.urls import path
from auth_app import views
from unicodedata import name


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inscription,name='inscription'),
    path('connexion/',views.connexion,name='connexion'),
    path('acceuil/',views.acceuil,name='acceuil'),
    path('deconnexion/',views.deconnexion,name='deconnexion'),
]
