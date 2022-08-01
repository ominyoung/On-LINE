from datetime import datetime

import requests
import json
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

from .forms import MemoForm, PlanForm
from .models import MemoModel, PlanModel


def index(request):
    # 기상청 중기 api
    # 현재 날짜 시간을 0600, 1800만 받아올수 있음 예시) 202207190600
    dt_now = datetime.now()
    if dt_now.hour < 6:
        dt_aj = datetime.strftime(dt_now - datetime.timedelta(1), '%Y-%m-%d')
        tmFc = str(datetime.strftime(dt_now - datetime.timedelta(1), '%Y%m%d'))+"1800"
    elif 6 <= dt_now.hour < 18:
        dt_aj = datetime.strftime(dt_now, '%Y-%m-%d')
        tmFc = str(datetime.strftime(dt_now, '%Y%m%d'))+"0600"
    else:
        dt_aj = datetime.strftime(dt_now, '%Y-%m-%d')
        tmFc = str(datetime.strftime(dt_now, '%Y%m%d'))+"1800"
    url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'
    params = {'serviceKey': 'bWG0fEz3JXziaxVbvDmZy9L97AdOHLEF7FrSPGynfDVMsrYAFF5NjMWTgSnhS2I70i7ziWy6QWPMxdQ3eSlLFA==',
              'pageNo': '1',
              'numOfRows': '10',
              'dataType': 'JSON',
              'regId': '11G00000', # 제주도
              'tmFc': tmFc}

    # 기상청 단기 api
    dt_short_now = datetime.now()
    if dt_short_now.hour < 5:
        dt_short_aj = str(datetime.strftime(dt_short_now - datetime.timedelta(1), '%Y%m%d'))
    else:
        dt_short_aj = str(datetime.strftime(dt_short_now, '%Y%m%d'))

    url_short = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    params_short = {'serviceKey': 'bWG0fEz3JXziaxVbvDmZy9L97AdOHLEF7FrSPGynfDVMsrYAFF5NjMWTgSnhS2I70i7ziWy6QWPMxdQ3eSlLFA==',
              'pageNo': '1', 'numOfRows': '1000', 'dataType': 'JSON', 'base_date': dt_short_aj, 'base_time': '0500',
              'nx': '53', 'ny': '38'}  # nx, ny : 제주도 일도동,이도동

    # tmFc에 현재 날짜 str로 더해서 넣기
    response = requests.get(url, params=params)
    response_short = requests.get(url_short, params=params_short)
    items = response_short.json().get('response').get('body').get('items').get('item')

    sky = []
    pty = []

    for i in items:
        sky_dict = {}
        pty_dict = {}
        if i["category"] == "SKY":
            if i["fcstTime"] == '0600' or i["fcstTime"] == "1200" or i["fcstTime"] == "1800":
                datestring = datetime.strptime(i["fcstDate"], "%Y%m%d")
                sky_dict["fcstDate"] = datetime.strftime(datestring, "%Y/%m/%d")
                sky_dict["fcstTime"] = i["fcstTime"]
                sky_dict["fcstValue"] = i["fcstValue"]
                sky.append(sky_dict)
        if i["category"] == "PTY":
            if i["fcstTime"] == '0600' or i["fcstTime"] == "1200" or i["fcstTime"] == "1800":
                #pty_dict["fcstDate"] = i["fcstDate"]
                #pty_dict["fcstTime"] = i["fcstTime"]
                pty_dict["fcstValue"] = i["fcstValue"]
                pty.append(pty_dict)

    # 3일뒤 오전 날씨
    return render(request, 'route/result.html',
                  {'time': dt_aj,    # 중기 api 날짜
                   'weather': response.json().get('response').get('body').get('items').get('item')[0],  # 중기 api 날짜
                   'sky': sky,       # 단기 api 날씨 [{날짜, 시간, 날씨}]
                   'pty': pty,       # 단기 api 날씨 [{날짜, 시간, 강수}]
                   })


def result(request):
    # datepicker가 있는 result.html 에서 넘어올때
    if request.method == "POST" and request.POST.get('startdate') != None:
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')

        day = int(request.POST.get('day'))
        where = request.POST.get('where')

        # 세션 값 설정하기
        request.session['startdate'] = startdate
        request.session['enddate'] = enddate
        request.session['day'] = day
        request.session['where'] = where
    # map.html에서 장소를 추가하고 day.html로 넘어올 때
    elif request.method == "POST" and request.POST.get('startdate') == None:
        # result.html에서 session으로 넘긴 값
        startdate = request.session['startdate']
        enddate = request.session['enddate']
        day = request.session['day']
        where = request.session['where']
        # map.html에서 넘겨받은 json 값 출력
        json_object = json.loads(request.body)
        print(json_object)
    else:
        startdate = request.session['startdate']
        enddate = request.session['enddate']
        day = request.session['day']
        where = request.session['where']

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


# 맞춤형 페이지
def custom(request):
    return render(request, 'route/CustomPage.html')


def spot(request):
    return render(request, 'route/spot.html')

# 스팟페이지 상세
def detail_spot(request):
    return render(request, 'route/detail_spot.html')