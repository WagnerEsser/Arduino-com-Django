# coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from coleta_app.views import ColetaView
from coleta_app.views.index import index
from django.http import HttpResponse
from coleta_app.admin import DadosResource


def novo_dado(request):

    if request.GET:
        if 'token' in request.GET:
            if 'dado' in request.GET:
                print("Requisição chegou...")

                print("TOKEN: ")
                print(request.GET['token'])

                print("Dado: ")
                print(request.GET['dado'])

                try:
                    coleta = ColetaModel.objects.get(token=request.GET['token'])
                except:
                    msg = "Não foi encontrado dados para este TOKEN!"
                    tipo_msg = "red"
                    print(msg)
                    return index(request, msg, tipo_msg)

                print("ID da coleta: ")
                print(coleta.id)

                if coleta.status != "Desativado" and coleta.status != "Fechado":
                    nome_projeto = coleta.projeto.nome
                    orientador_projeto = coleta.projeto.orientador.get_full_name()
                    dado = request.GET['dado']

                    if 'local' in request.GET:
                        print("Local: ")
                        print(request.GET['local'])
                        local = request.GET['local']
                    else:
                        local = ""

                    if 'data' in request.GET:
                        print("Data: ")
                        print(request.GET['data'])
                        data = request.GET['data']
                    else:
                        data = ""

                    if 'hora' in request.GET:
                        print("Hora: ")
                        print(request.GET['hora'])
                        hora = request.GET['hora']
                    else:
                        hora = ""

                    if 'sensor' in request.GET:
                        print("Sensor: ")
                        print(request.GET['sensor'])
                        sensor = request.GET['sensor']
                    else:
                        sensor = ""

                    if 'tipo_sensor' in request.GET:
                        print("Tipo do sensor: ")
                        print(request.GET['tipo_sensor'])
                        tipo_sensor = request.GET['tipo_sensor']
                    else:
                        tipo_sensor = ""

                    if 'unidade_medida' in request.GET:
                        print("Unidade de medida: ")
                        print(request.GET['unidade_medida'])
                        unidade_medida = request.GET['unidade_medida']
                    else:
                        unidade_medida = ""

                    try:
                        DadosModel.objects.create(nome_projeto=nome_projeto,
                                                  orientador_projeto=orientador_projeto,
                                                  coleta_id=coleta.id,
                                                  contexto=coleta.contexto,
                                                  local=local,
                                                  data=data,
                                                  hora=hora,
                                                  sensor=sensor,
                                                  tipo_sensor=tipo_sensor,
                                                  dado=dado,
                                                  unidade_medida=unidade_medida,
                                                  id_controlador=coleta.id_controlador,
                                                  )
                        msg = "Nova requisição chegou --> Dados gravados com sucesso"
                        tipo_msg = 'green'
                    except:
                        msg = "Nova requisição chegou --> ERRO! Os dados não foram gravados"
                        tipo_msg = 'red'
                    print(msg)
                else:
                    msg = "A coleta não está aberta para recepção de novos dados."
                    tipo_msg = "red"
                    print(msg)
            else:
                msg = "Não foi encontrado o dado coletado."
                tipo_msg = "red"
                print(msg)
        else:
            msg = "É necessário um token de autenticação."
            tipo_msg = "red"
            print(msg)
    else:
        msg = "Não existe uma requisição GET."
        tipo_msg = "yellow"
        print(msg)

    return index(request, msg, tipo_msg)


def lista_dados(request, id=None):
    context_dict = {}
    qtd_por_pagina = 10

    context_dict['previous_page'] = 1
    context_dict['next_page'] = 2
    bd_dados = DadosModel.objects.filter(coleta_id=id)
    context_dict['last_page'] = int(len(bd_dados)/qtd_por_pagina+1)
    if (request.GET and 'page' in request.GET) and (request.GET.get('page') != "") and (int(request.GET.get('page')) != 0):
        page = int(request.GET.get('page'))
        limit_inicio = page*qtd_por_pagina-qtd_por_pagina
        limit_fim = page*qtd_por_pagina
        dados = list(bd_dados)[limit_inicio:limit_fim]
        context_dict['previous_page'] = page-1
        context_dict['next_page'] = page+1
    else:
        dados = bd_dados[0:qtd_por_pagina]

    context_dict['dados'] = dados
    context_dict['id_coleta'] = id
    return render(request, "dados.html", context_dict)


def exportar_dados(request, id=None):
    context_dict = {'id_coleta': id}
    return render(request, 'exportar_dados.html', context_dict)


def download_dados(request, opcao=None, id=None):
    opcao = int(opcao)
    # opções:
    # 1 - CSV
    # 2 - JSON
    # 3 - HTML
    # 4 - XLS
    # 5 - ODS

    response = HttpResponseRedirect(reverse('index'))

    dataset = DadosResource().export()

    # CSV
    if opcao == 1:
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="dados.csv"'

    # JSON
    if opcao == 2:
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="dados.json"'

    # HTML
    if opcao == 3:
        response = HttpResponse(dataset.html, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="dados.html"'

    # XLS
    if opcao == 4:
        response = HttpResponse(dataset.xls, content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="dados.xls"'

    # ODS
    if opcao == 5:
        response = HttpResponse(dataset.ods, content_type='application/vnd.oasis.opendocument.spreadsheet')
        response['Content-Disposition'] = 'attachment; filename="dados.ods"'

    return response