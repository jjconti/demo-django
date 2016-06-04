from django.contrib import admin

import models


class LocalidadAdmin(admin.ModelAdmin):
    pass


class CuentaAdmin(admin.ModelAdmin):
    list_filter = ('localidad',)


class MovimientoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_filter = ('cuenta__nombre',)


admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Cuenta, CuentaAdmin)
admin.site.register(models.Movimiento, MovimientoAdmin)
