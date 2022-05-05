from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ValidationError
from django.http import JsonResponse
from .models import Topic
from django.conf import settings
from django.core.mail import send_mail
from .serializers import ContentSerializer, TopicSerializer
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createContent(request):

    content = ContentSerializer(data = request.data)
    content.is_valid()
    if content.errors:
        return JsonResponse({
                    'status': 'failed',
                    'message': content.errors,
                    'code': 500,
                 })

    content.save()
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