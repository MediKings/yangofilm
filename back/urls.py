from django.urls import path
from .views import AddPost, UpdatePost, DeletePost


urlpatterns = [
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('update_post/<str:slug>', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<str:slug>', DeletePost.as_view(), name='delete_post'),
]