from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), # URL para Home 
    path('about/', views.about, name='about'), # URL para About 
    path('contact/', views.contact, name='contact'), # URL para Contact 
]