# Generated by Django 4.0.4 on 2022-04-24 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0007_alter_show_room_carlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show_room',
            old_name='Name',
            new_name='Show_roomName',
        ),
    ]