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
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        if User.objects.filter(email=email):
            messages.warning(request, "Cet email existe déjà")
            return redirect('register')
        elif User.objects.filter(phone=phone):
            messages.warning(request, "Ce numéro existe déjà !")
            return redirect('register')
        else:
            user = User.objects.create_user(email, phone, password1)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            if user:
                auth = authenticate(username=user.email, password=password1)
                if auth is not None:
                    login(request, auth)
                    messages.success(request, f"Enregistrement réussit")
                    return redirect('home')
    return render(request, 'accounts/register.html', {})


def Login(request):
    email_phone = request.POST.get('email_phone')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(email=email_phone).exists()):
            user = authenticate(username=email_phone, password=password)
        elif(User.objects.filter(phone=email_phone).exists()):
            user = User.objects.get(phone=email_phone)
            user = authenticate(username=user.email, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('login')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Données incorrects! Réessayez")
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
    