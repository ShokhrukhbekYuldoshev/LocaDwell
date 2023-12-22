from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from locadwell.permissions import IsOwner


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReservationCreate(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReservationUpdate(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsOwner, IsAdminUser]


class ReservationDelete(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsOwner, IsAdminUser]


class RoomReservationList(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsOwner, IsAdminUser]

    def get_queryset(self):
        room_id = self.kwargs["pk"]
        reservations = Reservation.objects.filter(room__id=room_id)
        return reservations


class UserReservationList(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsOwner, IsAdminUser]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        reservations = Reservation.objects.filter(user=user_id)
        return reservations
