from django.urls import path
from .views import home, profile, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('home/', home, name='users-home'),
    #path('general/', homegen, name='users-gen'),
    #path('business/', homebus, name='users-bus'),
    #path('entertainment/', homeent, name='users-ent'),
    #path('health/', homehealth, name='users-health'),
    #path('science/', homescience, name='users-science'),
    #path('sport/', homesport, name='users-sport'),
    #path('technology/', hometech, name='users-tech'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]


