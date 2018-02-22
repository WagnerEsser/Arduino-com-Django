# coding:utf-8
from djongo import models
from coleta_app.models.projeto import ProjetoModel


class ColetaModel(models.Model):
    id_controlador = models.CharField(max_length=100)
    contexto = models.CharField(max_length=100)
    CHOICES_STATUS = (
        ('Ativado', 'Ativado'),
        ('Desativado', 'Desativado'),
        ('Fechado', 'Fechado'),
    )
    status = models.CharField(max_length=10, choices=CHOICES_STATUS)
    data_inicio = models.CharField(max_length=100)
    data_fim = models.CharField(max_length=100)
    token = models.CharField(max_length=1000, unique=True)
    projeto = models.ForeignKey(ProjetoModel, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.projeto.nome + " > Coleta: " + str(self.pk) + " - Status: " + self.status

    def __str__(self):
        return self.projeto.nome + " > Coleta: " + str(self.pk) + " - Status: " + self.status

    class Meta:
        verbose_name = "Coleta"
        verbose_name_plural = "Coletas"