from django.shortcuts import render
from app.professional_activity.serializers import Activity
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.professional_activity.serializers import ActivitySerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class ActivityViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['title']
    filterset_fields = ["title"]
