# Generated by Django 4.0.4 on 2022-04-29 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0019_remove_show_room_cname'),
    ]

    operations = [
        migrations.AddField(
            model_name='show_room',
            name='Cname',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='showrooms', to='Task.carlist'),
        ),
    ]
