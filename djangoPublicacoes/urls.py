"""pubicacoesApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import verAfiliacao, verHospital,verUnidadeOrganica, verCentroInvestigacao, verPaises, guardarPaises, index
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',index,name='index'),
    url(r'verAfiliacao',verAfiliacao,name='verAfiliacao'),
    url(r'verHospital',verHospital,name='verHospital'),
    url(r'verUnidadeOrganica',verUnidadeOrganica,name='verUnidadeOrganica'),
    url(r'verCentroInvestigacao',verCentroInvestigacao,name='verCentroInvestigacao'),
    url(r'verPaises',verPaises,name='verPaises'),
    url(r'guardarPaises',guardarPaises,name='guardarPaises'),
]
