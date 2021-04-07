from rest_framework import serializers
from .models import TablesRegistry
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablesRegistry
        fields = ['id', 'AMB_T', 'BOILER_T', 'COOL_FLOW', 'COOL_T_IN', 'COOL_T_OUT','CURRENT', 'E_ENERGY', 'E_POWER', 'HEAT_T_CON', 'HEAT_T_LIM', 'STATUS', 'VOLTAGE', 'DATETIME']