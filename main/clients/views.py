from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import Client
from .serializers.user_request import UserProfileSerializer

class GetClientInfoView(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = UserProfileSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)


class ClientDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    lookup_field = "id"
    queryset = Client.objects.all()


class RegistrationView(APIView):
    '''
    User registration.
    -----------------
    '''

    permission_classes = (
        AllowAny,
    )

    request_body = UserProfileSerializer
    serializer_class = UserProfileSerializer

    def post(self, request, format=None):
        obj = UserProfileSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response({'message': 'Ok'})
