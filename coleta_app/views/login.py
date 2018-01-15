# coding:utf-8
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        form = AuthenticationForm()
        context_dict['form'] = form
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_name, context_dict)

    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}

        username = request.POST['username']
        passwd = request.POST['password']

        user = authenticate(username=username, password=passwd)
        if user is not None and user.is_active:
            login(request, user)
        else:
            if User.objects.filter(username=username).count() > 0:
                msg = 'Senha incorreta.'
            else:
                msg = 'Email ou Senha incorretos.'

            form = AuthenticationForm()
            context_dict['form'] = form
            tipo_msg = 'red'

        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, "index.html", context_dict)
