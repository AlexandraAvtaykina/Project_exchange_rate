from django.urls import path

from main.apps import MainConfig
from main.views import get_currency_rate

app_name = MainConfig.name

urlpatterns = [
    path('rate/', get_currency_rate, name='get_currency_rate'),
]
