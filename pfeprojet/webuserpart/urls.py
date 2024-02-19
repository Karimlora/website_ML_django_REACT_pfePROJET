from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('principal_dashboard/', views.PrincipalDashboardView.as_view(), name='principal_dashboard'),  # Assurez-vous que le nom correspond à celui utilisé dans la redirection
]
