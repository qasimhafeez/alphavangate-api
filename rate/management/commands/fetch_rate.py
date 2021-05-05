from django.core.management import BaseCommand
from rate.utils import get_rate
from rate.models import BtcRate


class Command(BaseCommand):
    help = 'Fetching BTC/USD rates from alphavantage API'

    def handle(self, *args, **kwargs):
        BtcRate.objects.create(**{'exchange_rate': get_rate()})
