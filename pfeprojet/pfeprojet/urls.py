from django.contrib import admin
from django.urls import path, include
from webuserpart.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('webuserpart.urls')), 
    path('', HomePageView.as_view(), name='home'),  # Route pour la page d'accueil
]
