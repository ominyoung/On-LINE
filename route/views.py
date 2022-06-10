import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ResultForm, MemoForm
from .models import ResultModel, MemoModel


def index(request):
    return render(request, 'route/result.html')


def result(request):
    if request.method == "POST":
        result_renewal_form = ResultForm(request.POST)
        if result_renewal_form.is_valid():
            result_renewal_form.save()
            print(result_renewal_form.cleaned_data)
            day = result_renewal_form.cleaned_data.get('day')
            where = result_renewal_form.cleaned_data.get('where')
            print(day, where)
            memo_list = MemoModel.objects.filter(plan_pk=1)
    else:
        result_renewal_form = ResultForm()
        obj = ResultModel.objects.last()
        day = obj.day
        where = obj.where
        memo_list = MemoModel.objects.get(plan_pk=1)
    return render(request, 'route/day.html', {'where': where, 'days': range(day), 'memo_lists': memo_list})


def memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route:result')
    else:
        form = MemoForm()
    return render(request, 'route/memo_form.html', {'form': form})

def map(request):
    return render(request, 'route/map.html')