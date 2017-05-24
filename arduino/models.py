# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class ColetaModel(models.Model):
    data = models.DateTimeField(auto_now=True)
    temperatura = models.CharField(max_length=128)
    umidade = models.CharField(max_length=128)
    equipamento = models.CharField(max_length=128)
    id_controlador = models.CharField(max_length=128)

    def __unicode__(self):
        return self.data

    def __str__(self):
        return self.data

    class Meta:
        ordering = ['data']
        verbose_name = u"Coleta"
        verbose_name_plural = u"Coletas"
