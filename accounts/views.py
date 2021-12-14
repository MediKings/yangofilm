from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import RegisterForm
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


def Home(request):
    return render(request, 'index.html')
