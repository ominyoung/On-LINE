from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import ProfileCreationForm
from accounts.models import Profile
from route.models import PlanModel, PlaceModel, MemoModel


def main(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('main'))
    else:
        return render(request, 'accounts/main.html')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'accounts/signup.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'profile/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'profile/update.html'


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('main')
    template_name = 'profile/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        # print(temp_profile)
        temp_profile.save()
        return super().form_valid(form)
# def profile_create(request):
#     if request.method == 'POST':
#         data = {
#             'user': User.objects.get(username=request.USER),
#             'image': request.FILES.get('image'),
#             'nickname': request.POST.get('nickname'),
#             'message': request.POST.get('message'),
#         }
#         profile = Profile.objects.create(**data)
#
#         return render(request, 'profile/create.html', profile)
#     else:
#         return render(request, 'profile/create.html')


class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('main')
    template_name = 'profile/info_update.html'


# 개인 일정 모음 페이지
def personal(request):
    pers_routes = PlanModel.objects.filter(username=request.user)
    return render(request, 'route/personal_route.html', {'pers_routes': pers_routes})


# 개인 일정 > 자세히 보기 페이지
def personal_detail(request, pk):
    pers_place_detail = PlaceModel.objects.filter(plan_pk=pk).order_by('count')
    pers_memo_detail = MemoModel.objects.filter(plan_pk=pk).order_by('count')
    pers_plan_detail = PlanModel.objects.filter(pk=pk)
    pers_detail = {
        'pk': pk,
        'pers_place': pers_place_detail,
        'pers_memo': pers_memo_detail,
        'pers_plan': pers_plan_detail,
    }
    return render(request, 'route/personal_route_detail.html', pers_detail)