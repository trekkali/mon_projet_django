from django.urls import path
from .views import signup, user_login, dashboard, reset
from .views import password_reset_confirm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_login, name='home'),  # Définis la vue de connexion comme vue pour l'URL racine
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('reset/', reset, name='reset'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
]