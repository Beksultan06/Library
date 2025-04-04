from rest_framework import serializers
from app.base.models import Logo, Catalogs_ElectronicLibrary, WeOfferViewing, Partners, ReadingRating, BooksRating
from django.conf import settings


#Саидахмад
class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"
        
    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.logo_images.all()

        image_urls = []
        for image in images:
            if image.image:
                image_url = image.image.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.image}"
                image_urls.append(image_url)

        return image_urls 

class Catalogs_ElectronicLibrary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogs_ElectronicLibrary
        fields = "__all__"



#Алишер
class WeOfferViewingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeOfferViewing
        fields = '__all__'
        

class PartnersSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = Partners
        fields = '__all__'
        
    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.partner_images.all()

        image_urls = []
        for image in images:
            if image.image:
                image_url = image.image.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.image}"
                image_urls.append(image_url)

        return image_urls

        
class ReadingRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingRating
        fields = '__all__'
        
class BooksRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksRating
        fields = '__all__'
