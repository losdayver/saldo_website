from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('initial_saldo', views.init_saldo, name='initial saldo'),
    path('payments', views.payments, name='initial saldo'),
    path('charges', views.charges, name='initial saldo'),
    path('apartment', views.apartment, name='apartment'),
    path('year_result', views.year_result, name='year result'),
]