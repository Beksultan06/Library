from rest_framework import serializers
from .models import OurProjects, MainProjects, AmericanCorner

class OurProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProjects
        fields = ['title', 'description', 'image', 'created_at']

class MainProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProjects
        fields = ['title', 'description', 'image', 'created_at']

class AmericanCornerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmericanCorner
        fields = ['title', 'description', 'image', 'created_at']