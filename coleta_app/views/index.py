from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from coleta_app.models.pessoa import PessoaModel
from coleta_app.models.projeto import ProjetoModel
from coleta_app.models.coleta import ColetaModel
from django.db.models import Q


def index(request, msg=None, tipo_msg=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    context_dict = {}
    if not request.user.is_superuser:
        usuario = PessoaModel.objects.get(pk=request.user.id)
        query = ProjetoModel.objects.filter(
            Q(orientador=usuario.pk) |
            Q(quem_cadastrou=usuario.pk) |
            Q(pessoa_projeto__pessoa=usuario.pk)).order_by('nome')
        projetos = list(set(query))
        coletas = ColetaModel.objects.filter(projeto__in=projetos)

        context_dict['projetos'] = projetos
        context_dict['coletas'] = coletas

    context_dict['msg'] = msg
    context_dict['tipo_msg'] = tipo_msg
    return render(request, "index.html", context_dict)
