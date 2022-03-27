from rest_framework import serializers
from ..models import Client


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'phone_number',
            'mobile_operator',
            'tag',
            'client_time_zone',
        ]


def validate_phone_number(self, value):
    error = False
    try:
        Client.objects.get(phone_number=value)
        error = True
    except:
        pass

    if error:
        raise serializers.ValidationError('This phone_number is already exists')

    return value

    def save(self, **kwargs):
        profile = Client()
        profile.phone_number = self.validated_data['phone_number']
        profile.mobile_operator = self.validated_data['mobile_operator']
        profile.tag = self.validated_data['tag']
        profile.client_time_zone = self.validated_data['client_time_zone']
        profile.save()
        return profile