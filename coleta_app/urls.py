from django.conf.urls import url
from django.views.generic import TemplateView
from coleta_app import views
from coleta_app.views.login import LoginView
from coleta_app.views.coleta import ColetaView
from coleta_app.views.pessoa import PessoaView
from coleta_app.views.projeto import ProjetoView
from coleta_app.views.edita_senha import EditaSenhaView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', TemplateView.as_view(template_name='contato.html'), name='contato'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/', LoginView.logout, name='logout'),
    url(r'^perfil/$', PessoaView.perfil, name='perfil'),

    # REFERENTE A USUÁRIO
    url(r'^nova_pessoa/$', PessoaView.as_view(), name='nova_pessoa'),
    url(r'^edita_pessoa/(?P<id>\d+)/$', PessoaView.as_view(), name='edita_pessoa'),
    url(r'^edita/senha/(?P<id>\d+)/$', EditaSenhaView.as_view(), name='edita_senha'),

    # CRUDS
    url(r'^novo_projeto/$', ProjetoView.as_view(), name='novo_projeto'),
    url(r'^edita_projeto/(?P<id>\d+)/$', ProjetoView.as_view(), name='edita_projeto'),
    url(r'^nova_coleta/$', ColetaView.as_view(), name='nova_coleta'),
    url(r'^edita_coleta/(?P<id>\d+)/$', ColetaView.as_view(), name='edita_coleta'),

    # DEMAIS
    url(r'^dados/(?P<id>\d+)/$', views.lista_dados, name='lista_dados'),
    url(r'^novo_dado$', views.novo_dado, name='novo_dado'),
    url(r'^coleta/(?P<id>\d+)/$', ColetaView.VisualizarColeta, name='coleta'),
    url(r'^exportar_dados/(?P<id>\d+)/$', views.exportar_dados, name='exportar_dados'),
    url(r'^download/(?P<id>\d+)/$', views.download_dados, name='download_dados'),

    # 404
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
