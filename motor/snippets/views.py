from rest_framework.decorators import api_view
from .models import TablesRegistry
from .serializers import TableSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt, timedelta as td, timezone
import pytz


def list_registries(request):
    return render(request, 'snippets/Registries.html', {'endpoint': '/registriesAPI/'})


@api_view(('GET',))
def registry_list(request):
    if request.method == 'GET':
        registries = TablesRegistry.objects.all()
        serializer = TableSerializer(registries, many=True)
        return Response(serializer.data)


@api_view(('GET',))
def registry_detail(request, pk):
    try:
        registry = TablesRegistry.objects.get(pk=pk)
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry)
        return Response(serializer.data)


@api_view(('GET',))
def registry_table(request, date_from, date_to):
    try:
        registry = TablesRegistry.objects.filter(
            DATETIME__gte=dt(year=date_from[:4], month=date_from[4:6], day=date_from[6:], tzinfo=timezone.utc)).filter(
            DATETIME__lte=dt(year=date_to[:4], month=date_to[4:6], day=date_to[6:], tzinfo=timezone.utc))
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry)
        return Response(serializer.data)


@api_view(('GET',))
def registry_today(request):
    try:
        today = dt.now(tz=pytz.timezone('Europe/Madrid'))-td(days=1)
        registry = TablesRegistry.objects.filter(
            DATETIME__gte=today)

    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry, many=True)
        return Response(serializer.data)