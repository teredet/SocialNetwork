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



    # def post(self, request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username, password=password)

    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)

    #             return HttpResponseRedirect('/form')
    #         else:
    #             return HttpResponse("Inactive user.")
    #     else:
    #         return HttpResponseRedirect('login')

    #     return render(request, "index.html")

    # def get(self, request, *args, **kwargs):
    #     form = CustomUserChangeForm(request.POST or None)
    #     return render(request, 'base/login.html', {'form': form})


    # def post(self, request, *args, **kwargs):
    #     form = CustomUserChangeForm(request.POST or None)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             login(request, user)
    #             return HttpResponseRedirect('/')
    #     context = {'form':form,}
    #     return render(request, 'base/login.html', {'form': form})


class RegistrationView(CreateView):
    template_name = 'base/registration.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
