from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    admin = models.TextField()

class List(models.Model):
    service =models.CharField(max_length=100)

class Public(models.Model):
    body = models.CharField(max_length=250)