# Generated by Django 2.1.7 on 2019-07-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty', '0002_spendpoints_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialdeals',
            name='deal_name',
            field=models.CharField(blank=True, default='no name', max_length=100),
        ),
    ]