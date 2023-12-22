from rest_framework import serializers

from reviews.models import Review

from .models import Room
from media.models import Media
from django.contrib.contenttypes.models import ContentType


class RoomSerializer(serializers.ModelSerializer):
    media_files = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    def get_media_files(self, room):
        """
        Retrieves all media files associated with a given room.

        :param room: The room for which to retrieve media files.
        :type room: Room

        :return: A list of URLs pointing to the media files.
        :rtype: List[str]
        """
        room_content_type = ContentType.objects.get_for_model(Room)
        media_files = Media.objects.filter(
            model_type=room_content_type, model_id=room.id
        )
        return [media_file.media_file.url for media_file in media_files]

    def get_rating(self, room):
        """
        Calculates the rating of a room based on its reviews.

        Parameters:
            room (Room): The room for which to calculate the rating.

        Returns:
            float: The average rating of the room. If there are no reviews, returns 0.
        """
        reviews = Review.objects.filter(reservation__room=room)
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0

    class Meta:
        model = Room
        fields = [
            "id",
            "home_type",
            "room_type",
            "total_occupancy",
            "total_bedrooms",
            "total_bathrooms",
            "summary",
            "address",
            "has_tv",
            "has_kitchen",
            "has_heating",
            "has_internet",
            "price",
            "published_at",
            "owner",
            "created_at",
            "updated_at",
            "latitude",
            "longitude",
            "media_files",
            "rating",
        ]
