from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError


class Review(models.Model):
    reservation = models.ForeignKey(
        "reservations.Reservation", on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, "Rating must be between 1 and 5"),
            MaxValueValidator(5, "Rating must be between 1 and 5"),
        ]
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} star review for Reservation #{self.reservation_id} by {self.reservation.user}"

    def clean(self):
        # Check if a review already exists for the given reservation
        if Review.objects.filter(reservation=self.reservation).exists():
            raise ValidationError("You have already reviewed this reservation.")
