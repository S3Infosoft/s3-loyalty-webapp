# Generated by Django 2.1.7 on 2019-06-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty', '0003_auto_20190612_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='contact_p_phone',
            field=models.CharField(max_length=12),
        ),
    ]
