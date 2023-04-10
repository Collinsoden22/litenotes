from django.db import models
from datetime import date,time

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=32)
    fullname = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    account_creation_date = models.DateTimeField()
    active = models.TextChoices('ACTIVE', 'INACTIVE')

class Review(models.Model):
    book_title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    user_email = models.CharField(max_length=32)
    comment = models.TextField(max_length=255)
    ratings = models.IntegerField()
    date_submitted = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    cover = models.TextField(max_length=64)

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
