from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import hello_world, AccountCreateView, ProfileCreateView, AccountDetailView, AccountUpdateView, \
    ProfileUpdateView, personal, personal_detail

app_name = "accounts"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('profile/', ProfileCreateView.as_view(), name='profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),

    path('pers_route/', personal, name='personal'),
    path('pers_route/<int:pk>', personal_detail, name='personal_detail'),
]