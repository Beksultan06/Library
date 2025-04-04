from django.urls import path, include 
from app.professional_activity.views import ActivityViewViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'ativity', ActivityViewViewSet, basename='ativity')

urlpatterns = [

]

urlpatterns += router.urls