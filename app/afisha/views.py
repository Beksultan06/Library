# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


from app.afisha.models import Events, Afisha
from app.afisha.serializers import EventsSerializer, AfishaSerializer


class AfishaMixins(GenericViewSet,
                    mixins.ListModelMixin):
   
    queryset = Afisha.objects.all()
    serializer_class = AfishaSerializer

class EventsMixins(GenericViewSet,
                    mixins.ListModelMixin):
   
    queryset = Events.objects.all()
    serializer_class = EventsSerializer    