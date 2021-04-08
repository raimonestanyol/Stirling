from rest_framework.decorators import api_view
from .models import TablesRegistry
from .serializers import TableSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt, timedelta as td


def list_registries(request):
    return render(request, 'snippets/Registries.html', {'endpoint': '/registriesAPI/'})


@api_view(('GET',))### NOT NEEDED
def registry_list(request):
    if request.method == 'GET':
        registries = TablesRegistry.objects.all()
        serializer = TableSerializer(registries, many=True)
        return Response(serializer.data)


@api_view(('GET',))### NOT NEEDED
def registry_detail(request, pk):
    try:
        registry = TablesRegistry.objects.get(pk=pk)
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry)
        return Response(serializer.data)

class Formatted_Date():
    def __init__(self, unformatted_date):
        self.year = int(str(unformatted_date)[:4])
        self.month = int(str(unformatted_date)[4:6])
        self.day = int(str(unformatted_date)[6:])


@api_view(('GET',))
def registry_table(request, date_from, date_to):
    date_from = Formatted_Date(date_from)
    date_to = Formatted_Date(date_to)
    try:
        registry = TablesRegistry.objects.filter(
            DATETIME__gte=dt(year=date_from.year, month=date_from.month, day=date_from.day)).filter(
            DATETIME__lte=dt(year=date_to.year, month=date_to.month, day=date_to.day))
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry, many=True)
        return Response(serializer.data)


@api_view(('GET',))
def registry_today(request):
    try:
        today = dt.now()-td(days=1)
        registry = TablesRegistry.objects.filter(
            DATETIME__gte=today)

    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry, many=True)
        return Response(serializer.data)