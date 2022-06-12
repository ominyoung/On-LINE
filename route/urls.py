from django.urls import path

from route import views

app_name = "route"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('memo/', views.memo, name='memo'),
    path('map/', views.map, name='map'),



    # 맞춤형 페이지
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('index_result/', views.index_result, name='index_result'),
]