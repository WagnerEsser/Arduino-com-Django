# coding:utf-8
from djongo import models
from django.contrib.auth.models import User


class PessoaModel(User):
    turma = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
