from django.contrib import admin
from .models import Tyre, Vendor


# admin.site.register(Tyre)
admin.site.register(Vendor)


@admin.register(Tyre)
class PostAdmin(admin.ModelAdmin):
 list_display = ('model', 'price')