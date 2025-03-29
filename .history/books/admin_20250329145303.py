from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Subject)
admin.site.register(Book)

################################################################
# Models for teacher work
################################################################

admin.site.register(Student)
admin.site.register(Course)
