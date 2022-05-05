from rest_framework import serializers
from .models import *
class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields= '__all__'
    
class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields= '__all__'
