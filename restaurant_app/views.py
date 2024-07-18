from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from myapp.models import Reservation
User = get_user_model()

# Create your views here.

def home(request):
    return render(request, 'index.html')

def user_logout(request):
    logout(request)
    return redirect('home') 


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect('home')
            else:
                messages.error(request, "Your account is disabled.")
                return render(request, 'login.html')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html', {'form': request.POST})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user) 
        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('home')

    return render(request, 'register.html')

def reservation(request):
    return render(request, 'reservation.html')

@login_required
def make_reservation(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        if date and time and guests:
            reservation = Reservation(
                user=request.user,
                date=date,
                time=time,
                guests=guests
            )
            reservation.save()
            messages.success(request, 'Your reservation was successful.')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'reservation.html')

def vegan(request):
    return render(request, 'vegan.html')

def custom_404_view(request, *args, **argv):
    return render(request, '404.html', status=404)