from django.urls import path
from .views import *

urlpatterns = [
    path('', GetMailingInfoView.as_view()),
    path('add/', RegistrationView.as_view()),
    path('<int:id>/', MailingAPIView.as_view()),
    path('<int:id>/messages/', MessageAPIView.as_view()),
    path('<int:id>/send/', SendMessageAPI.as_view()),
    ]
