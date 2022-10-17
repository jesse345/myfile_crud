from rest_framework import serializers
from profile_app.models import MProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MProfile
        fields = '__all__' 

