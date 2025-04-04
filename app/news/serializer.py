from rest_framework import serializers
from app.news.models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "description", "left_image", "middle_image", "dextral_image"]

class DailyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNews
        fields = ["id", "title", "description", "image"]

class EventsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsNews
        fields = ["id", "title", "description", "image", "time"]

class BookArrivalSerializer(serializers.ModelSerializer):
    open_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = BookArrival
        fields = ['id', 'title', 'author', 'description', 'image', 'link', 'open_url', 'download_url']

    def get_open_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.file.url) if request else obj.file.url

    def get_download_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/v1/news/book-arrivals/{obj.id}/download/') if request else f'/api/v1/news/book-arrivals/{obj.id}/download/'

class MediaCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCoverage
        fields = ['title', 'coverage_period', 'description', 'image']
        