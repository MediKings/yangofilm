from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from post.models import Post, Genre, Pub
from django.contrib.auth import get_user_model


User = get_user_model()

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, f"Successfully")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def Login(request):
    email_phone = request.POST.get('email_phone')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(email=email_phone).exists()):
            user = authenticate(username=email_phone, password=password)
        else:
            user = User.objects.get(phone=email_phone)
            user = authenticate(username=user.email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f"Données incorrects! Réessayez")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    return redirect('login')


@login_required
def Profile(request):
    aside = Post.objects.all().order_by('?')[:10]
    genres = Genre.objects.all()
    pubs = Pub.objects.all()
    context = { 
        'user': request.user, 
        'genres': genres, 
        'aside': aside,
        'pubs': pubs
        }
    return render(request, 'accounts/profile.html', context)


@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile mis à jour avec succès')
            return redirect('profile')
        else:
            messages.error(request, f'Echec de mis à jour')
    return render(request, 'accounts/update_profile.html', {'form': form})
    