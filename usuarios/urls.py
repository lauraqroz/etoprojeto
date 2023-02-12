from django.urls import path 
from django.contrib.auth import views as auth_views 
from principal.views import *

 

urlpatterns = [
   
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/usuario.html'
     ), name = 'login'),
    path('accounts/', conta , name='conta'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name = 'logout'),   
    path('accounts/cadastro', cadastro , name='cadastro'),
]
