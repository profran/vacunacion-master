from django.shortcuts import render, redirect
from vacunacion.models import Dose


# Create your views here.

def Home(request):
    if (request.user.is_authenticated):
        if (not request.user.is_medic):
            return render(request, 'webpage/home.html', {'children': request.user.carnets.all()})
        else:
            return (home_medic(request))
    else:
        return redirect('/accounts/login')


def home_medic(request):
    return render(request, 'webpage/medic.html', {'vaccinations': request.user.doses.all()[:30:-1]})
