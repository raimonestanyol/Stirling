from rest_framework import serializers
from .models import TablesRegistry
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablesRegistry
        fields = ['id', 'amb_t', 'boiler_t', 'cool_flow', 'cool_t_in', 'cool_t_out']