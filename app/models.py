from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.IntegerField(null=True)
    organization = models.IntegerField(null=True)

    def __str__(self):
        return self.id;

class NonProfit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, null=True)
    location = models.IntegerField(null=True)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    address = models.CharField(max_length=100)
    location = models.IntegerField()
    description = models.CharField(max_length=500)
    photo = models.CharField(max_length=200, null=True)
    min_volunteers = models.IntegerField()
    max_volunteers = models.IntegerField()
    organization = models.ForeignKey(NonProfit, null=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class EventXUser(models.Model):
    uId = models.ForeignKey(User)
    eId = models.ForeignKey(Event)

    class Meta:
        unique_together =(("uId", "eId"),)

