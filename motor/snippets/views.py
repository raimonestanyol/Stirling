from rest_framework.decorators import api_view
from .models import TablesRegistry
from .serializers import TableSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt, timedelta as td
from math import ceil


def list_registries(request):
    return render(request, 'snippets/Table.html', {'endpoint': '/tableAPI/'})


def graph_registries(request):
    return render(request, 'snippets/Graph.html', {'endpoint': '/graphAPI/'})


def home(request):
    return render(request, 'snippets/Home.html')


def about(request):
    return render(request, 'snippets/About.html')


@api_view(('GET',))  ### NOT NEEDED
def registry_list(request):
    if request.method == 'GET':
        registries = TablesRegistry.objects.all()
        serializer = TableSerializer(registries, many=True)
        return Response(serializer.data)


@api_view(('GET',))  ### NOT NEEDED
def registry_detail(request, pk):
    try:
        registry = TablesRegistry.objects.get(pk=pk)
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry)
        return Response(serializer.data)


class FormattedDate:
    def __init__(self, unformatted_date):
        self.year = int(str(unformatted_date)[:4])
        self.month = int(str(unformatted_date)[4:6])
        self.day = int(str(unformatted_date)[6:])
        self.date = dt(self.year, self.month, self.day)


@api_view(('GET',))
def registry_table(request, date_from, date_to):
    date_from = FormattedDate(date_from)
    date_to = FormattedDate(date_to)
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
def real_time(request):
    try:
        registry = TablesRegistry.objects.last()
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry)
        return Response(serializer.data)


def graphs_decoder(graphs):
    graphs = str(graphs)
    graphs_num = graphs.count("1") - 1
    columns = ["DATETIME", "AMB_T", "BOILER_T", "HEAT_T_CON", "HEAT_T_LIM", "COOL_FLOW", "COOL_T_IN", "COOL_T_OUT",
               "CURRENT", "VOLTAGE", "E_POWER", "E_ENERGY", None, "STATUS"]
    activated_graphs = list(filter(None, map(lambda x, y: x if y == "1" else None, columns, graphs)))

    return graphs_num, activated_graphs


@api_view(('GET',))
def registry_graph(request, graphs, date_from, date_to):
    date_from = FormattedDate(date_from)
    date_to = FormattedDate(date_to)
    days_difference = date_to.date - date_from.date
    graphs_num, activated_graphs = graphs_decoder(graphs)
    divider = ceil(days_difference.days * graphs_num / 90)
    try:
        registry = TablesRegistry.objects.filter(
            DATETIME__gte=dt(year=date_from.year, month=date_from.month, day=date_from.day)).filter(
            DATETIME__lte=dt(year=date_to.year, month=date_to.month, day=date_to.day)).values(*activated_graphs, )[
                   :: divider]
        print("days " + str(days_difference.days))
        print(graphs_num, *activated_graphs)
        print(divider)
        print(ceil(len(registry) * graphs_num / divider))

    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)
    return Response(registry)
    if request.method == 'GET':
        # serializer = TableSerializer(registry, many=True)
        return Response(registry)


@api_view(('GET',))  ### NOT NEEDED
def registry_today(request):
    try:
        today = dt.now() - td(days=1)
        registry = TablesRegistry.objects.filter(
            DATETIME__gte=today)

    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry, many=True)
        return Response(serializer.data)
