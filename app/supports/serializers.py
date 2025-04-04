from rest_framework import serializers
from .models import LibrarySupport, LibraryValue, LibraryTitles

class LibrarySupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrarySupport
        fields = ['title', 'description', 'image',]

class LibraryValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryValue
        fields = ['title', 'icon', 'short_description', 'full_description']

class LibraryTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryTitles
        fields = ['title_1', 'title_2', 'title_3',  'left_description', 'right_description']