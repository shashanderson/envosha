from django.shortcuts import render

# Create your views here.


def form_list(request):
    return render(request, 'cem_reports/form_list.html', {})
