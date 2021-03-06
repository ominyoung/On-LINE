from django.urls import path

from route import views

app_name = "route"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('memo/', views.memo, name='memo'),
    path('map/', views.map, name='map'),
    path('schedule_save/', views.schedule_save, name='schedule_save'),
    path('schedule_del/', views.schedule_del, name="schedule_del"),
]