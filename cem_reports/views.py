from django.shortcuts import render

# Create your views here.


def form_list(request):
    return render(request, 'cem_reports/form_list.html', {})


def form_validation(request):
    return render(request, 'cem_reports/form_validation.html', {})


def form(request):
    return render(request, 'cem_reports/form.html', {})



