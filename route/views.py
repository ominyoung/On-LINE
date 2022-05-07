from django.shortcuts import render

# Create your views here.


#Serializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from route.models import Privacy
from .serializers import PrivacySerializer
import json

class PrivacyCreateReadView(ListCreateAPIView):
    queryset = Privacy.objects.all()
    serializer_class = PrivacySerializer
