from django.urls import path
from .views import Index, Logout, Register, Login


urlpatterns = [
    path('', Index, name='compte'),
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
]