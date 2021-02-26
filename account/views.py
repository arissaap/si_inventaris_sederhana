from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from account.forms import RegistrasiForm

def logout_view(request):
    logout(request)
    return redirect('/')

def daftar(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method == 'POST':
        form = RegistrasiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Daftar!')
            return redirect('login')
    else:
        form = RegistrasiForm()

    data = {}
    data['form'] = form
    data['state'] = 'Daftar'
    return render(request, 'login.html', data)