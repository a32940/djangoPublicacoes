from django import forms
from django.forms import ModelForm,Textarea,TextInput,ClearableFileInput
from .models import exclusoes,publicacoes

class ExclusoesForm(ModelForm):
    class Meta:
        model = exclusoes
        fields = ['termo']
        widgets = {
            'termo':forms.Select(choices=exclusoes.objects.all().values_list()),
        }