from django.contrib import admin

from .models import Vendor, Tyre, Incoming

admin.site.register(Vendor)


@admin.register(Tyre)
class TyreAdmin(admin.ModelAdmin):
    list_display = ('model', 'vendor', 'price')

@admin.register(Incoming)
class IncomingAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')