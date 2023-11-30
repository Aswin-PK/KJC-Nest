# Generated by Django 4.2.7 on 2023-11-30 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0004_alter_applicant_details_deposit_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant_details',
            name='bed_no',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='deposit_amount',
            field=models.CharField(blank=True, default='Null', max_length=255),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='fees_paid',
            field=models.CharField(blank=True, default='Null', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='fees_remaining',
            field=models.CharField(blank=True, default='Null', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='room_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='total_fees',
            field=models.CharField(blank=True, default='Null', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feestransaction',
            name='final_amount',
            field=models.CharField(blank=True, default='Null', max_length=255),
        ),
        migrations.AlterField(
            model_name='feestransaction',
            name='total_fees',
            field=models.CharField(blank=True, default='Null', max_length=255),
        ),
        migrations.AlterField(
            model_name='hostel_details',
            name='mess_fees',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no1_price',
            field=models.CharField(default='5000', max_length=255),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no2_price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no3_price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='bed_no4_price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hostelroomdetails',
            name='no_of_beds',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], max_length=255),
        ),
    ]
