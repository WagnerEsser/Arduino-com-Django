# coding:utf-8
from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.core import serializers
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from django.views.generic.base import View
from django.db.models import Q
from coleta_app.forms.pessoa import PessoaForm
from coleta_app.models.pessoa import PessoaModel


class PessoaView(View):
    template = 'cruds/pessoa.html'
    template_perfil = 'perfil.html'

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}

        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                pessoa = PessoaModel.objects.get(pk=id)
            except:
                raise Http404("Pessoa não encontrada.")
            form = PessoaForm(instance=pessoa)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = PessoaForm()
        #
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
                pessoa = PessoaModel.objects.get(pk=id)
            except:
                raise Http404("Pessoa não encontrada.")
            form = PessoaForm(instance=pessoa, data=request.POST)
            if form.is_valid():
                # form.save()
                PessoaModel.objects.filter(pk=id).update(first_name=request.POST['first_name'],
                                                         last_name=request.POST['last_name'],
                                                         turma=request.POST['turma'],
                                                         email=request.POST['email'],
                                                         username=request.POST['username'])
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = PessoaForm(data=request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                print(user.password)
                user.set_password(user.password)
                print(user.password)
                user.save()
                msg = 'Pessoa cadastrada com sucesso!'
                tipo_msg = 'green'
                form = PessoaForm()
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
    def perfil(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            context_dict['pessoa'] = PessoaModel.objects.get(pk=request.user.id)
        except:
            raise Http404("Pessoa não encontrada.")
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_perfil, context_dict)
