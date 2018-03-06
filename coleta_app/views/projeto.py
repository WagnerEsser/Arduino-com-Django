# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from django.views.generic.base import View
from coleta_app.forms.projeto import ProjetoForm
from coleta_app.models.projeto import ProjetoModel, Pessoa_Projeto
from coleta_app.models.pessoa import PessoaModel


class ProjetoView(View):
    template = 'cruds/novo_projeto.html'

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}

        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                pessoa = ProjetoModel.objects.get(pk=id)
            except:
                raise Http404("Pessoa não encontrada.")
            form = ProjetoForm(instance=pessoa)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = ProjetoForm()

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}

        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                pessoa = ProjetoModel.objects.get(pk=id)
            except:
                raise Http404("Projeto não encontrado.")
            form = ProjetoForm(instance=pessoa, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = ProjetoForm(data=request.POST)
            if form.is_valid():
                projeto = form.save(commit=False)
                projeto.data_cadastro = datetime.now().date()
                projeto.quem_cadastrou = PessoaModel.objects.get(pk=request.user.pk)
                projeto.save()
                for integrante in form.cleaned_data['integrantes']:
                    pessoa_projeto = Pessoa_Projeto()
                    pessoa_projeto.pessoa = integrante
                    pessoa_projeto.projeto = projeto
                    pessoa_projeto.data_inicio = datetime.now().date()
                    pessoa_projeto.save()
                msg = 'Projeto cadastrado com sucesso!'
                tipo_msg = 'green'
                form = ProjetoForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @classmethod
    def VisualizarColeta(self, request, id=None):
        context_dict = {}
        try:
            context_dict['coleta'] = ColetaModel.objects.get(pk=id)
        except:
            raise Http404("Coleta não encontrada.")
        context_dict['dados'] = DadosModel.objects.filter(coleta_id=id)[:10]
        return render(request, self.template, context_dict)
