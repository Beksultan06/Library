from rest_framework import serializers
from app.professional_activity.models import Activity


class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "title",
            "description",
            "links",
            'description_details',

        ]
