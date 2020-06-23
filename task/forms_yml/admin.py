from django.contrib import admin

from .models import Vendor, Tyre

admin.site.register(Vendor)


@admin.register(Tyre)
class TyreAdmin(admin.ModelAdmin):
    list_display = ('model', 'vendor', 'price')