from django.urls import path
from .views import Admin


urlpatterns = [
    path('admin/', Admin, name='admin'),
]