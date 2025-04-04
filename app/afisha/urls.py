from rest_framework.routers import DefaultRouter
from .views import EventsMixins, AfishaMixins

router = DefaultRouter()

router.register(r'afisha', AfishaMixins, basename='afisha')
router.register(r'events', EventsMixins, basename='events')

urlpatterns = router.urls