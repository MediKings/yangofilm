from django.urls import path
from .views import Admin, Authors, AddPost, UpdatePost, DeletePost


urlpatterns = [
    path('admin/', Admin, name='admin'),
    path('authors/', Authors, name='authors'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('update_post/<slug:slug>/', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<slug:slug>/', DeletePost.as_view(), name='delete_post'),
]