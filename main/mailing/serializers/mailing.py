from rest_framework import serializers
from ..models import Mailing, Message


class MailingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = [
            'start_time',
            'message',
            'mobile_operator',
            'tag',
            'completion_time',
        ]


class MailingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = fields = '__all__'


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
