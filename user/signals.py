from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


from trade.models import Trader
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_trader_instance(sender, instance, created, **kwargs):
    if created:
        Trader.objects.create(user=instance, balance=100.0)
