# Generated by Django 4.2.7 on 2023-11-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
