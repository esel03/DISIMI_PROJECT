from django.urls import path
from neuron import views
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.main),
    path('short_description/', views.short_description),
    path('short_description/confirm', views.confirm),
    path('short_description/create/', views.create),
    path('create/<int:id_user>/<int:id_depend>', views.output),
    path('registration/', views.registration),
    path('view_login/', views.view_login),
    path('room/exit/', views.exit),
    path('room/', views.room),


]