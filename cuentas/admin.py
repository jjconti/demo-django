from django.contrib import admin

import models


class MovimientoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'


admin.site.register(models.Localidad)
admin.site.register(models.Cuenta)
admin.site.register(models.Movimiento, MovimientoAdmin)
