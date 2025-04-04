from rest_framework import serializers
from app.page_for_readers.models import Banner, Graphic_work, Titles


class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            "title",
            "description",
            "links",
            'image',

        ]

# class BannerSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Banner
#         fields = [
#             "title",
#             "description",
#             "image",
#             'links'
#         ]

class Graphic_workSerializers(serializers.ModelSerializer):
    class Meta:
        model = Graphic_work
        fields = [
            "title",
            "description",
        ]
class TitlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = [
           "work",
        "citizens",
        "hall",
        'readers',
        'books'
        ]