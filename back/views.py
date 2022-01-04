from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from post.forms import PostForm
from post.models import Post


User = get_user_model()

def Admin(request):
    authors = Post.type
    template_name = 'back/admin.html'
    context = {'authors': authors}
    return render(request, template_name, context)


def Authors(request):
    template_name = 'back/admin.html'
    return render(request, template_name)


# CRUD
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'back/add_post.html'
    success_url = '/'

class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'back/update_post.html'
    success_url = '/'

class DeletePost(DeleteView):
    model = Post
    template_name = 'back/delete_post.html'
    success_url = '/'
