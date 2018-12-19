from django.shortcuts import render, redirect
from .forms import VaccinationAddForm
from .models import Carnet, Vaccine, Vaccination, Dose
from .forms import CreateCarnetForm
from django.db.models import Q


# Create your views here.

def create_carnet(request):
    if request.method == 'POST':
        form = CreateCarnetForm(data=request.POST)
        if (form.is_valid()):
            carnet = Carnet(user=request.user, name=form.cleaned_data.get('name'),
                            last_name=form.cleaned_data.get('last_name'),
                            dni=form.cleaned_data.get('dni'),
                            born_date=form.cleaned_data.get('born_date'))
            carnet.save()
            return redirect('/')
    else:
        form = CreateCarnetForm()
        print("xdddd")
    return render(request, 'accounts/form.html', {'title': 'Crear carnet', 'form': form})


def get_dni(request):
    if request.method == 'POST':
        form = VaccinationAddForm(data=request.POST)
        if (form.is_valid()):
            vaccination = Vaccination.objects.get_or_create()
            return redirect('/')
    else:
        form = VaccinationAddForm()
    return render(request, 'accounts/form.html', {'title': 'Iniciar sesion', 'form': form})


def add_vaccination(request, query):
    if (request.user.is_medic):
        if request.method == 'POST':
            print(request.POST)
            carnet = Carnet.objects.get(id=request.POST.get('carnet'))
            vaccine = Vaccine.objects.get(id=request.POST.get('vaccine'))
            vaccination = Vaccination.objects.get_or_create(carnet=carnet, vaccine=vaccine)[0]
            date = request.POST.get('date_year') + '-' + request.POST.get('date_month') + '-' + request.POST.get('date_day')
            next_dose_date = request.POST.get('next_dose_year') + '-' + request.POST.get(
                'next_dose_month') + '-' + request.POST.get('next_dose_day')
            dose = Dose(vaccination=vaccination, type=request.POST.get('type'), medic=request.user,
                        date=date, next_dose=next_dose_date, batch_number=request.POST.get('batch_number'))
            dose.save()
            return redirect('/')
        else:
            queryset = Carnet.objects.prefetch_related('user').filter(
                Q(user__dni=query) | Q(user__username=query))
            print(queryset)
            form = VaccinationAddForm(queryset=queryset)
        return render(request, 'accounts/form.html', {'title': 'Añadir vacuna', 'form': form})
    else:
        return redirect('/')

def carnet_detail(request, carnet_id):
    if (request.user.is_authenticated):
        if (request.user.is_medic):
            try:
                carnet = Carnet.objects.get(id=carnet_id)
                return render(request, 'webpage/carnet_detail.html', {'carnet': carnet})
            except:
                return redirect('/')
        else:
            try:
                carnet = Carnet.objects.get(user=request.user, id=carnet_id)
                return render(request, 'webpage/carnet_detail.html', {'carnet': carnet})
            except:
                return redirect('/')
