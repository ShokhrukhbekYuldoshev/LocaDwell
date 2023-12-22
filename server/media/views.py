from rest_framework import generics
from .models import Media
from .serializers import MediaSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from locadwell.permissions import IsOwner


class MediaList(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MediaDetail(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MediaCreate(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MediaUpdate(generics.UpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsOwner, IsAdminUser]


class MediaDelete(generics.DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsOwner, IsAdminUser]
