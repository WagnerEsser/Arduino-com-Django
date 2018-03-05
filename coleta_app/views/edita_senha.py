# coding:utf-8
from django.http import Http404
from coleta_app.forms.pessoa import PessoaPasswordForm
from django.views.generic.base import View
from coleta_app.models.pessoa import PessoaModel
from django.contrib.auth import logout
from django.shortcuts import render
# from coleta.views.cruds.funcoes import EnviaEmailSenha
# from coleta.grupos import *
# from coleta.views.permissoes import verifica_login_permissao
from django.contrib.auth.forms import AuthenticationForm


class EditaSenhaView(View):
    template = "cruds/edita_senha.html"

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        form = PessoaPasswordForm()

        try:
            pessoa = PessoaModel.objects.get(pk=id)
        except:
            raise Http404("Usuário não encontrado.")

        # if pessoa.primeiro_login:
        #     id = request.session['user_id']
        #     logout(request)
        #     request.session['user_id'] = id
        #     msg = "Bem-vindo ao ISSEM. É necessário criar uma senha para ter acesso ao Sistema."
        #     context_dict['msg_tipo_senha'] = "Defina sua senha"
        #     tipo_msg = "yellow"

        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['pessoa'] = pessoa
        context_dict['form'] = form
        return render(request, self.template, context_dict)

    def post(self, request, id=None, msg=None, tipo_msg=None):
        template = None
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
    #     else:
        #         if request.user.id == pessoa.id:
        #             form.save()
        #             logout(request)
        #
        #             # EnviaEmailSenha(pessoa, alteracao=True, host=request.META['HTTP_HOST'])
        #
        #             form = AuthenticationForm()
        #             msg = 'Sua senha foi alterada com sucesso! É necessário fazer login novamente ' \
        #                                   'para acessar o sistema.'
        #             tipo_msg = 'green'
        #             template = self.template_login
        #         elif verifica_login_permissao(request, grupo=ADMINISTRADOR_GERAL_NAME):
        #             msg = 'Senha de %s foi alterada com sucesso!' % pessoa.get_full_name()
        #             tipo_msg = 'green'
        #             form.save()
        #             EnviaEmailSenha(pessoa, alteracao=True, host=request.META['HTTP_HOST'])
        #             template = self.template
        else:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['pessoa'] = pessoa
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)
