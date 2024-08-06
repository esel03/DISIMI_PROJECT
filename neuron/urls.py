from django.urls import path
from neuron import views

urlpatterns = [
    
    path('', views.short_description),
    path('create/', views.create),
    path('create/<int:id>', views.output),

]