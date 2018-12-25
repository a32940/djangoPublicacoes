from django.contrib import admin
from .models import publicacoes, termosUalg,termosHospital,termosUnidadeOrganica,centroInvestigacao,paises

from import_export.admin import ImportExportModelAdmin

class PublicacoesAdmin(ImportExportModelAdmin):
    pass

class modelAdmin(admin.ModelAdmin):
    pass


admin.site.register(publicacoes, PublicacoesAdmin)
admin.site.register(termosUalg, modelAdmin)
admin.site.register(termosHospital, modelAdmin)
admin.site.register(termosUnidadeOrganica, modelAdmin)
admin.site.register(centroInvestigacao, modelAdmin)
admin.site.register(paises, modelAdmin)