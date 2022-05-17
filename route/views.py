import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ResultForm


def index(request):
    return render(request, 'route/result.html')


def result(request):
    if request.method == "POST":
        result_renewal_form = ResultForm(request.POST)
        if result_renewal_form.is_valid():
            result_renewal_form.save()
            day = result_renewal_form.cleaned_data.get('day')
            where = result_renewal_form.cleaned_data.get('where')
    else:
        result_renewal_form = ResultForm()
    return render(request, 'route/day.html', {'day': day, 'where': where})






