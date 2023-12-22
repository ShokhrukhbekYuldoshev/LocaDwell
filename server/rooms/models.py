from django.db import models
from users.models import CustomUser


class Room(models.Model):
    id = models.AutoField(primary_key=True)

    # NOTE: Choices for HomeType and RoomType
    class HomeType(models.TextChoices):
        HOUSE = "House", "House"
        APARTMENT = "Apartment", "Apartment"

    class RoomType(models.TextChoices):
        ENTIRE_PLACE = "Entire Place", "Entire Place"
        PRIVATE_ROOM = "Private Room", "Private Room"
        SHARED_ROOM = "Shared Room", "Shared Room"

    home_type = models.CharField(
        max_length=20,
        choices=HomeType.choices,
        default=HomeType.HOUSE,
    )

    room_type = models.CharField(
        max_length=20,
        choices=RoomType.choices,
        default=RoomType.ENTIRE_PLACE,
    )

    total_occupancy = models.IntegerField()
    total_bedrooms = models.IntegerField()
    total_bathrooms = models.IntegerField()
    summary = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    has_tv = models.BooleanField()
    has_kitchen = models.BooleanField()
    has_heating = models.BooleanField()
    has_internet = models.BooleanField()
    price = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address
