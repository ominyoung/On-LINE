from django import template
import datetime

register = template.Library()

@register.simple_tag
def route_date(startdate, day):
    startdate = list(map(int, startdate.split('-')))
    date = datetime.datetime(startdate[0], startdate[1], startdate[2])
    days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    arr = [] #날짜 담을 리스트
    for i in range(len(day)):
        today = date + datetime.timedelta(days=i)
        arr.append(today.strftime('%Y-%m-%d')+" "+days[today.weekday()])
    return arr