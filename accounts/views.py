from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm

# Create your views here.
# class WelcomeView(TemplateView):
#     template_name: str = "base.html"


class SignUpView(TemplateView):
    form_class = CustomUserCreationForm
    # success_url = reverse_lazy('welcome:home')
    template_name = "base.html"

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     login(self.request, self.object)
    #     return response


class HomeView(TemplateView):
    pass
