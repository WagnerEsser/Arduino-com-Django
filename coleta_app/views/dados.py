# coding:utf-8
from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.core import serializers
from coleta_app.models.coleta import ColetaModel
from coleta_app.models.dados import DadosModel
from django.views.generic.base import View
from django.db.models import Q
from coleta_app.forms.coleta import ColetaForm
import binascii
import os
from coleta_app.views.index import index


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
