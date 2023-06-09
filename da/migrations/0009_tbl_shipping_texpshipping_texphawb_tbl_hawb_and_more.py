# Generated by Django 4.1.5 on 2023-03-31 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0008_tbl_postclearance_tbl_preclearance_tcharacterdeal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBL_SHIPPING',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('way_bill', models.CharField(max_length=100)),
                ('expected_delivery', models.DateField()),
                ('remarks', models.TextField(blank=True)),
                ('date_transfer_docs', models.DateField(blank=True, null=True)),
                ('act_number', models.CharField(blank=True, max_length=100)),
                ('act_date', models.DateField(blank=True, null=True)),
                ('act_comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TexpShipping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('way_bill', models.CharField(max_length=100)),
                ('shipping_invoice', models.CharField(blank=True, max_length=100)),
                ('date_send_to_bc', models.DateField()),
                ('date_of_placement', models.DateField(blank=True, null=True)),
                ('declaration_num', models.CharField(blank=True, max_length=100)),
                ('date_of_issue', models.DateField(blank=True, null=True)),
                ('procedures', models.TextField(blank=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('flight_number', models.CharField(blank=True, max_length=100)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('delay_reason', models.TextField(blank=True)),
                ('regime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.tregime')),
            ],
        ),
        migrations.CreateModel(
            name='Texphawb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hawb', models.CharField(max_length=100)),
                ('exp_shipping_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.texpshipping')),
            ],
        ),
        migrations.CreateModel(
            name='TBL_HAWB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hawb', models.CharField(max_length=100)),
                ('shipping_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.tbl_shipping')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_preclearance_shipping',
            name='HAWB_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='da.tbl_hawb'),
        ),
        migrations.AddField(
            model_name='tbl_preclearance_shipping',
            name='SHIPPING_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='da.tbl_shipping'),
        ),
    ]
