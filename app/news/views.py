from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from django.http import FileResponse
from app.news.pagination import NewsPagination
from app.news.models import *
from app.news.serializer import *

# Create your views here.

class NewsAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination

class DailyNewsAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = DailyNews.objects.all()
    serializer_class = DailyNewsSerializer

class EventsNewsAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = EventsNews.objects.all()
    serializer_class = EventsNewsSerializer

class BookArrivalAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = BookArrival.objects.all()
    serializer_class = BookArrivalSerializer

    @action(detail=True, methods=['get'], url_path='download')
    def download(self, request, pk=None):
        book_arrival = self.get_object()
        file_path = book_arrival.file.path
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=book_arrival.file.name)
        return response

class MediaCoverageAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = MediaCoverage.objects.all()
    serializer_class = MediaCoverageSerializer