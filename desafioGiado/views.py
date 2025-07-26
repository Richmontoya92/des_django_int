from django.shortcuts import render

def home(request): # Vista para el Home 
    return render(request, 'home.html')

def about(request): # Vista para el About 
    return render(request, 'about.html')

def contact(request): # Vista para el Contact con formulario 
    return render(request, 'contact.html')