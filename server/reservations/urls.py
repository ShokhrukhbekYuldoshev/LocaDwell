# urls.py
from django.urls import path
from .views import (
    ReservationList,
    ReservationDetail,
    ReservationCreate,
    ReservationUpdate,
    ReservationDelete,
    RoomReservationList,
    UserReservationList,
)

urlpatterns = [
    path("", ReservationList.as_view(), name="reservation-list"),
    path("<int:pk>/", ReservationDetail.as_view(), name="reservation-detail"),
    path("create/", ReservationCreate.as_view(), name="reservation-create"),
    path("<int:pk>/update/", ReservationUpdate.as_view(), name="reservation-update"),
    path("<int:pk>/delete/", ReservationDelete.as_view(), name="reservation-delete"),
    path("room/<int:pk>/", RoomReservationList.as_view(), name="room-reservations"),
    path("user/<int:pk>/", UserReservationList.as_view(), name="user-reservations"),
]
