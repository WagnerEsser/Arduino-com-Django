# coding: utf-8
from django import forms
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.projeto import ProjetoModel


class ColetaForm(forms.ModelForm):
    projeto = forms.ModelChoiceField(required=True,
                                     empty_label="Selecione um projeto",
                                     queryset=ProjetoModel.objects.all(),
                                     widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"}))
    contexto = forms.CharField(max_length=100)
    id_controlador = forms.CharField(max_length=100)
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    class Meta:
        model = ColetaModel
        fields = '__all__'
        exclude = ('token',)
