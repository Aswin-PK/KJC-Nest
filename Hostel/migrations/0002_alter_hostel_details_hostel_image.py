# Generated by Django 4.2.7 on 2023-11-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel_details',
            name='hostel_image',
            field=models.ImageField(default='image not available', null=True, upload_to=''),
        ),
    ]