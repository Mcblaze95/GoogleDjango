from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




def home1(request):
    return render(request, "home1.html")

def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def index(request):
    return render(request, 'index.html')