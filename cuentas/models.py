from __future__ import unicode_literals

from django.db import models


class Localidad(models.Model):

    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class Cuenta(models.Model):

    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    localidad = models.ForeignKey(Localidad)
    email = models.EmailField()

    def __unicode__(self):
        return "{0}-{1}-{2}".format(self.nombre, self.localidad, self.email)


class Movimiento(models.Model):

    cuenta = models.ForeignKey(Cuenta)
    comprobante = models.TextField()
    fecha = models.DateField()
    signo = models.CharField(max_length=1, choices=[('+', '+'), ('-', '-')])
    importe = models.DecimalField(max_digits=20, decimal_places=4)

    def __unicode__(self):
        return "{0}{1} ({2})".format(self.signo, self.importe, self.fecha)
