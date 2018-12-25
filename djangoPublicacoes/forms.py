from django import forms
from django.forms import ModelForm,Textarea,TextInput,ClearableFileInput
from .models import termosUalg,publicacoes

class ExclusoesForm(ModelForm):
    class Meta:
        model = termosUalg
        fields = ['termo']
        widgets = {
            'termo':forms.Select(choices=termosUalg.objects.all().values_list()),
        }