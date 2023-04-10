from django.contrib import admin
from note.models import *

# Register your models here.
admin.site.register([User, Note, Socials, UserDetails])
