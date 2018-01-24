# coding:utf-8
from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.utils.datetime_safe import datetime

from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from django.views.generic.base import View
from django.db.models import Q
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
        #
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

    # @classmethod
    # def AtualizaCid(self, request):
    #     funcoes = CidModel.objects.filter(excluido=False)
    #     json = serializers.serialize("json", funcoes)
    #     return HttpResponse(json)

    # @classmethod
    # def ListaCids(self, request, msg=None, tipo_msg=None):
    #     if verifica_login_permissao(request, grupo=ADMINISTRATIVO_NAME) != 1:
    #         return verifica_login_permissao(request, grupo=ADMINISTRATIVO_NAME)
    #
    #     context_dict = {}
    #     if request.GET:
    #         ''' SE EXISTIR PAGINAÇÃO OU FILTRO; CASO EXISTA FILTRO MAS NÃO EXISTA PAGINAÇÃO,
    #         FARÁ A PAGINAÇÃO COM VALOR IGUAL À ZERO '''
    #         if 'filtro' in request.GET:
    #             gravidade = None
    #             if request.GET.get('filtro').lower() in 'sim':
    #                 gravidade = True
    #             elif request.GET.get('filtro').lower() in 'não':
    #                 gravidade = False
    #
    #             cids = CidModel.objects.filter(
    #                 Q(descricao__icontains=request.GET.get('filtro'), excluido=False) |
    #                 Q(cod_cid__icontains=request.GET.get('filtro'), excluido=False) |
    #                 Q(gravidade=gravidade, excluido=False)).order_by('descricao')
    #         else:
    #             cids = CidModel.objects.filter(excluido=False)
    #     else:
    #         cids = CidModel.objects.filter(excluido=False).order_by('descricao')
    #
    #     dados, page_range, ultima = pagination(cids, request.GET.get('page'))
    #
    #     context_dict['dados'] = dados
    #     context_dict['page_range'] = page_range
    #     context_dict['ultima'] = ultima
    #     context_dict['msg'] = msg
    #     context_dict['tipo_msg'] = tipo_msg
    #     context_dict['filtro'] = request.GET.get('filtro')
    #     return render(request, self.template_lista, context_dict)
    #
    # @classmethod
    # def CidDelete(self, request, id=None):
    #     if verifica_login_permissao(request, grupo=ADMINISTRADOR_GERAL_NAME) != 1:
    #         return verifica_login_permissao(request, grupo=ADMINISTRADOR_GERAL_NAME)
    #
    #     try:
    #         cid = CidModel.objects.get(pk=id)
    #     except:
    #         raise Http404("CID não encontrado.")
    #     cid.excluido = True
    #     cid.save()
    #     msg = 'CID excluído com sucesso!'
    #     tipo_msg = 'green'
    #     return self.ListaCids(request, msg, tipo_msg)

    @classmethod
    def VisualizarColeta(self, request, id=None):
        context_dict = {}
        try:
            context_dict['coleta'] = ColetaModel.objects.get(pk=id)
        except:
            raise Http404("Coleta não encontrada.")
        context_dict['dados'] = DadosModel.objects.filter(coleta_id=id)[:10]
        return render(request, self.template, context_dict)
