# Generated by Django 4.0.4 on 2022-04-29 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0022_alter_show_room_cname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show_room',
            name='Cname',
        ),
    ]
