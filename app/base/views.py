from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from app.base.serializers import LogoSerializer, Catalogs_ElectronicLibrary_Serializer, WeOfferViewingSerializer, PartnersSerializer, ReadingRatingSerializer, BooksRatingSerializer
from app.base.models import Logo, Catalogs_ElectronicLibrary, WeOfferViewing, Partners, ReadingRating, BooksRating

# Create your views here.

#Саидахмад
class HomeViewSet(GenericViewSet,
                  mixins.ListModelMixin):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class Catalogs_ElectronicLibraryViewSet(GenericViewSet,
                                        mixins.ListModelMixin):
    queryset = Catalogs_ElectronicLibrary.objects.all()
    serializer_class = Catalogs_ElectronicLibrary_Serializer



#Алишер
class WeOfferViewingView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = WeOfferViewing.objects.all()
    serializer_class = WeOfferViewingSerializer
    

class PartnersView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    

class ReadingRatingView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = ReadingRating.objects.all()
    serializer_class = ReadingRatingSerializer
    

class BooksRatingView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = BooksRating.objects.all()
    serializer_class = BooksRatingSerializer
