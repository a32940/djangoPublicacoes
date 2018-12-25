from django.contrib import admin
from .models import publicacoes, termosUalg,termosHospital,termosUnidadeOrganica,centroInvestigacao,paises
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats



class PublicacoesAdmin(ImportExportModelAdmin):
    pass

class MyAdmin(PublicacoesAdmin):
    def get_export_formats(self):
            """
            Returns available export formats.
            """
            formats = (
                  # base_formats.CSV,
                  base_formats.XLS,
            )
            return [f for f in formats if f().can_export()]

class modelAdmin(admin.ModelAdmin):
    pass


admin.site.register(publicacoes, MyAdmin)
admin.site.register(termosUalg, modelAdmin)
admin.site.register(termosHospital, modelAdmin)
admin.site.register(termosUnidadeOrganica, modelAdmin)
admin.site.register(centroInvestigacao, modelAdmin)
admin.site.register(paises, modelAdmin)