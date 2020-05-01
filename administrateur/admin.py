from django.contrib import admin

# Register your models here.
from .models import Etudiant,Module,Note
admin.site.register(Etudiant)
admin.site.register(Module)
admin.site.register(Note)