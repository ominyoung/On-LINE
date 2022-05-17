from django.urls import path

from route import views

app_name = "route"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]