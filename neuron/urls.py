from django.urls import path
from neuron import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.main),
    path('short_description/', views.short_description),
    path('short_description/create/', views.create),
    path('create/<int:id>', views.output),
    path('registration/', views.registration),
    path('login/', views.login),

]