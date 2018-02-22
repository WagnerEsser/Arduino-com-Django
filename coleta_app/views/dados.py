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
    msg = None
    tipo_msg = None

    if request.GET:
        if 'token' in request.GET:
            print("Requisição chegou...")

            print("TOKEN: ")
            print(request.GET['token'])

            coleta = ColetaModel.objects.get(token=request.GET['token'])
            print("ID da coleta: ")
            print(coleta.id)

            if 'local' in request.GET:
                print("Local: ")
                print(request.GET['local'])

            if 'data' in request.GET:
                print("Data: ")
                print(request.GET['data'])

            if 'hora' in request.GET:
                print("Hora: ")
                print(request.GET['hora'])

            if 'sensor' in request.GET:
                print("Sensor: ")
                print(request.GET['sensor'])

            if 'tipo_sensor' in request.GET:
                print("Tipo do sensor: ")
                print(request.GET['tipo_sensor'])

            if 'dado' in request.GET:
                print("Dado: ")
                print(request.GET['dado'])

            if 'unidade_medida' in request.GET:
                print("Unidade de medida: ")
                print(request.GET['unidade_medida'])

            try:
                DadosModel.objects.create(nome_projeto=request.GET['nome_projeto'],
                                          orientador_projeto=request.GET['orientador_projeto'],
                                          coleta_id=request.GET['coleta_id'],
                                          contexto=request.GET['contexto'],
                                          local=request.GET['local'],
                                          data=request.GET['data'],
                                          hora=request.GET['hora'],
                                          sensor=request.GET['sensor'],
                                          tipo_sensor=request.GET['tipo_sensor'],
                                          dado=request.GET['dado'],
                                          unidade_medida=request.GET['unidade_medida'],
                                          id_controlador=request.GET['id_controlador'],
                                          token=request.GET['token'],
                                          )
                msg = "Nova requisição chegou --> Dados gravados com sucesso"
                tipo_msg = 'green'
            except:
                msg = "Nova requisição cehgou --> ERRO! Os dados não foram gravados"
                tipo_msg = 'red'
        else:
            msg = "É necessário um token de autenticação."
            tipo_msg = "red"
            print(msg)
    else:
        msg = "Não existe uma requisição GET."
        tipo_msg = "yellow"
        print(msg)

    return index(request, msg, tipo_msg)
