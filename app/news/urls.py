from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.news.views import *

router = DefaultRouter()
router.register(r"news", NewsAPI, basename="news")
router.register(r'daily-news', DailyNewsAPI, basename='dailynews')
router.register(r'events-news', EventsNewsAPI, basename='eventsnews')
router.register(r'book-arrivals', BookArrivalAPI, basename='bookarrival')
router.register(r'media-coverage', MediaCoverageAPI, basename='mediacoverage')

urlpatterns = [
    path("", include(router.urls)),
]