from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        choices = ['bar', 'pie']
        model = Product
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_products': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        