from unicodedata import name
from django.core.management.base import BaseCommand
from trade.models import Trader
from user.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Create initial stock traders'

    def handle(self, *args, **options):
        traders_count = Trader.objects.count()
        while traders_count < 10:
            faker = Faker()
            name =  faker.name()
            email = faker.email()
            password = faker.password()

            user = User(
                name=name,
                email=email,
            )
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created trader: {name}"))
            traders_count += 1