from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('r/<int:pk>/', views.detail, name='detail'),
    path('register/',register,name='register'),
    path('login/',sigin,name='login'),
    path('logout/',signout,name='logout'),
    path('patient/registration/', AddPatients.as_view(), name='addp'),
    path('nurse/registration/', AddNurses.as_view(), name='addn'),
    path('doctor/registration/', AddDoctors.as_view(), name='addd'),
    path('maindoctor/registration/', AddMaindoctors.as_view(), name='addm'),
]