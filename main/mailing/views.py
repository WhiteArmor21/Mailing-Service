from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers.mailing import *
from .models import Mailing, Message
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
import requests


class RegistrationView(APIView):
    """View for registration new mailing"""
    permission_classes = (
        AllowAny,
    )
    request_body = MailingCreateSerializer
    serializer_class = MailingCreateSerializer

    def post(self, request, format=None):
        obj = MailingCreateSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response({'message': 'Ok'})


class GetMailingInfoView(APIView):
    """View for detailed info about mailings"""
    def get(self, request):
        queryset = Mailing.objects.all()
        serializer = MailingDetailSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)


class MailingAPIView(RetrieveUpdateDestroyAPIView):
    """View for Retrieving, Updating or Destroying mailings"""
    serializer_class = MailingDetailSerializer
    lookup_field = "id"
    queryset = Mailing.objects.all()


class MessageAPIView(APIView):
    """View for message info filtered by mailing"""
    permission_classes = (
        AllowAny,
    )

    request_body = MessageDetailSerializer
    serializer_class = MessageDetailSerializer

    def get(self, request, id: int):
        queryset = Message.objects.filter(mailing=id)
        serializer = MessageDetailSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)


class SendMessageAPI(CreateAPIView):
    """View that create new message, upload it to the server and add it to db"""
    serializer_class = MessageDetailSerializer
    permission_classes = [AllowAny]

    def post(self, request, id: int, *args, **kwargs):
        mailing_object = Mailing.objects.get(id=id)
        mailing_object.counter += 1
        mailing_object.save()
        obj = MessageDetailSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        id = obj.data.get('id')
        r = requests.post('https://probe.fbrq.cloud/docs#/send/%s' % id, data=obj.data)
        print(r.status_code)
        
        return Response({'message': 'Ok'})




