# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TablesRegistry(models.Model):
    amb_t = models.DecimalField(db_column='AMB_T', max_digits=3, decimal_places=1)  # Field name made lowercase.
    boiler_t = models.DecimalField(db_column='BOILER_T', max_digits=4, decimal_places=1)  # Field name made lowercase.
    cool_flow = models.DecimalField(db_column='COOL_FLOW', max_digits=3, decimal_places=1)  # Field name made lowercase.
    cool_t_in = models.DecimalField(db_column='COOL_T_IN', max_digits=4, decimal_places=1)  # Field name made lowercase.
    cool_t_out = models.DecimalField(db_column='COOL_T_OUT', max_digits=4, decimal_places=1)  # Field name made lowercase.
    current = models.DecimalField(db_column='CURRENT', max_digits=3, decimal_places=2)  # Field name made lowercase.
    e_energy = models.DecimalField(db_column='E_ENERGY', max_digits=5, decimal_places=1)  # Field name made lowercase.
    e_power = models.PositiveSmallIntegerField(db_column='E_POWER')  # Field name made lowercase.
    heat_t_con = models.DecimalField(db_column='HEAT_T_CON', max_digits=5, decimal_places=1)  # Field name made lowercase.
    heat_t_lim = models.DecimalField(db_column='HEAT_T_LIM', max_digits=5, decimal_places=1)  # Field name made lowercase.
    status = models.PositiveSmallIntegerField(db_column='STATUS')  # Field name made lowercase.
    voltage = models.DecimalField(db_column='VOLTAGE', max_digits=4, decimal_places=1)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DATETIME')  # Field name made lowercase.

    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return

    def update(self, *args, **kwargs):
        return
    class Meta:
        db_table = 'tables_registry'
