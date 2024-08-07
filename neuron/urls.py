from django.urls import path
from neuron import views

urlpatterns = [
    path('', views.main),
    path('short_description/', views.short_description),
    path('create/', views.create),
    path('create/<int:id>', views.output),
    path('registration/', views.registration),
    path('login/', views.login),

]