from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView


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