# Generated by Django 5.0.6 on 2024-05-19 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_district')),
            ],
        ),
    ]
