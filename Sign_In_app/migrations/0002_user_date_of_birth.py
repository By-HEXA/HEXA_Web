# Generated by Django 5.1.4 on 2025-01-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sign_In_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Date_of_Birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
