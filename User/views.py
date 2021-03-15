from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

@login_required
def home(request):
    return render(request, 'User/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can login now')
            return redirect('home')

    else:
        form = UserRegisterForm(request.POST)

    return render(request, 'User/register.html', {'form' : form})




