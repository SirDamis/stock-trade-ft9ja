from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
import time, json
from .models import Trade, Trader
from user.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def home_view(request):
    trader = Trader.objects.get(user=request.user)
    trader_id = trader.id
    trader_balance = trader.balance

    current_time = timezone.now()
    hours_ago = current_time - timedelta(hours=1)

    trades = Trade.objects.filter(trader=trader_id, timestamp__gte=hours_ago, timestamp__lte=current_time).values("profit_loss", "timestamp")
    trades = Trade.objects.filter(trader=trader_id).values("profit_loss", "timestamp")

    context = {
        'current_balance': trader_balance,
        'trader_id': trader_id,
        'user_trade': json.dumps(list(trades), cls=DjangoJSONEncoder)
    }
    return render(request, 'home.html', context)

@staff_member_required
def admin_dashboard_view(request):
    all_traders = Trader.objects.all()
    context = {
        'all_traders': all_traders,
    }
    return render(request, 'admin/dashboard.html', context)

@staff_member_required
def admin_traders_dashboard_view(request, trader_id):
    trader = Trader.objects.get(id=trader_id)

    current_time = timezone.now()
    hours_ago = current_time - timedelta(hours=1)

    trades = Trade.objects.filter(trader=trader_id, timestamp__gte=hours_ago, timestamp__lte=current_time).values("profit_loss", "timestamp")

    context = {
        'current_balance': trader.balance,
        'trader_name': trader.user.name,
        'trader_id': trader.id,
        'trader_trade': json.dumps(list(trades), cls=DjangoJSONEncoder)
    }
    return render(request, 'admin/trader-details.html', context)

@login_required
def make_admin(request):
    user = User.objects.get(id=request.user.id)
    user.is_staff = True
    user.save()
    return HttpResponse("User has been made an admin")