from .models import publicacoes, termosUalg,termosHospital,termosUnidadeOrganica,centroInvestigacao,paises
from django.shortcuts import get_object_or_404, render,redirect,render_to_response
from django.http import HttpResponse, JsonResponse
import operator
from django.db.models import Q
from functools import reduce
import requests



def verAfiliacao(request):
    termos = termosUalg.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)
    print(termosProcura)
    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    for i in resultados:
        publicacoes.objects.filter(pk=i['id']).update(UalgAfiliacao= "sim")
    msg = {"msg": "Afiliaçáo Ualg verificada com sucesso"}
    # return render(request, "index.html", msg)
    return redirect('index')



def verHospital(request):
    termos = termosHospital.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)
    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    for i in resultados:
        publicacoes.objects.filter(pk=i['id']).update(Hospital= "sim")
    msg = {"msg": "Hospital verificado com sucesso"}
    # return render(request, "index.html", msg)
    return redirect('index')


def verUnidadeOrganica(request):
    termos = termosUnidadeOrganica.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)
    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    for i in range(len(resultados)):
        UOs = []
        for x in range(len(termosProcura)):
            if (str(termosProcura[x]) in resultados[i]["C1"]):
                UOs.append(str(termosProcura[x]))
                publicacoes.objects.filter(pk=resultados[i]["id"]).update(unidadeOriganica=", ".join(UOs))
    msg = {"msg": "Unidades orgânicas verificados com sucesso"}
    # return render(request, "index.html", msg)
    return redirect('index')

def verCentroInvestigacao(request):
    termos = centroInvestigacao.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)
    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    for i in range(len(resultados)):
        CCs = []
        for x in range(len(termosProcura)):
            if (str(termosProcura[x]) in resultados[i]["C1"]):
                CCs.append(str(termosProcura[x]))
                publicacoes.objects.filter(pk=resultados[i]["id"]).update(centroInvestigacao=", ".join(CCs))
    msg = {"msg": "Centros de investigação verificados com sucesso"}
    #return render(request, "index.html", msg)
    return redirect('index')

def verPaises(request):
    termos = paises.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)
    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    for i in range(len(resultados)):
        todosPaises = []
        for x in range(len(termosProcura)):
            if (str(termosProcura[x]) in resultados[i]["C1"]):
                todosPaises.append(str(termosProcura[x]))
                publicacoes.objects.filter(pk=resultados[i]["id"]).update(pais=", ".join(todosPaises))
    msg = {"msg":"Paises verificados com sucesso"}
    # return render(request, "index.html",msg)
    return redirect('index')


def guardarPaises(request):
    r = requests.get('https://restcountries.eu/rest/v2/all')
    for i in range(len(r.json())):
        if(r.json()[i]["name"]):
            paises.objects.create(termo=r.json()[i]["name"])
    return JsonResponse({"paises": "Paises importados com sucesso"})

def index (request):
    return render(request, "index.html")
