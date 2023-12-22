# urls.py
from django.urls import path
from .views import RoomList, RoomDetail, RoomCreate, RoomUpdate, RoomDelete

urlpatterns = [
    path("", RoomList.as_view(), name="room-list"),
    path("<int:pk>/", RoomDetail.as_view(), name="room-detail"),
    path("create/", RoomCreate.as_view(), name="room-create"),
    path("<int:pk>/update/", RoomUpdate.as_view(), name="room-update"),
    path("<int:pk>/delete/", RoomDelete.as_view(), name="room-delete"),
]
