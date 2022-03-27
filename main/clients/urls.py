from django.urls import path
from .views import GetClientInfoView, ClientDetailAPIView, RegistrationView


urlpatterns = [
    path('', GetClientInfoView.as_view()),
    path('<int:id>/', ClientDetailAPIView.as_view()),
    path('add/' ,RegistrationView.as_view()),
]