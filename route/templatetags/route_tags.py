from django import template
import datetime

register = template.Library()

@register.simple_tag
def route_date(startdate, day):
    startdate = list(map(int, startdate.split('-')))
    date = datetime.datetime(startdate[0], startdate[1], startdate[2])
    arr = []
    for i in range(len(day)):
        today = date + datetime.timedelta(days=i)
        arr.append(today.strftime('%Y-%m-%d'))
    print(arr)
    return arr