from django.http import JsonResponse
from django.shortcuts import render

from main.models import Currency


def get_currency_rate(request):
    charcode = request.GET.get('charcode')
    date = request.GET.get('date')
    currency = Currency.objects.filter(charcode=charcode, date=date).first()

    if currency:
        return JsonResponse({
            'charcode': currency.charcode,
            'date': currency.date,
            'rate': currency.rate
        })
    else:
        return JsonResponse({'ERROR': 'Currency rate not found'}, status=404)


