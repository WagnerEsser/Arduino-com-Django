from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from coleta_app.models.pessoa import PessoaModel
from coleta_app.models.projeto import ProjetoModel
from coleta_app.models.coleta import ColetaModel
from django.db.models import Q


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    context_dict = {}
    # usuario = PessoaModel.objects.get(pk=2)
    id_user = request.user.pk
    print(id_user)
    projetos = ProjetoModel.objects.filter(
        Q(pessoa_projeto__pessoa=id_user) |
        Q(orientador=id_user)).order_by('nome')
    coletas = ColetaModel.objects.filter(projeto__in=projetos)

    context_dict['projetos'] = projetos
    context_dict['coletas'] = coletas
    return render(request, "index.html", context_dict)
