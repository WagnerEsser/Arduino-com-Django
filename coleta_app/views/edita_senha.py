# coding:utf-8
from django.http import Http404
from coleta_app.forms.pessoa import PessoaPasswordForm
from django.views.generic.base import View
from coleta_app.models.pessoa import PessoaModel
from django.shortcuts import render


class EditaSenhaView(View):
    template = "cruds/edita_senha.html"

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        form = PessoaPasswordForm()

        try:
            pessoa = PessoaModel.objects.get(pk=id)
        except:
            raise Http404("Usuário não encontrado.")

        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['pessoa'] = pessoa
        context_dict['form'] = form
        return render(request, self.template, context_dict)

    def post(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}

        try:
            pessoa = PessoaModel.objects.get(pk=id)
        except:
            raise Http404("Usuário não encontrado.")

        form = PessoaPasswordForm(instance=pessoa, data=request.POST)

        if form.is_valid():
            form.save()
            msg = 'Sua nova senha foi cadastrada com sucesso.'
            tipo_msg = 'green'
        else:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['pessoa'] = pessoa
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)
