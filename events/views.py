from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .models import Event
from .serializers import EventSerializer, UserSerializer # RegisterSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_public=True)
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#
# class RegisterViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = RegisterSerializer
