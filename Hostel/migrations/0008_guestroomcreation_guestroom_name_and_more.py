# Generated by Django 4.2.4 on 2023-12-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0007_guestroom_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestroomcreation',
            name='Guestroom_name',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='guestroomcreation',
            name='bed_count',
            field=models.IntegerField(choices=[(1, '1'), (2, '2')]),
        ),
    ]
