from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages  # Ajout de l'import pour les messages d'erreur
from .forms import SignUpForm  # Importez votre formulaire SignUpForm
from .forms import LoginForm
from django.contrib.auth import logout

def signup(request):
    email_exists = False  # Initialiser la variable à False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            subscribe_to_newsletter = form.cleaned_data['subscribe_to_newsletter']
            user = User.objects.filter(username=email).first()
            if user is not None:
                email_exists = True  # Mettre à True si l'e-mail existe déjà
                # messages.error(request, "User with this email already exists.")
                # return render(request, 'signup.html', {'form': form})
            else:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
                # Authentifier et connecter l'utilisateur nouvellement créé
                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error with field '{field}': {error}")
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'email_exists': email_exists})



def user_logout(request):
    logout(request)
    return redirect('login')  # Redirige vers la page de connexion
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authentification de l'utilisateur
            user = authenticate(request, username=email, password=password)  # Utilisez 'username' au lieu de 'email'
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                # Gérer les cas où l'authentification échoue
                # Vous pouvez ajouter un message d'erreur ou une autre logique ici
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def reset(request):
    return render(request, 'reset.html')

def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')