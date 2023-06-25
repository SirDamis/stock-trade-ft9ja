from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegisterForm

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


# Sign Up View
class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    success_message = "Account was created successfully"
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')
        return super(RegisterView, self).get(self, request, *args, **kwargs)

