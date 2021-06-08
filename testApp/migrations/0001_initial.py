# Generated by Django 3.1.7 on 2021-05-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationCountry', models.CharField(max_length=20)),
                ('destinationCity', models.CharField(max_length=20)),
                ('hotel', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('departureDay', models.DateTimeField()),
            ],
        ),
    ]
