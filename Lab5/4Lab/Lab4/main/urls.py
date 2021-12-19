from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cream', views.cream, name='cream'),
    path('ice_cr', views.ice_cr, name='ice_cr'),
    path('dari_ice_cr', views.dari_ice_cr, name='dari_ice_cr'),
    path('sherbet', views.sherbet, name='sherbet'),
    path('cost', views.cost, name='cost')
]

