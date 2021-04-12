from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('registriesAPI/', views.registry_list),
    path('registriesAPI/<int:pk>/', views.registry_detail),
    path('table/', views.list_registries),
    path('graph/', views.graph_registries),

    path('registriesAPI/<int:date_from>/<int:date_to>/', views.registry_table),
    path('registriesAPI/today/', views.registry_today)
]
