from django.contrib import admin

from main.models import Currency


@admin.register(Currency)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('charcode', 'date', 'rate',)
