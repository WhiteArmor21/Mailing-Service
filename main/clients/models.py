from django.db import models

class Client(models.Model):
    phone_number = models.CharField(max_length=12, unique=True)
    mobile_operator = models.CharField(max_length=3)
    tag = models.CharField(max_length=50, blank=True)
    client_time_zone = models.CharField(max_length=30)
