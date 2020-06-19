from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import PostForm
from .forms import MakeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':

     if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
def coa(request):
    form = MakeForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
          form.save()
          form = MakeForm()
    return render(request, 'coaching.html', {'form': form})


@login_required
def profile(request):
    form = PostForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            form = PostForm()
    return render(request, 'profile.html', {'form': form})