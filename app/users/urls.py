from .views import UserRegister, IncreaseUserRatingView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'register', UserRegister, basename='register')
router.register(r'raiting', IncreaseUserRatingView, basename='raiting')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_user_login"),
    path('refresh/', TokenRefreshView.as_view(), name="api_user_refresh"),
    path('', include(router.urls)),
]
