# Generated by Django 5.0 on 2023-12-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectorInfo', '0011_rename_buildid_room_build_remove_room_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='storey',
            field=models.IntegerField(default=1, verbose_name='楼层'),
        ),
    ]