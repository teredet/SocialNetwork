from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, LoginForm


class BaseView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'base/base.html')


class LoginView(View):
    template_name = 'base/login.html'
    redirect_authenticated_user=True
    
    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, self.template_name, {'form': form})


class RegistrationView(CreateView):
    template_name = 'base/registration.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
