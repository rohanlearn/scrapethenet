from django.urls import path

from .views import scrape 
from .views import help 
from .views import home# scrape views function from views.py

urlpatterns = [path("", scrape, name="extractimg"),
path('help', help, name="help"),
path('home', home, name='home')]
