from django.urls import path
from .views import signup, user_login, dashboard, reset

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),  # Mettez à jour cette ligne
    path('dashboard/', dashboard, name='dashboard'),
    path('reset/', reset, name='reset'),
]
