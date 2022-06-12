import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ResultForm, MemoForm
from .models import ResultModel, MemoModel


def index(request):
    return render(request, 'route/result.html')
    #return render(request, 'route/CustomPage1.html')

# 맞춤형 페이지
def first(request):
    return render(request, 'route/CustomPage1.html')
def second(request):
    return render(request, 'route/CustomPage2.html')
def third(request):
    return render(request, 'route/CustomPage3.html')
def index_result(request):
    return render(request, 'route/CustomResult.html')


def result(request):
    if request.method == "POST":
        result_renewal_form = ResultForm(request.POST)
        if result_renewal_form.is_valid():
            result_renewal_form.save()
            print(result_renewal_form.cleaned_data)
            day = result_renewal_form.cleaned_data.get('day')
            where = result_renewal_form.cleaned_data.get('where')
            print(day, where)
            memo_list = MemoModel.objects.filter(plan_pk=1) # 일정생성 pk=1로 하드코딩
    else:
        result_renewal_form = ResultForm()
        obj = ResultModel.objects.last()
        day = obj.day
        where = obj.where
        memo_list = MemoModel.objects.filter(plan_pk=1)  # 일정생성 pk=1로 하드코딩
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