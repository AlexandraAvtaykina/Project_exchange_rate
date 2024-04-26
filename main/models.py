from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Currency(models.Model):
    charcode = models.CharField(max_length=5, verbose_name='код валюты')
    date = models.DateField(max_length=100, verbose_name='дата')
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='курс валюты')

    def __str__(self):
        return f'{self.charcode} {self.date} - {self.rate}'

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'
