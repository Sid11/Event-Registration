from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Event #Register


class EventSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'attendees', 'is_public', 'creator']


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'events']

#
# class RegisterSerializer(serializers.ModelSerializer):
#     register = EventSerializer()
#
#     class Meta:
#         model = Register
#         fields = ['username']
