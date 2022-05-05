from rest_framework import serializers
from .models import Subscriber
from content.models import Topic
class SubscriberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    topics = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), many=True)
    class Meta:
        model = Subscriber
        fields= ['email','topics']

