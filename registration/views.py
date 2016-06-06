from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from registration.forms import *
from django.views.generic import ListView
# Create your views here:
class Home(ListView):
   template_name="index.html"

   def get_queryset(self):
       return Chocolate.objects.all()

class UserRegistrationView(AnonymousRequiredMixin, FormView):
   template_name = "register/user/register_user.html"
   authenticated_redirect_url = reverse_lazy(u"home")
   form_class = UserRegistrationForm
   success_url = '/register/user/success/'

   def form_valid(self, form):
      form.save()
      return FormView.form_valid(self, form)

class AddChocolateView( FormView):
   template_name = "register/chocolate/add_chocolate.html"
   authenticated_redirect_url = reverse_lazy(u"home")
   form_class = AddChocolateForm
   success_url = '/register/chocolate/success/'

   def form_valid(self, form):
       form.save()
       return FormView.form_valid(self, form)
