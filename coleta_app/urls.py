from django.conf.urls import url
from coleta_app import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', TemplateView.as_view(template_name='contato.html'), name='contato'),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^perfil/$', TemplateView.as_view(template_name='perfil.html'), name='perfil'),
    url(r'^edita_perfil/$', TemplateView.as_view(template_name='cruds/edita_perfil.html'), name='edita_perfil'),

    # CRUDS
    url(r'^novo_projeto/$', TemplateView.as_view(template_name='cruds/novo_projeto.html'), name='novo_projeto'),
    url(r'^nova_coleta/$', TemplateView.as_view(template_name='cruds/nova_coleta.html'), name='nova_coleta'),
    url(r'^novo_sensor/$', TemplateView.as_view(template_name='cruds/novo_sensor.html'), name='novo_sensor'),
    url(r'^novo_local/$', TemplateView.as_view(template_name='cruds/novo_local.html'), name='novo_local'),
    url(r'^nova_pessoa/$', TemplateView.as_view(template_name='cruds/nova_pessoa.html'), name='nova_pessoa'),

    # LISTAS
    url(r'^sensores/$', TemplateView.as_view(template_name='listas/sensores.html'), name='lista_sensores'),
    url(r'^sensores_projetos/$', TemplateView.as_view(template_name='listas/sensores_projetos.html'), name='lista_sensores_projetos'),
    url(r'^dados/$', TemplateView.as_view(template_name='listas/dados.html'), name='lista_dados'),

    # DEMAIS
    url(r'^coleta/$', TemplateView.as_view(template_name='coleta.html'), name='coleta'),
    url(r'^exportar_dados/$', TemplateView.as_view(template_name='exportar_dados.html'), name='exportar_dados'),

    # 404
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
