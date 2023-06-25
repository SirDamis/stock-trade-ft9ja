from django.contrib.auth import views 
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("login/", views.LoginView.as_view(redirect_authenticated_user=True, template_name = 'login.html'), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
]