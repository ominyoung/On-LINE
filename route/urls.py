from django.urls import path

from route import views

from django.conf.urls.static import static
from django.conf import settings

app_name = "route"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('memo/', views.memo, name='memo'),
    path('map/', views.map, name='map'),
    path('schedule_save/', views.schedule_save, name='schedule_save'),
    path('schedule_del/', views.schedule_del, name="schedule_del"),
    # 메모, 지도 update, delete
    path('memo_update/<int:pk>', views.memo_update, name='memo_update'),
    path('memo_delete/<int:pk>', views.memo_delete, name='memo_delete'),
    path('map_delete/<int:pk>', views.map_delete, name='map_delete'),
    path('map_update/<int:pk>', views.map_update, name='map_update'),

    # 맞춤형 페이지
    path('custom/', views.custom, name='custom'),

    # 스팟 페이지
    path('spot/', views.spot, name='spot'),

    #리뷰 페이지
    path('review/', views.review, name='review'),

    #리부 글 쓰기 페이지
    path('write/', views.write, name='write'),

    # 리부 글 보기 페이지
    path('view/', views.view, name='view'),
    path('detail_spot/', views.detail_spot, name='detail_spot'),

    # 리뷰페이지
    path('review/', views.review, name='review'),
    path('view/', views.view, name='view'),
    path('write/', views.write, name='write'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)