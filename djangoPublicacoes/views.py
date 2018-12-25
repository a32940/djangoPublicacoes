from .models import publicacoes, termosUalg,termosHospital,termosUnidadeOrganica,centroInvestigacao,paises
from django.shortcuts import get_object_or_404, render,redirect,render_to_response
from django.http import HttpResponse, JsonResponse
import json
from .forms import ExclusoesForm
import operator
from django.db.models import Q
from functools import reduce


def verExclusoes(request):
    #user = User.objects.get(username=request.user.get_username())
    allExclusions = termosUalg.objects.all().values()
    # return render (request ,{'exclusoes':exclusoesVer})
    #return HttpResponse(list(json.dumps(exclusoesVer)), content_type="application/json")
    #return JsonResponse({"exclusoes": list(allExclusions)})
    return render (request ,"verExclusoes.html",{"form": ExclusoesForm ,"titulo" : allExclusions})

def listaExclusoes(request):
    #user = User.objects.get(username=request.user.get_username())
    allExclusions = termosUalg.objects.all().values()
    # return render (request ,{'exclusoes':exclusoesVer})
    #return HttpResponse(list(json.dumps(exclusoesVer)), content_type="application/json")
    return JsonResponse({"exclusoes": list(allExclusions)})
    #return render (request ,"verExclusoes.html",{"form": ExclusoesForm ,"titulo" : allExclusions})





def verAfiliacao(request):
    termos = termosUalg.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)
    print(termosProcura)
    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    # print(resultados)


    # django export por xls cmo default

    conta = 0
    for i in resultados:
        conta = conta +1
        publicacoes.objects.filter(pk=i['id']).update(UalgAfiliacao= "sim")
    print(conta)

    # print (resultados.id)
    #print(resultados)
    return JsonResponse({"exclusoes": list("cc")})


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
    return JsonResponse({"exclusoes": list("cc")})


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
    return JsonResponse({"exclusoes": list("cc")})

def verCentroInvestigacao(request):
    termos = centroInvestigacao.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)

    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    # print((termos))
    for i in range(len(resultados)):
        CCs = []
        for x in range(len(termosProcura)):
            if (str(termosProcura[x]) in resultados[i]["C1"]):
                CCs.append(str(termosProcura[x]))
                publicacoes.objects.filter(pk=resultados[i]["id"]).update(centroInvestigacao=", ".join(CCs))
    return JsonResponse({"exclusoes": list("cc")})

def verPaises(request):
    termos = paises.objects.all()
    termosProcura = []
    for x in termos:
        termosProcura.append(x)

    clauses = (Q(C1__icontains=p) for p in termosProcura)
    query = reduce(operator.or_, clauses)
    resultados = publicacoes.objects.filter(query).values()
    print((termos))
    for i in range(len(resultados)):
        todosPaises = []
        for x in range(len(termosProcura)):
            if (str(termosProcura[x]) in resultados[i]["C1"]):
                todosPaises.append(str(termosProcura[x]))
                publicacoes.objects.filter(pk=resultados[i]["id"]).update(pais=", ".join(todosPaises))
    return JsonResponse({"exclusoes": list("cc")})