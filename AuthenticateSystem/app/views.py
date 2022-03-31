from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from .forms import UserForm


# Create your views here.

@login_required(login_url='login')
def HomePage(request):

    return render(request, 'home.html')

def LoginUser(request):
    try:
        if request.user.is_authenticated is True:
            return redirect('home')
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username,password)
            if(username is None or password is None):
                return render(request, 'login.html', {'error': 'Please fill all the details'})
            try:
                user = authenticate(request, username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'error': 'Invalid email or Password'})
            except Exception as e:
                return render(request, 'login.html', {'error':e})
        return render(request, 'login.html')
    except Exception as e:
        print(e)
        return redirect('login')

def RegisterUser(request):
    try:
        if request.user.is_authenticated is True:
            return redirect('home')
        uform = UserForm()
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.errors:
                print(form.errors)
                return render(request, 'register.html', {'error': form.errors})
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('login')
        return render(request, 'register.html', {'form':uform})
    except:
        return redirect('register')

def LogoutUser(request):
    logout(request)
    return redirect('login')