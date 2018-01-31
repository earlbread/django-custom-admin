from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)


class EmailChangeRequest(models.Model):
    new_email = models.CharField(max_length=255)
    id_card = models.FileField()

