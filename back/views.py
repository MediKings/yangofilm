from django.views.generic.edit import CreateView, UpdateView, DeleteView
from post.models import Post
from post.forms import PostForm


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
