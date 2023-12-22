from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.forms import ValidationError
from users.models import CustomUser


class Media(models.Model):
    model_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    model_id = models.PositiveIntegerField()
    file_name = models.CharField(max_length=255, blank=True)

    class MimeType(models.TextChoices):
        JPEG = "image/jpeg"
        PNG = "image/png"
        GIF = "image/gif"
        WEBP = "image/webp"
        MP4 = "video/mp4"
        WEBM = "video/webm"

    mime_type = models.CharField(
        max_length=100,
        choices=MimeType.choices,
        blank=True,
        help_text="The mime type of the media file.",
    )
    media_file = models.FileField(upload_to="uploads/")

    # Generic Foreign Key to associate media with any model
    content_object = GenericForeignKey("model_type", "model_id")

    def __str__(self):
        return self.file_name

    def clean(self):
        """
        Cleans the media file by performing the following validations:

        - Checks if the mime type of the media file is valid. The valid mime types are "image/jpeg", "image/png", "image/gif", "image/webp", "video/mp4", and "video/webm". If the mime type is not valid, raises a ValidationError with the message "Invalid mime type".

        - Checks if the size of the media file is within the allowed limit of 5MB. If the size exceeds the limit, raises a ValidationError with the message "File size too large".

        - Checks if the model_type is set to User and the media file is not an image file (i.e., does not have a file extension of .jpg, .jpeg, or .png). If the conditions are met, raises a ValidationError with the message "Only image files are allowed for User model."

        This function does not take any parameters and does not return any value.
        """

        # Check if the file exists
        if not self.media_file:
            raise ValidationError("File does not exist")

        # Check if the file size is less than 5MB
        if self.media_file.size > 5 * 1024 * 1024:
            raise ValidationError("File size too large")

        # Check if the model_type is User and the file is not an image
        if (
            self.model_type
            and self.model_type.model_class() == CustomUser
            and not self.media_file.name.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            )
        ):
            raise ValidationError("Only image files are allowed for User model.")
