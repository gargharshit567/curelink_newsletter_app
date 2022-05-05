from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from content.models import Topic
from django.conf import settings
from django.core.mail import send_mail
from .serializers import SubscriberSerializer
# Create your views here.


   
#send_simple_message()

@api_view(['POST'])
@permission_classes([AllowAny])
def subscribeUser(request):

    try:
        subscriber= SubscriberSerializer(data= request.data)
        subscriber.is_valid()
        if subscriber.errors:
            return JsonResponse({
                    'status': 'failed',
                    'message': subscriber.errors,
                    'code': 500,
                 })

        subscriber.save()
        
    except Exception as e:
        print(e)
        return JsonResponse({
        'status': 'failed',
        'code': 500,
        })

    return JsonResponse({
        'status': 'succeded',
        'message': 'succesfully subscribed',
        'code': 200,
        })
