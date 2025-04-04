from .models import User
from .serializers import RegisterSerializer, ReatingsSerializers
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserRegister(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class IncreaseUserRatingView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ReatingsSerializers
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        Обновляет рейтинг текущего пользователя и возвращает его данные.
        """
        user = request.user
        try:
            user.reitforusers = int(user.reitforusers) + 1
        except:
            user.reitforusers = 1
        user.save()

        serializer = self.get_serializer(user)
        return Response({
            'message': 'Ваш рейтинг обновлён',
            'new_rating': user.reitforusers,
            'user': serializer.data
        })