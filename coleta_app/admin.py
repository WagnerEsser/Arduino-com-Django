from django.contrib import admin
from coleta_app.models.pessoa import PessoaModel
from coleta_app.models.projeto import ProjetoModel, Pessoa_Projeto
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from import_export import resources

admin.site.register(PessoaModel)
admin.site.register(ProjetoModel)
admin.site.register(Pessoa_Projeto)
admin.site.register(ColetaModel)
admin.site.register(DadosModel)


class DadosResource(resources.ModelResource):

    class Meta:
        model = DadosModel
        fields = ('nome_projeto', 'orientador_projeto', 'contexto', 'local', 'data', 'hora', 'sensor',
                  'tipo_sensor', 'id_controlador', 'unidade_medida', 'dado')
