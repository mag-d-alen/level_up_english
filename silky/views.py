from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from accounts.forms import CustomUserCreationForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RegisterPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


