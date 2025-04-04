from django.shortcuts import render
from app.page_for_readers.serializers import Banner, Graphic_work, Titles
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.page_for_readers.serializers import BannerSerializers, Graphic_workSerializers, TitlesSerializers

# Create your views here.

class BannerViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers


class Graphic_workViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Graphic_work.objects.all()
    serializer_class = Graphic_workSerializers


class TitlesViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializers
