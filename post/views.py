from django.http import HttpResponseRedirect
from django.urls import reverse     
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Post, Genre, Comment, Pub
from back.forms import CommentForm
from django.contrib.auth import get_user_model


User = get_user_model()

def Home(request):
    posts = Post.objects.all().order_by('-date')[:6]
    randoms = Post.objects.all().order_by('?')[:6]
    aside = Post.objects.all().order_by('?')[:6]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = {
        'posts': posts, 
        'randoms': randoms, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'post/index.html', context)


@login_required
def DetailPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    aside = Post.objects.all().order_by('?')[:8]
    genres = Genre.objects.all()
    template_name = 'post/detail_post.html'
    # Commentaires
    comments = Comment.objects.filter(post=post).order_by('date')
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('detail_post', args=[slug]))
    else:
        form = CommentForm()
    return render(request, template_name, {
        'post': post, 
        'form': form, 
        'comments': comments, 
        'genres': genres, 
        'aside': aside
        })

    
def Films(request):
    posts = Post.objects.filter(type=1).order_by('-date')
    aside = Post.objects.all().order_by('?')[:9]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = {
        'posts': posts, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'post/films.html', context)


def Series(request):
    posts = Post.objects.filter(type=2).order_by('-date')
    aside = Post.objects.all().order_by('?')[:9]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = {
        'posts': posts, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'post/series.html', context)


def Documentaires(request):
    posts = Post.objects.filter(type=3).order_by('-date')
    aside = Post.objects.all().order_by('?')[:9]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = {
        'posts': posts, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'post/documentaires.html', context)


def Emissions(request):
    posts = Post.objects.filter(type=4).order_by('-date')
    aside = Post.objects.all().order_by('?')[:9]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = {
        'posts': posts, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'post/emissions.html', context)


def Tele_realites(request):
    posts = Post.objects.filter(type=5).order_by('-date')
    aside = Post.objects.all().order_by('?')[:9]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = {
        'posts': posts, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'post/tele_realites.html', context)


def Genres(request, genre):
    genre_post = get_object_or_404(Genre, slug=genre)
    posts = Post.objects.filter(genre=genre_post)
    aside = Post.objects.all().order_by('?')[:5]
    genres = Genre.objects.all()
    template_name = 'post/genre.html'
    context = {
        'genre_post': genre_post, 
        'posts': posts, 
        'aside': aside,
        'genres': genres,
        }
    return render(request, template_name, context)


def Nouveautes(request):
    posts = Post.objects.all().order_by('-date')
    aside = Post.objects.all().order_by('?')[:9]
    genres = Genre.objects.all()
    template_name = 'post/nouveautes.html'
    context = {
        'posts': posts, 
        'aside': aside,
        'genres': genres,
        }
    return render(request, template_name, context)


# def Populaires(request):
#     posts = Post.objects.all()
#     aside = Post.objects.all().order_by('?')[:9]
#     genres = Genre.objects.all()
#     template_name = 'post/populaires.html'
#     context = {
#         'posts': posts, 
#         'aside': aside,
#         'genres': genres,
#         }
#     return render(request, template_name, context)


# def Meilleures(request):
#     posts = Post.objects.all()
#     aside = Post.objects.all().order_by('?')[:9]
#     genres = Genre.objects.all()
#     template_name = 'post/meilleures.html'
#     context = {
#         'posts': posts, 
#         'aside': aside,
#         'genres': genres,
#         }
#     return render(request, template_name, context)


# def Suggestions(request):
#     posts = Post.objects.all()
#     aside = Post.objects.all().order_by('?')[:9]
#     genres = Genre.objects.all()
#     template_name = 'post/suggestions.html'
#     context = {
#         'posts': posts, 
#         'aside': aside,
#         'genres': genres,
#         }
#     return render(request, template_name, context)




def Search(request):
    search = request.GET.get('search')
    posts = Post.objects.filter(title__icontains=search)
    aside = Post.objects.all().order_by('?')[:5]
    genres = Genre.objects.all()
    context = {
        'search': search,
        'posts': posts,
        'aside': aside,
        'genres': genres,
        }
    return render(request, 'post/search.html', context)
  