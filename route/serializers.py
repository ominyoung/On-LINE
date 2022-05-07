from dataclasses import fields
from rest_framework import serializers
from .models import Privacy

class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Privacy
        fields = (
            'id',
            'password',
            'name',
            'phone_num',
            'age'
        )