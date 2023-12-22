# urls.py
from django.urls import path
from .views import MediaList, MediaDetail, MediaCreate, MediaUpdate, MediaDelete

urlpatterns = [
    path("", MediaList.as_view(), name="media-list"),
    path("<int:pk>/", MediaDetail.as_view(), name="media-detail"),
    path("create/", MediaCreate.as_view(), name="media-create"),
    path("<int:pk>/update/", MediaUpdate.as_view(), name="media-update"),
    path("<int:pk>/delete/", MediaDelete.as_view(), name="media-delete"),
]
