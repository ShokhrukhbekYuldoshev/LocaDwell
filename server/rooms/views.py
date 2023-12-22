from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from locadwell.permissions import IsOwner
from rest_framework import filters
from rest_framework import pagination


# http://example.com/api/rooms?search=room1
class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]

    # NOTE:
    # The search behavior may be specified by prefixing field names in search_fields with one of the following characters (which is equivalent to adding __<lookup> to the field):
    # ^ istartswith
    # = iexact
    # $ iregex
    # @ search
    # None icontains
    # For example:
    # search_fields = ['=name', '^name', '$name', '@name', 'name']

    search_fields = ["address", "summary"]
    pagination_class = pagination.PageNumberPagination


class RoomDetail(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomCreate(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomUpdate(generics.UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsOwner, IsAdminUser]


class RoomDelete(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsOwner, IsAdminUser]
