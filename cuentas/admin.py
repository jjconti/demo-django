from django.contrib import admin

import models


class LocalidadAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    readonly_fields = ('nombre',)


class CuentaAdmin(admin.ModelAdmin):
    list_filter = ('localidad',)
    search_fields = ('nombre',)


class MovimientoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_filter = ('cuenta__nombre',)
    readonly_fields = ('cuenta', 'fecha', 'importe', 'signo')


admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Cuenta, CuentaAdmin)
admin.site.register(models.Movimiento, MovimientoAdmin)
