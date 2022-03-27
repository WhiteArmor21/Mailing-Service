from django.utils import timezone
from django.db import models
from clients.models import Client


class Mailing(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=500)
    mobile_operator = models.CharField(max_length=3, blank=True)
    tag = models.CharField(max_length=50, blank=True)
    completion_time = models.DateTimeField()
    counter = models.IntegerField(default=0, null=True)


class Message(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='+')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
