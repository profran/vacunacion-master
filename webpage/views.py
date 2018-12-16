from django.shortcuts import render, redirect
# Create your views here.

def Home(request):
    if (request.user.is_authenticated):
        if (not request.user.is_medic):
            return render(request, 'webpage/home.html', {'children': request.user.childs.all()})
    else:
        return redirect('/accounts/login')
