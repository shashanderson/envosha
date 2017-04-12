from django.shortcuts import render

# Create your views here.

# log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def login(request):
    return render(request, "form_list.html")


def form_list(request):
    return render(request, 'cem_reports/form_list.html', {})


def form_validation(request):
    return render(request, 'cem_reports/form_validation.html', {})


def form(request):
    return render(request, 'cem_reports/form.html', {})


def login_page(request):
    return render(request, 'cem_reports/login.html', {})
