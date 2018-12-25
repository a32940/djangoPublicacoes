from django.contrib import admin
from .models import publicacoes, exclusoes
from import_export.admin import ImportExportModelAdmin

class PublicacoesAdmin(ImportExportModelAdmin):
    pass

class ExclusoesAdmin(admin.ModelAdmin):
    pass

admin.site.register(publicacoes, PublicacoesAdmin)
admin.site.register(exclusoes, ExclusoesAdmin)