from django.urls import path
from .views import signup, user_login, dashboard, reset

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_login, name='home'),  # Définis la vue de connexion comme vue pour l'URL racine
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='reset.html'), name='reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
]