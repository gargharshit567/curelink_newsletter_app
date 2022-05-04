from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from .models import Topic
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def subscribeUser(request):

    try:
        email = request.data['email']
        topics = request.data['topics']

        for topic in topics:
            if not Topic.objects.filter(topic = topic):
                Topic.objects.create(topic=topic)
        
        for i in Topic.objects.all():
            print(i)
    except Exception as e:
        print(e)
        return JsonResponse({
        'status': 'failed',
        'code': 500,
        })

    return JsonResponse({
        'status': 'succeded',
        'code': 200,
        })
