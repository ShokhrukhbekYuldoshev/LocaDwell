# Generated by Django 4.2.6 on 2023-12-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_file',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='mime_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
