from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout



def register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.add_message(request, messages.SUCCESS, f'user {username} has been created successfully')
    return render(request, 'user_forms.html',
                             {'form': form})


def login_view(request):
    form = UserLoginForm()
    username = request.POST.get('')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f'user {user.username} has been logged in')
            return redirect('home')
        else:
            messages.add_message(request, messages.WARNING, 'WRONG CREDENTIALS')

    return render(request, 'user_forms.html',
                  {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')