# Generated by Django 4.2.4 on 2023-11-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0002_alter_hostel_details_hostel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant_details',
            name='user_registered',
            field=models.CharField(default='Null', max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='deposit_amount',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='fees_paid',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='fees_remaining',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='total_fees',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='feestransaction',
            name='final_amount',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='feestransaction',
            name='total_fees',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hostel_details',
            name='mess_fees',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no1_price',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no2_price',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no3_price',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no4_price',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
