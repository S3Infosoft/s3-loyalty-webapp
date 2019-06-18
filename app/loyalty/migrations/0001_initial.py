# Generated by Django 2.1.7 on 2019-06-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('address', models.TextField()),
                ('points_available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RewardItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.FloatField(max_length=10)),
                ('item_description', models.TextField()),
                ('points_required', models.IntegerField()),
            ],
        ),
    ]