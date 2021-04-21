from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('registriesAPI/', views.registry_list),
    path('registriesAPI/<int:pk>/', views.registry_detail),
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('table/', views.list_registries),
    path('graph/', views.graph_registries),

    path('realTimeAPI/', views.real_time),
    path('tableAPI/<int:date_from>/<int:date_to>/', views.registry_table),
    path('graphAPI/<int:graphs>/<int:date_from>/<int:date_to>/', views.registry_graph)
]
