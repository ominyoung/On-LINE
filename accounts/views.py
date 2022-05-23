from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import ProfileCreationForm
from accounts.models import Profile


def hello_world(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('accounts:hello_word'))
    else:
        return render(request, 'accounts/main.html')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:hello_world')
    template_name = 'accounts/signup.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'profile/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:hello_world')
    template_name = 'profile/update.html'


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accounts:hello_world')
    template_name = 'profile/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accounts:hello_world')
    template_name = 'profile/info_update.html'
