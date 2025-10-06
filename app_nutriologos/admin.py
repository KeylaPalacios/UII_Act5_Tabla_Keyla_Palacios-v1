from django.contrib import admin

# Register your models here.

from .models import Nutriologo
# registrar el modelo Nutriologo en el admin
admin.site.register(Nutriologo)
