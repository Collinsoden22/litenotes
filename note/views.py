from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from .models import User, UserDetails, Note

# Create your views here.


def home_view(request, *args, **kwargs):
    user = User.objects.get(id=1)
    user_details = UserDetails.objects.get(user_email=user.email)
    my_notes = Note.objects.filter(user_email=user.email)
    context = {
        'email': user.email,
        'name': user.fullname,
        'year': date.today().year,
        'bio': user_details.bio,
        'phone_number': user_details.phone_number,
        'profile_image': user_details.profile_picture,
        'notes': my_notes,
    }
    return render(request, "home.html", context)


def new_note_view(request, *args, **kwargs):
    user_details = User.objects.get(id=1)
    context = {
        'email': user_details.email,
        'name': user_details.fullname,
        'year': date.today().year
    }
    return render(request, "new.html", context)


def edit_note_view(request, *args, **kwargs):
    user_details = User.objects.get(id=1)
    context = {
        'email': user_details.email,
        'name': user_details.fullname,
        'year': date.today().year
    }
    return render(request, "edit.html", context)


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})
