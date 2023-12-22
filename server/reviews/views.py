from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from locadwell.permissions import IsOwner


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewUpdate(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwner, IsAdminUser]


class ReviewDelete(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwner, IsAdminUser]


class RoomReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        room_id = self.kwargs["pk"]
        reviews = Review.objects.filter(reservation__room__id=room_id)
        return reviews


class UserReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        reviews = Review.objects.filter(reservation__user__id=user_id)
        return reviews
