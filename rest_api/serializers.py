from rest_framework import serializers
from accounts.models import Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'nickname', 'message')