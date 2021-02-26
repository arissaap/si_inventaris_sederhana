from django.contrib import admin

# Register your models here.
from inventaris.models import Barang, Inventaris

admin.site.register(Barang)
admin.site.register(Inventaris)