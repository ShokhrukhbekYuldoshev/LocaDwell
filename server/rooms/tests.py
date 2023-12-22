from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Room
from users.models import CustomUser


class RoomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(
            home_type="House",
            room_type="Entire Place",
            total_occupancy=4,
            total_bedrooms=2,
            total_bathrooms=1,
            summary="A nice house",
            address="123 Main St",
            has_tv=True,
            has_kitchen=True,
            has_heating=True,
            has_internet=True,
            price=200,
            owner=CustomUser.objects.create(
                email="test@test.com", password="testpassword"
            ),
            published_at="2020-01-01 00:00:00",
            created_at="2020-01-01 00:00:00",
            updated_at="2020-01-01 00:00:00",
            latitude=40.7128,
            longitude=-74.0060,
        )

    def test_room_content(self):
        room = Room.objects.get(id=1)
        expected_object_name = f"{room.home_type}, {room.room_type}"
        self.assertEquals(expected_object_name, "House, Entire Place")

    def test_room_list_view(self):
        response = self.client.get(reverse("room-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_room_detail_view(self):
        response = self.client.get(reverse("room-detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_room_create_view(self):
    #     response = self.client.post(
    #         reverse("room-create"),
    #         {
    #             "home_type": "Apartment",
    #             "room_type": "Private Room",
    #             "total_occupancy": 2,
    #             "total_bedrooms": 1,
    #             "total_bathrooms": 1,
    #             "summary": "A nice apartment",
    #             "address": "456 Oak St",
    #             "has_tv": True,
    #             "has_kitchen": True,
    #             "has_heating": True,
    #             "has_internet": True,
    #             "price": 150,
    #             "owner": CustomUser.objects.get(email="testuser@test.com"),
    #             "published_at": "2020-01-01 00:00:00",
    #             "created_at": "2020-01-01 00:00:00",
    #             "updated_at": "2020-01-01 00:00:00",
    #             "latitude": 40.7128,
    #             "longitude": -74.0060,
    #         },
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_room_update_view(self):
    #     response = self.client.put(
    #         reverse("room-update", args=[1]),
    #         {
    #             "home_type": "House",
    #             "room_type": "Private Room",
    #             "total_occupancy": 2,
    #             "total_bedrooms": 1,
    #             "total_bathrooms": 1,
    #             "summary": "Updated summary",
    #             "address": "123 Updated St",
    #             "has_tv": False,
    #             "has_kitchen": True,
    #             "has_heating": True,
    #             "has_internet": True,
    #             "price": 200,
    #         },
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_room_delete_view(self):
        self.client.login(email="test@test.com", password="testpassword")
        response = self.client.delete(reverse("room-detail", args=[1]))
        if response.status_code != status.HTTP_204_NO_CONTENT:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
