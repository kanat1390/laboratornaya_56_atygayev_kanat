from django import forms
from .models import Product 

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Введите название товара'}),
            'description': forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'Введите описание товара'}),
            'category': forms.Select(attrs={'class':'form-control mb-3', 'id':'category'}),
            'qty':forms.TextInput(attrs={'class':'form-control mb-3', 'id':'qty'}),
            'price':forms.TextInput(attrs={'class':'form-control mb-3', 'id':'price'}),
            'image':forms.FileInput(attrs={'class':'form-control mb-3', 'id':'image'}),
        }

