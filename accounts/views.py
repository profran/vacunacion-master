from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpUserForm, SignUpMedicForm, CreateOwnerForm
from .models import MedicProfile, CarnetOwner


# Create your views here.

def signup_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpUserForm()
    return render(request, 'accounts/form.html', {'title': 'Registrarse como Usuario', 'form': form})


def signup_medic(request):
    if request.method == 'POST':
        form = SignUpMedicForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            medic_profile = MedicProfile(user=user, plate=form.cleaned_data.get('plate'))
            medic_profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpMedicForm()
    return render(request, 'accounts/form.html', {'title': 'Registrarse como Medico', 'form': form})


def login_account(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {'title': 'Iniciar sesion', 'form': form})


def logout_account(request):
    logout(request)
    return redirect('/accounts/login')


def create_owner(request):
    if request.method == 'POST':
        form = CreateOwnerForm(data=request.POST)
        if (form.is_valid()):
            child = CarnetOwner(user=request.user, name=form.cleaned_data.get('name'),
                                last_name=form.cleaned_data.get('last_name'),
                                dni=form.cleaned_data.get('dni'),
                                born_date=form.cleaned_data.get('born_date'))
            child.save()
            return redirect('/')
    else:
        form = CreateOwnerForm()
    return render(request, 'accounts/form.html', {'title': 'Registrar hijo/a', 'form': form})
