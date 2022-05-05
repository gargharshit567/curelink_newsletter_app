from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ValidationError
from django.http import JsonResponse
from .models import Topic
from subscribers.models import Subscriber
from django.conf import settings
from .serializers import ContentSerializer, TopicSerializer
from datetime import datetime, timedelta
from curelink.celery import send_email_to_reciepent
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createContent(request):
    try:
        content = ContentSerializer(data = request.data)
        content.is_valid()
        if content.errors:
            return JsonResponse({
                        'status': 'failed',
                        'message': content.errors,
                        'code': 500,
                    })

        reciepents = Subscriber.objects.filter(topics= content.validated_data['topic'].topic)
        if reciepents:
            print("recieved request")
            text_to_mail = content.validated_data['content_text']
            subject_of_mail = content.validated_data['content_desc']
            arr = []
            for reciepent in reciepents:
                arr.append(reciepent.email)
            send_email_to_reciepent.apply_async((text_to_mail,subject_of_mail,arr), eta = content.validated_data['time'])
        else:
            print(reciepents)
        content.save()
    except Exception as e:
        print(e)
        return JsonResponse({
                    'status': 'failed',
                    'message': e,
                    'code': 200,
                 }) 
    return JsonResponse({
                    'status': 'success',
                    'code': 200,
                 })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTopic(request):
    try:
        topic = TopicSerializer(data = request.data)
        topic.is_valid()

        if topic.errors:
            return JsonResponse({
                        'status': 'failed',
                        'message': topic.errors,
                        'code': 500,
                    })
    except Exception as e:
        print(e)
        return JsonResponse({
                    'status': 'failed',
                    'message': e,
                    'code': 500,
                 })

    return JsonResponse({
                    'status': 'success',
                    'code': 200,
                 })