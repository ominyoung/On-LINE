import datetime

import requests
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

from .forms import ResultForm, MemoForm, PlanForm
from .models import ResultModel, MemoModel, PlanModel


def index(request):
    # 현재 날짜 시간을 0600, 1800만 받아올수 있음 예시) 202207190600
    dt_now = datetime.datetime.now()
    if dt_now.hour < 6:
        dt_aj = datetime.datetime.strftime(dt_now - datetime.timedelta(1), '%Y%m%d')
        tmFc = str(dt_aj)+"1800"
    elif 6 <= dt_now.hour < 18:
        dt_aj = datetime.datetime.strftime(dt_now, '%Y%m%d')
        tmFc = str(dt_aj)+"0600"
    else:
        dt_aj = datetime.datetime.strftime(dt_now, '%Y%m%d')
        tmFc = str(dt_aj)+"1800"
    #  + dt_now.day
    # 기상청 api
    url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'
    params = {'serviceKey': 'bWG0fEz3JXziaxVbvDmZy9L97AdOHLEF7FrSPGynfDVMsrYAFF5NjMWTgSnhS2I70i7ziWy6QWPMxdQ3eSlLFA==',
              'pageNo': '1',
              'numOfRows': '10',
              'dataType': 'JSON',
              'regId': '11G00000', # 제주도
              'tmFc': tmFc}
    # tmFc에 현재 날짜 str로 더해서 넣기
    response = requests.get(url, params=params)
    # 3일뒤 오전 날씨
    return render(request, 'route/result.html',
                  {'time': dt_aj,
                   'weather': response.json().get('response').get('body').get('items').get('item')[0]
                   })


def result(request):
    if request.method == "POST":
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')

        day = int(request.POST.get('day'))
        where = request.POST.get('where')


        # 일전에 임시로 저장해놓은 메모 불러오기
        memo_list = MemoModel.objects.filter(Q(plan_pk=None) & Q(username=request.user))


    return render(request, 'route/day.html',
                  {
                      'startdate': startdate,
                      'enddate': enddate,
                      'where': where,
                      'days': range(day),  # 일정기간
                      'memo_lists': memo_list
                  })

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