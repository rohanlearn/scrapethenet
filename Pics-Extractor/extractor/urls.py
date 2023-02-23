from django.urls import path
from .views import download

from .views import help,Login,signup,home,Logout,history
from .views import home# scrape views function from views.py

urlpatterns = [path('', signup, name='signup'),
    path("home/", home, name="home"),
path('help/', help, name="help"),
path('download/', download, name='download'),
path('login/', Login, name='login'),
path('signup/', signup, name='signup'),
path('logout/', Logout, name='logout'),
path('history/', history, name='history')
]
