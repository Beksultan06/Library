import re
from django.db import connection
from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from app.afisha.models import Events
from app.projects.models import MainProjects, AmericanCorner
from app.news.models import DailyNews, EventsNews, BookArrival, MediaCoverage
from app.services.models import Service, ServiceHeader

from app.afisha.serializers import EventsSerializer
from app.projects.serializers import MainProjectsSerializer, AmericanCornerSerializer
from app.news.serializer import DailyNewsSerializer, EventsNewsSerializer, BookArrivalSerializer, MediaCoverageSerializer
from app.services.serializers import ServiceSerializer, ServiceHeaderSerializer


class GlobalSearch(APIView):

    def get(self, request):
        query = request.query_params.get('search', '').strip()

        if not query or len(query) < 3:
            raise ValidationError({"error": "Введите поисковый запрос (минимум 3 символа)"})

        query = self.clean_query(query)

        query_words = query.split()

        if len(query_words) < 1:
            raise ValidationError({"error": "Запрос слишком короткий, введите хотя бы одно слово"})

        paginator = PageNumberPagination()
        paginator.page_size = int(request.query_params.get('page_size', 10))

        is_postgresql = self.is_postgresql()

        events = self.perform_search(query, query_words, Events, is_postgresql)
        main_projects = self.perform_search(query, query_words, MainProjects, is_postgresql)
        american_corners = self.perform_search(query, query_words, AmericanCorner, is_postgresql)
        daily_news = self.perform_search(query, query_words, DailyNews, is_postgresql)
        events_news = self.perform_search(query, query_words, EventsNews, is_postgresql)
        book_arrival = self.perform_search(query, query_words, BookArrival, is_postgresql)
        media_coverage = self.perform_search(query, query_words, MediaCoverage, is_postgresql)
        service = self.perform_search(query, query_words, Service, is_postgresql)
        service_header = self.perform_search(query, query_words, ServiceHeader, is_postgresql)

        combined_results = list(events) + list(main_projects) + list(american_corners) + list(daily_news) + \
                            list(events_news) + list(book_arrival) + list(media_coverage) + list(service) + \
                            list(service_header)

        if len(combined_results) > 100:
            raise ValidationError({"error": "Результатов слишком много, уточните запрос."})

        combined_results = sorted(combined_results, key=lambda x: self.calculate_relevance(x, query), reverse=True)

        paginated_results = paginator.paginate_queryset(combined_results, request)

        data = []
        for result in paginated_results:
            result_data = {}

            if isinstance(result, Events):
                result_data = EventsSerializer(result).data
                result_data['приложения'] = 'Afisha'
            elif isinstance(result, MainProjects):
                result_data = MainProjectsSerializer(result).data
                result_data['приложения'] = 'Projects'
            elif isinstance(result, AmericanCorner):
                result_data = AmericanCornerSerializer(result).data
                result_data['приложения'] = 'Projects'
            elif isinstance(result, DailyNews):
                result_data = DailyNewsSerializer(result).data
                result_data['приложения'] = 'news'
            elif isinstance(result, EventsNews):
                result_data = EventsNewsSerializer(result).data
                result_data['приложения'] = 'news'
            elif isinstance(result, BookArrival):
                result_data = BookArrivalSerializer(result).data
                result_data['приложения'] = 'news'
            elif isinstance(result, MediaCoverage):
                result_data = MediaCoverageSerializer(result).data
                result_data['приложения'] = 'news'
            elif isinstance(result, Service):
                result_data = ServiceSerializer(result).data
                result_data['приложения'] = 'services'
            elif isinstance(result, ServiceHeader):
                result_data = ServiceHeaderSerializer(result).data
                result_data['приложения'] = 'services'

            data.append(result_data)

        return paginator.get_paginated_response({
            "results": data
        })

    def perform_search(self, query, query_words, model, is_postgresql):
        filters = Q()

        for word in query_words:
            filters |= Q(title__contains=word)

        if is_postgresql:
            results = model.objects.filter(filters)
            results = results.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1).order_by('-similarity')
        else:
            results = model.objects.filter(filters)

        return results

    def is_postgresql(self):
        return connection.vendor == 'postgresql'

    def calculate_relevance(self, instance, query):
        return sum([1 for word in query.split() if word in instance.title])

    def clean_query(self, query):
        query = re.sub(r'\s+', ' ', query)
        query = re.sub(r'[^\w\s]', '', query)
        return query




# ______________________________________________________________________________________________________________________________________________________





class Similars(APIView):
    def get(self, request):
        query = request.query_params.get('search', '').strip()

        if not query:
            raise ValidationError({"error": "Введите поисковый запрос"})

        event_suggestions = self.get_suggestions(query, Events)
        project_suggestions = self.get_suggestions(query, MainProjects)
        corner_suggestions = self.get_suggestions(query, AmericanCorner)
        daily_news_suggestions = self.get_suggestions(query, DailyNews)
        events_news_suggestions = self.get_suggestions(query, EventsNews)
        book_arrival_suggestions = self.get_suggestions(query, BookArrival)
        media_coverage_suggestions = self.get_suggestions(query, MediaCoverage)
        service_suggestions = self.get_suggestions(query, Service)
        service_header_suggestions = self.get_suggestions(query, ServiceHeader)

        return Response({
            "events": event_suggestions, 
            "projects": project_suggestions,
            "corners": corner_suggestions,
            "daily_news": daily_news_suggestions,
            "events_news": events_news_suggestions,
            "book_arrival": book_arrival_suggestions,
            "media_coverage": media_coverage_suggestions,
            "services": service_suggestions,
            "service_headers": service_header_suggestions,
        })

    def get_suggestions(self, query, model):
        filters = Q(title__icontains=query)

        is_postgresql = self.is_postgresql()
        if is_postgresql:
            suggestions = model.objects.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1).order_by('-similarity')[:10]
        else:
            suggestions = model.objects.filter(filters).distinct()[:10]

        return [
            {
                "id": item.id,
                "title": item.title
            }
            for item in suggestions
        ]

    def is_postgresql(self):
        return connection.vendor == 'postgresql'
