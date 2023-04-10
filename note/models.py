from django.db import models
from datetime import date, time

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=32)
    fullname = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    account_creation_date = models.DateTimeField()
    active = models.TextChoices('ACTIVE', 'INACTIVE')


class UserDetails(models.Model):
    user_email = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=64)
    bio = models.TextField(max_length=255)
    profile_picture = models.TextField(max_length=64)


class Socials(models.Model):
    email = models.CharField(max_length=32)
    linkedin = models.CharField(max_length=32, null=True)
    twitter = models.CharField(max_length=32, null=True)
    facebook = models.CharField(max_length=32, null=True)
    instagram = models.CharField(max_length=32, null=True)


class Note(models.Model):
    user_email = models.CharField(max_length=32)
    title = models.TextField(max_length=64)
    note_content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
