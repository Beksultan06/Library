from django.urls import path, include 
from app.page_for_readers.views import BannerViewViewSet, Graphic_workViewViewSet, TitlesViewViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'banner', BannerViewViewSet, basename='banner')
router.register(r'graphic_work', Graphic_workViewViewSet, basename='Graphic_work')
router.register(r'titles', TitlesViewViewSet, basename='Titles')

urlpatterns = [

]   

urlpatterns += router.urls