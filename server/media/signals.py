from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Media


def get_mime_type(file_name):
    import mimetypes

    return mimetypes.guess_type(file_name, strict=False)[0]


@receiver(pre_save, sender=Media)
def pre_save_media(sender, instance: Media, **kwargs):
    print("pre_save_media")
    if instance.media_file:
        instance.file_name = instance.media_file.name
        mime_type = get_mime_type(instance.media_file.path)
        print(mime_type)
        if mime_type:
            instance.mime_type = mime_type


# This connects the pre_save_media function to the pre_save signal of the Media model
pre_save.connect(pre_save_media, sender=Media)
