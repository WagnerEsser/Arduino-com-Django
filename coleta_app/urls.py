from django.conf.urls import url
from django.views.generic import TemplateView
from coleta_app import views
from coleta_app.views.login import LoginView
from coleta_app.views.coleta import ColetaView
from coleta_app.views.pessoa import PessoaView
from coleta_app.views.projeto import ProjetoView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', TemplateView.as_view(template_name='contato.html'), name='contato'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/', LoginView.logout, name='logout'),
    url(r'^perfil/$', TemplateView.as_view(template_name='perfil.html'), name='perfil'),
    url(r'^edita_perfil/$', TemplateView.as_view(template_name='cruds/edita_perfil.html'), name='edita_perfil'),

    # CRUDS
    url(r'^novo_projeto/$', ProjetoView.as_view(), name='novo_projeto'),
    url(r'^edita_projeto/(?P<id>\d+)/$', ProjetoView.as_view(), name='novo_projeto'),
    url(r'^nova_coleta/$', ColetaView.as_view(), name='nova_coleta'),
    url(r'^edita_coleta/(?P<id>\d+)/$', ColetaView.as_view(), name='edita_coleta'),
    url(r'^novo_sensor/$', TemplateView.as_view(template_name='cruds/novo_sensor.html'), name='novo_sensor'),
    url(r'^novo_local/$', TemplateView.as_view(template_name='cruds/novo_local.html'), name='novo_local'),
    url(r'^nova_pessoa/$', PessoaView.as_view(), name='nova_pessoa'),
    url(r'^edita_pessoa/(?P<id>\d+)/$', PessoaView.as_view(), name='edita_pessoa'),

    # LISTAS
    url(r'^sensores/$', TemplateView.as_view(template_name='listas/sensores.html'), name='lista_sensores'),
    url(r'^sensores_projetos/$', TemplateView.as_view(template_name='listas/sensores_projetos.html'), name='lista_sensores_projetos'),
    url(r'^dados/$', TemplateView.as_view(template_name='listas/dados.html'), name='lista_dados'),

    # DEMAIS
    url(r'^coleta/(?P<id>\d+)/$', ColetaView.VisualizarColeta, name='coleta'),
    url(r'^exportar_dados/$', TemplateView.as_view(template_name='exportar_dados.html'), name='exportar_dados'),

    # 404
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
