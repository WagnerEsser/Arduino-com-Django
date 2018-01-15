# coding:utf-8
from djongo import models
from django.contrib.auth.models import User


class ColetaModel(models.Model):
    id_controlador = models.CharField(max_length=100)
    contexto = models.CharField(max_length=100)
    CHOICES_STATUS = (
        ('Ativado', 'Ativado'),
        ('Desativado', 'Desativado'),
        ('Fechado', 'Fechado'),
    )
    status = models.CharField(max_length=10, choices=CHOICES_STATUS)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    token = models.CharField(max_length=1000)
    projeto = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Coleta"
        verbose_name_plural = "Coletas"