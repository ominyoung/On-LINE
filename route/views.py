from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

from .forms import ResultForm, MemoForm, PlanForm
from .models import ResultModel, MemoModel, PlanModel


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
            day = result_renewal_form.cleaned_data.get('day')
            where = result_renewal_form.cleaned_data.get('where')
            print(day, where)
            memo_list = MemoModel.objects.filter(Q(plan_pk=None)&Q(username=request.user))
            # 일정생성할때 새로 만들어지는 메모, plan 테이블에 아직 저장 안됨
    else:
        result_renewal_form = ResultForm()
        obj = ResultModel.objects.last()
        day = obj.day
        where = obj.where
        memo_list = MemoModel.objects.filter(plan_pk=None)
        # 일정생성할때 새로 만들어지는 메모, plan 테이블에 아직 저장 안됨
    return render(request, 'route/day.html', {'where': where, 'days': range(day), 'memo_lists': memo_list})

# 메모 저장
def memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user
            post.save()
            return redirect('route:result')
    else:
        form = MemoForm()
    return render(request, 'route/memo_form.html', {'form': form})

def map(request):
    return render(request, 'route/map.html')


# 일정페이지에서 close를 누를때 임시저장되었던 메모 삭제
def schedule_del(request):
    MemoModel.objects.filter(plan_pk=None).delete()
    return redirect('accounts:hello_world')


# 일정페이지에서 저장을 누를때 임시저장되었던 메모 plan 테이블로 저장
def schedule_save(request):
    if request.method == "POST":
        # 새로운 id의 plan을 생성
        new_plan_form = PlanForm(request.POST)

        if new_plan_form.is_valid():
            # 수정기능이 완료되면 save() 열거임
            new_plan_form.save()
            lastest_plan = PlanModel.objects.last()
            # memo 테이블에 plan_pk 칼럼이 none이였는데, 새로운 plan으로 update
            memo_list = MemoModel.objects.filter(plan_pk=None)
            memo_list.update(plan_pk=lastest_plan)

    return redirect('accounts:hello_world')
    #return render(request, 'accounts/main.html')