from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date, parse_time
from django.utils import timezone
from datetime import timedelta, time
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
    today = timezone.localdate()
    one_month_ahead = today + timedelta(days=30)
    hours = ['{:02d}:00'.format(hour) for hour in range(8, 19)]
    if request.method == 'POST':
        date_input = request.POST.get('date')
        time_input = request.POST.get('time')
        guests = request.POST.get('guests')
        print('data:', date_input, time_input, guests)

        
        reservation_date = parse_date(date_input)
        reservation_time = parse_time(time_input)

        # Date checks
        today = timezone.localdate()
        if reservation_date < today:
            messages.error(request, 'You cannot make a reservation for a past date.')
            return redirect('/reservation/?section=add')
        
        one_month_ahead = today + timedelta(days=30)
        if reservation_date > one_month_ahead:
            messages.error(request, 'You can only make reservations up to one month in advance.')
            return redirect('/reservation/?section=add')

        # Time checks
        if reservation_time < time(8, 0) or reservation_time > time(18, 0) or reservation_time.minute != 0:
            messages.error(request, 'Please select a time between 08:00 and 18:00 at exact hours.')
            return redirect('/reservation/?section=add')

        # Conflict checks
        if Reservation.objects.filter(date=reservation_date, time=reservation_time).exists():
            messages.error(request, 'A reservation already exists at the specified date and time.')
            return redirect('/reservation/?section=add')

        if date_input and time_input and guests:
            reservation = Reservation(
                user=request.user,
                date=reservation_date,
                time=reservation_time,
                guests=guests
            )
            reservation.save()
            messages.success(request, 'Your reservation was successfully made.')
            return redirect('/reservation/?section=myreservations')
        else:
            messages.error(request, 'Please fill in all fields.')

    section = request.GET.get('section', 'myreservations')
    reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'reservation.html', {
        'today': today,
        'one_month_ahead': one_month_ahead,
        'section': section,
        'reservations': reservations,
        'hours': hours
    })

@login_required
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation deleted successfully.')
        return redirect('/reservation/?section=myreservations') 

def vegan(request):
    return render(request, 'vegan.html')

def custom_404_view(request, *args, **argv):
    return render(request, '404.html', status=404)