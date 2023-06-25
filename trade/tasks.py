import random
from celery import shared_task
from datetime import datetime
from django.utils import timezone
from .models import Trade, Trader
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from itertools import islice

@shared_task
def generate_profit_loss():
    BATCH_SIZE = 100
    traders = Trader.objects.all()
    profit_loss_map = {}
    for chunk in batch_iterator(traders, BATCH_SIZE):
        trades = []
        for trader in chunk:
            if trader.balance <= 0:
                profit_loss = 0.0
            else:
                profit_loss = random.uniform(-10, 10)
                trader.balance += (profit_loss)
                trader.save()
                
            trade = Trade(trader=trader, profit_loss=profit_loss)
            trades.append(trade)
            profit_loss_map[str(trader.id)] = profit_loss
        Trade.objects.bulk_create(trades)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('trade', {
        'type': 'process_trade',
        'data': {
            "profit_loss": profit_loss_map
        },
    })

def batch_iterator(iterable, batch_size):
    iterator = iter(iterable)
    while True:
        batch = list(islice(iterator, batch_size))
        if not batch:
            return
        yield batch
