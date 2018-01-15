from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from coleta_app.models.pessoa import PessoaModel
from coleta_app.models.projeto import ProjetoModel
from coleta_app.models.coleta import ColetaModel


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    context_dict = {}
    # usuario = PessoaModel.objects.get(pk=2)
    projetos = ProjetoModel.objects.all()
    coletas = ColetaModel.objects.filter(projeto__in=projetos)

    context_dict['projetos'] = projetos
    context_dict['coletas'] = coletas
    return render(request, "index.html", context_dict)
