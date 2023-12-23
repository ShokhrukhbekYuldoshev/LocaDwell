from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()

    def get_user(self, review):
        user = review.reservation.user
        return user.id

    def get_room(self, review):
        room = review.reservation.room
        return room.id

    class Meta:
        model = Review
        fields = (
            "id",
            "reservation",
            "rating",
            "comment",
            "created_at",
            "updated_at",
            "user",
            "room",
        )
