# Generated by Django 4.2.6 on 2023-12-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_room_home_type_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/rooms'),
        ),
    ]
