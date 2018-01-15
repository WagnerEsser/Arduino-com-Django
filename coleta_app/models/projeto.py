# coding:utf-8
from djongo import models
from coleta_app.models.pessoa import PessoaModel


class ProjetoModel(models.Model):
    nome = models.CharField(max_length=100)
    orientador = models.ForeignKey(PessoaModel, related_name="orientador", null=True, on_delete=models.SET_NULL)
    data_cadastro = models.CharField(max_length=100)
    quem_cadastrou = models.ForeignKey(PessoaModel, related_name="quem_cadastrou", null=True, on_delete=models.SET_NULL)
    integrantes = models.ManyToManyField(PessoaModel, related_name="integrantes", through='Pessoa_Projeto')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"


class Pessoa_Projeto(models.Model):
    projeto = models.ForeignKey(ProjetoModel, null=True, on_delete=models.SET_NULL)
    pessoa = models.ForeignKey(PessoaModel, null=True, on_delete=models.SET_NULL)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __unicode__(self):
        return self.pessoa.get_full_name() + " - " + self.projeto.nome

    def __str__(self):
        return self.pessoa.get_full_name() + " - " + self.projeto.nome

    class Meta:
        verbose_name = "Integrante - Projeto"
        verbose_name_plural = "Integrantes dos projetos"
