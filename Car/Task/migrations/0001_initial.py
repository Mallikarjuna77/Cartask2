# Generated by Django 4.0.4 on 2022-04-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=30)),
                ('Price', models.IntegerField()),
                ('Ratings', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Brand', models.CharField(max_length=30)),
                ('Modelyear', models.IntegerField()),
            ],
        ),
    ]
