from django.contrib import admin
from coleta_app.models.pessoa import PessoaModel
from coleta_app.models.projeto import ProjetoModel
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel

admin.site.register(PessoaModel)
admin.site.register(ProjetoModel)
admin.site.register(ColetaModel)
admin.site.register(DadosModel)
