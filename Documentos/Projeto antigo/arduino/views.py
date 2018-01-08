# coding:utf-8
from django.shortcuts import render
from arduino.models import ColetaModel


def index(request):

    if request.GET:
        print("Requisição chegou...")
        print("ID Controlador: ")
        print(request.GET['idcontrolador'])
        print("Temperatura: ")
        print(request.GET['temperatura'])
        print("Umidade: ")
        print(request.GET['umidade'])
        ColetaModel.objects.create(temperatura=request.GET['temperatura'], umidade=request.GET['umidade'],
                                          equipamento="Arduino MEGA + Ethernet Shield + DHT22",
                                          id_controlador=request.GET['idcontrolador'])
        print("Nova requisição chegou --> Dados gravados com sucesso")

    print("Abrindo index.html")
    return render(request, 'index.html', {'dados': ColetaModel.objects.all()})
