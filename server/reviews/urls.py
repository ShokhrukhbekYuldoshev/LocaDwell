# urls.py
from django.urls import path
from .views import (
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    ReviewUpdate,
    ReviewDelete,
    RoomReviewList,
    UserReviewList,
)

urlpatterns = [
    path("", ReviewList.as_view(), name="review-list"),
    path("<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    path("create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/update/", ReviewUpdate.as_view(), name="review-update"),
    path("<int:pk>/delete/", ReviewDelete.as_view(), name="review-delete"),
    path("room/<int:pk>/", RoomReviewList.as_view(), name="room-reviews"),
    path("user/<int:pk>/", UserReviewList.as_view(), name="user-reviews"),
]
