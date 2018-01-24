# coding: utf-8
from django import forms
from coleta_app.models.pessoa import PessoaModel


class PessoaForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    turma = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = PessoaModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')
