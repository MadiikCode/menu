from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Customer
from .forms import CustomerRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu_list')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customers/register.html', {'form': form})

def profile(request):
 #   customer = request.user.customer
 #   return render(request, 'customers/profile.html', {'customer': customer})

    return render(request, 'profile.html')
