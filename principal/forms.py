from django import forms
from principal.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(),
        }