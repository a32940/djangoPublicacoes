from .models import publicacoes, exclusoes
from django.shortcuts import get_object_or_404, render,redirect,render_to_response
from django.http import HttpResponse, JsonResponse
import json
from .forms import ExclusoesForm

def verExclusoes(request):
    #user = User.objects.get(username=request.user.get_username())
    allExclusions = exclusoes.objects.all().values()
    # return render (request ,{'exclusoes':exclusoesVer})
    #return HttpResponse(list(json.dumps(exclusoesVer)), content_type="application/json")
    #return JsonResponse({"exclusoes": list(allExclusions)})
    return render (request ,"verExclusoes.html",{"form": ExclusoesForm ,"titulo" : allExclusions})

def listaExclusoes(request):
    #user = User.objects.get(username=request.user.get_username())
    allExclusions = exclusoes.objects.all().values()
    # return render (request ,{'exclusoes':exclusoesVer})
    #return HttpResponse(list(json.dumps(exclusoesVer)), content_type="application/json")
    return JsonResponse({"exclusoes": list(allExclusions)})
    #return render (request ,"verExclusoes.html",{"form": ExclusoesForm ,"titulo" : allExclusions})