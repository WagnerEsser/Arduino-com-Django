# coding:utf-8
from djongo import models


class DadosModel(models.Model):
    nome_projeto = models.CharField(max_length=100)
    orientador_projeto = models.CharField(max_length=100)
    contexto = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    sensor = models.CharField(max_length=100)
    tipo_sensor = models.CharField(max_length=100)
    dado = models.CharField(max_length=100)
    unidade_medida = models.CharField(max_length=100)
    id_controlador = models.CharField(max_length=100)

    def __unicode__(self):
        return self.contexto + " > " + self.dado + " " + self.unidade_medida + " - " + self.data + " - " + self.hora

    def __str__(self):
        return self.contexto + " > " + self.dado + " " + self.unidade_medida + " - " + self.data + " - " + self.hora

    class Meta:
        verbose_name = "Dado"
        verbose_name_plural = "Dados"
