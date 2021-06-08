from django.db import models
import datetime


class Voucher(models.Model):
    name = models.CharField(max_length=20, default="")
    destinationCountry = models.CharField(max_length=20)
    hotel = models.CharField(max_length=20)
    duration = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.FloatField()
    departureDay = models.DateTimeField()


class Order(models.Model):
    user = models.CharField(max_length=20)
    vouchers = models.IntegerField()
    price = models.FloatField()
    creationDate = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=20)

