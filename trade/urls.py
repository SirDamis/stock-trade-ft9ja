from django.urls import path
from .views import home_view, admin_dashboard_view, admin_traders_dashboard_view, make_admin

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('dashboard/admin', admin_dashboard_view, name='admin_dashboard_view'),
    path('dashboard/admin/trader/<uuid:trader_id>', admin_traders_dashboard_view, name='admin_dashboard_view'),
    path('make-admin/', make_admin, name='make_admin'),
]
