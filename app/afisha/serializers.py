from rest_framework import serializers

from .models import Afisha, Events

class AfishaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afisha
        fields = ['id', 'title', 'image', 'description', 'title_2']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'time_of_the_event', 'title', 'description', 'image', 'details_link']