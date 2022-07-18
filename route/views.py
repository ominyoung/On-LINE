import requests
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

from .forms import ResultForm, MemoForm, PlanForm
from .models import ResultModel, MemoModel, PlanModel


def index(request):
    # 기상청 api
    url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'
    params = {'serviceKey': 'bWG0fEz3JXziaxVbvDmZy9L97AdOHLEF7FrSPGynfDVMsrYAFF5NjMWTgSnhS2I70i7ziWy6QWPMxdQ3eSlLFA==',
              'pageNo': '1',
              'numOfRows': '10',
              'dataType': 'JSON',
              'regId': '11G00000',
              'tmFc': '202207181800'}

    response = requests.get(url, params=params)
    # 3일뒤 오전 날씨
    print(response.json().get('response').get('body').get('items').get('item')[0].get('wf3Am'))
    return render(request, 'route/result.html')


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
        memo_list = MemoModel.objects.filter(Q(plan_pk=None)&Q(username=request.user))
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