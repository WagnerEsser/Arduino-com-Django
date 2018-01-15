from django.contrib import admin
from coleta_app.models.pessoa import PessoaModel
from coleta_app.models.projeto import ProjetoModel, Pessoa_Projeto
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel

admin.site.register(PessoaModel)
admin.site.register(ProjetoModel)
admin.site.register(Pessoa_Projeto)
admin.site.register(ColetaModel)
admin.site.register(DadosModel)
