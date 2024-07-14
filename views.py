from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from .models import appointments


@login_required
def accounts_view(request):
    user = request.user
    user_appointments = appointments.objects.filter(nume=user.last_name, prenume=user.first_name)
    context = {
        'email': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'appointments': user_appointments
    }
    return render(request, 'accounts/accounts.html', context)

@login_required
def profile_view(request):
    user = request.user
    last_login = user.last_login
    return render(request, 'profile.html', {'last_login': last_login})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_view')  
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'accounts/register.html')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'accounts/Main.html')

def contact(request):
    return render(request, 'accounts/Contactt.html')

def prices(request):
    return render(request, 'accounts/Prices.html')
def appm(request):
    if request.method == 'POST':
        selected_services = request.POST.getlist('selected_services')
        request.session['selected_services'] = selected_services
        return redirect('end')
    else:
        return render(request, 'accounts/Programari-barbat.html')
def appf(request):
    if request.method == 'POST':
        selected_services = request.POST.getlist('selected_services')
        request.session['selected_services'] = selected_services
        return redirect('end')
    else:
        return render(request, 'accounts/Programari-femeie.html')
def app(request):
    return render(request, 'accounts/Programarii.html')

def end(request):
    if request.method == 'POST':
        selected_services = request.session.get('selected_services', [])
        selected_services_str = ','.join(selected_services)
        appointment = appointments.objects.create(
            nume=request.POST.get('nume'),
            prenume=request.POST.get('prenume'),
            data_preferinta=request.POST.get('data_preferinta'),
            ora_preferinta=request.POST.get('ora_preferinta'),
            favStylist=request.POST.get('favStylist', ''),
            favStylistName=request.POST.get('favStylistName', ''),
            telefon=request.POST.get('telefon', ''),
            mail=request.POST.get('mail', ''),
            selected_services=selected_services_str,
           
        )

        request.session.pop('selected_services', None)
        return render(request, 'accounts/Main.html')
    else: 
        return render(request, 'accounts/Sfarsit.html')

def employee(request):
    return render(request, 'accounts/Employee.html')
    
# @login_required
def profile(request):
    return render(request, 'profile.html')

# @login_required
def offers(request):
    return render(request, 'accounts/oferte.html')

def logout_view(request):
    logout(request)
    return redirect('/')
