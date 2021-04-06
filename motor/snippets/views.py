from rest_framework.decorators import api_view
from .models import TablesRegistry
from .serializers import TableSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render


class RegistryList(generics.ListCreateAPIView):
    queryset = TablesRegistry.objects.all()
    serializer_class = TableSerializer


class RegistryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TablesRegistry.objects.all()
    serializer_class = TableSerializer

@api_view(('GET',))
def registry_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        registries = TablesRegistry.objects.all()
        serializer = TableSerializer(registries, many=True)
        return Response(serializer.data)

@api_view(('GET',))
def registry_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        registry = TablesRegistry.objects.get(pk=pk)
    except TablesRegistry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TableSerializer(registry)
        return Response(serializer.data)


def list_registries(request):
    return render(request, 'snippets/Registries.html', {'endpoint': '/registriesAPI/'})