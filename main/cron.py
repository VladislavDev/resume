from django.utils.timezone import now

from .models import ExRates, DesiredPosition

import requests

def ex_rates_update():

    print('ExRatesUpdate (Cron) start')

    lastRate = ExRates.objects.order_by('-updated')[:1]
    if lastRate.count() > 0:

        if lastRate[0].updated.date() >= now().date():
            return

    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    print('Get start')

    if (response.status_code == 200):

        try:
            rate = response.json()['Valute']['USD']['Value']

            print('Updated')
            ExRates.objects.add(rate)

            DesiredPosition.objects.updateSalaryUSD(rate)

        except Exception as e:
            # TODO Create ExceptionCollector
            print(e)

    else:
        # TODO Create ExceptionCollector
        print('Can not requesting this information')
