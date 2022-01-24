from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    BaseView, LoginView, RegistrationView
)


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('loguot/', LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]