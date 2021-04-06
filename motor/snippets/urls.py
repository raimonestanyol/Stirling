from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('registriesAPI/', views.registry_list),
    path('registriesAPI/<int:pk>/', views.registry_detail),
    path('registries/', views.list_registries),

]