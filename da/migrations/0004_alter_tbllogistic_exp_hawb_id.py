# Generated by Django 4.1.5 on 2023-03-10 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0003_alter_texphawb_exp_shipping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbllogistic',
            name='exp_hawb_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='da.texphawb'),
        ),
    ]