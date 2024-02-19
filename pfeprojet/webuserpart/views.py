from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import TemplateView

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Rediriger l'utilisateur vers la page principale après connexion réussie
            return redirect('principal_dashboard')  # Remplacez 'principal_dashboard' par le nom de votre vue de page principale
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Rediriger l'utilisateur vers la page principale après inscription réussie
            return redirect('principal_dashboard')  # Remplacez 'principal_dashboard' par le nom de votre vue de page principale
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class PrincipalDashboardView(TemplateView):
    template_name = 'principal_dashboard.html' 