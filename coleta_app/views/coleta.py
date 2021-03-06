# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from django.views.generic.base import View
from coleta_app.forms.coleta import ColetaForm
import binascii
import os


class ColetaView(View):
    template = 'cruds/coleta.html'
    template_view = 'coleta.html'

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}

        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                coleta = ColetaModel.objects.get(pk=id)
            except:
                raise Http404("Coleta não encontrada.")
            form = ColetaForm(instance=coleta)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = ColetaForm()

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    def post(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}

        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                coleta = ColetaModel.objects.get(pk=id)
            except:
                raise Http404("Coleta não encontrada.")
            form = ColetaForm(instance=coleta, data=request.POST)
            if form.is_valid():
                ColetaModel.objects.filter(pk=id).update(id_controlador=request.POST['id_controlador'],
                                                         contexto=request.POST['contexto'],
                                                         status=request.POST['status'],
                                                         data_inicio=request.POST['data_inicio'],
                                                         data_fim=request.POST['data_fim'],
                                                         projeto=request.POST['projeto'])
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = ColetaForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                numero_de_caracteres = 5
                token = binascii.hexlify(os.urandom(numero_de_caracteres))
                obj.token = token
                obj.save()
                msg = 'Coleta cadastrada com sucesso!'
                tipo_msg = 'green'
                form = ColetaForm()
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
    def VisualizarColeta(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            context_dict['coleta'] = ColetaModel.objects.get(pk=id)
        except:
            raise Http404("Coleta não encontrada.")

        context_dict['dados'] = DadosModel.objects.filter(coleta_id=id)[:5]
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_view, context_dict)
