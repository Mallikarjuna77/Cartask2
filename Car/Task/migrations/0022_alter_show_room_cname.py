# Generated by Django 4.0.4 on 2022-04-29 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0021_alter_show_room_cname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show_room',
            name='Cname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task.carlist'),
        ),
    ]
