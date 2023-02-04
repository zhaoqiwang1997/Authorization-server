from django.db import models

class Card(models.Model):
    card_number = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    com_name = models.CharField(max_length=20)
    expiration_data = models.DateField()
    masked_number =  models.IntegerField()
    limit = models.IntegerField()
    balance = models.IntegerField()

class User(models.Model):
    user_name = models.CharField(max_length=20)
    com_name = models.CharField(max_length=20)
    user_cards = models.JSONField()
    user_permission = models.CharField(max_length=10)

class Company(models.Model):
    com_name = models.CharField(max_length=20, primary_key=True)
    users = models.JSONField(default=list, blank=True)
    cards =  models.JSONField(default=list, blank=True)