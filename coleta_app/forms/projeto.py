# coding: utf-8
from django import forms
from coleta_app.models.projeto import ProjetoModel
from coleta_app.models.pessoa import PessoaModel


class ProjetoForm(forms.ModelForm):
    orientador = forms.ModelChoiceField(required=True,
                                        empty_label="Selecione um orientador",
                                        queryset=PessoaModel.objects.all(),
                                        widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"}))
    integrantes = forms.ModelMultipleChoiceField(required=True,
                                                 queryset=PessoaModel.objects.all(),
                                                 widget=forms.SelectMultiple(
                                                     attrs={"class": "ui fluid search selection dropdown"})
                                                 )

    class Meta:
        model = ProjetoModel
        fields = '__all__'
        exclude = ('quem_cadastrou', 'data_cadastro')
