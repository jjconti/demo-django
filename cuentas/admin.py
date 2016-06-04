from django.contrib import admin
from django.db.models import Sum

import models


class LocalidadAdmin(admin.ModelAdmin):
    ordering = ('nombre',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['nombre']
        else:
            return []


class CuentaAdmin(admin.ModelAdmin):
    list_filter = ('localidad',)
    search_fields = ('nombre',)
    list_display = ('nombre', 'localidad', 'total')

    def total(self, obj):
        suma = obj.movimiento_set.aggregate(Sum('importe'))['importe__sum']
        if suma:
            return"$ {0}".format(suma)

class MovimientoAdmin(admin.ModelAdmin):
    fields = ('cuenta', 'fecha', 'comprobante', 'importe')
    date_hierarchy = 'fecha'
    list_filter = ('cuenta__nombre',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['cuenta', 'fecha', 'importe']
        else:
            return []


admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Cuenta, CuentaAdmin)
admin.site.register(models.Movimiento, MovimientoAdmin)
